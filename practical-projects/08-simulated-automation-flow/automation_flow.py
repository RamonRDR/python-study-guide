"""Deterministic orchestration for a fully simulated automation flow."""

from __future__ import annotations

from dataclasses import dataclass

try:
    from enum import StrEnum
except ImportError:  # Python < 3.11
    from enum import Enum

    class StrEnum(str, Enum):
        """Minimal compatibility backport of enum.StrEnum behavior."""

        def __str__(self) -> str:
            return self.value


class StepName(StrEnum):
    """Ordered execution steps in the simulated automation."""

    PREPARE = "prepare"
    PROCESS = "process"
    VERIFY = "verify"
    FINALIZE = "finalize"


class StepStatus(StrEnum):
    """Final status for one automation step."""

    SUCCEEDED = "succeeded"
    FAILED = "failed"
    SKIPPED = "skipped"


class RunStatus(StrEnum):
    """Final status for one automation run."""

    SUCCEEDED = "succeeded"
    FAILED = "failed"


class EventType(StrEnum):
    """Types of events emitted while the automation runs."""

    STARTED = "started"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    SKIPPED = "skipped"


STEP_ORDER = (
    StepName.PREPARE,
    StepName.PROCESS,
    StepName.VERIFY,
    StepName.FINALIZE,
)


def _normalize_text(value: str, *, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    if not normalized.isprintable():
        raise ValueError(f"{field_name} must contain only printable characters")
    return normalized


@dataclass(frozen=True)
class AutomationRequest:
    """Validated immutable input for one simulated automation run."""

    request_id: str
    items: tuple[str, ...]

    def __post_init__(self) -> None:
        request_id = _normalize_text(self.request_id, field_name="request_id")
        if not isinstance(self.items, tuple):
            raise TypeError("items must be a tuple of strings")
        if not self.items:
            raise ValueError("items must contain at least one value")

        normalized_items = tuple(
            _normalize_text(item, field_name="item") for item in self.items
        )
        if len(normalized_items) != len(set(normalized_items)):
            raise ValueError("items must be unique after normalization")

        object.__setattr__(self, "request_id", request_id)
        object.__setattr__(self, "items", normalized_items)


@dataclass(frozen=True)
class SimulationPolicy:
    """Optional deterministic failure injection for demonstration and tests."""

    fail_at: StepName | None = None

    def __post_init__(self) -> None:
        if self.fail_at is not None and not isinstance(self.fail_at, StepName):
            raise TypeError("fail_at must be a StepName or None")


@dataclass(frozen=True)
class Evidence:
    """One immutable piece of evidence produced by a completed step."""

    step: StepName
    key: str
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.step, StepName):
            raise TypeError("step must be a StepName")
        key = _normalize_text(self.key, field_name="evidence key")
        value = _normalize_text(self.value, field_name="evidence value")
        object.__setattr__(self, "key", key)
        object.__setattr__(self, "value", value)


@dataclass(frozen=True)
class StepResult:
    """Final outcome for exactly one step."""

    step: StepName
    status: StepStatus
    message: str
    evidence: tuple[Evidence, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.step, StepName):
            raise TypeError("step must be a StepName")
        if not isinstance(self.status, StepStatus):
            raise TypeError("status must be a StepStatus")
        message = _normalize_text(self.message, field_name="step message")
        if not isinstance(self.evidence, tuple):
            raise TypeError("evidence must be a tuple")
        if any(not isinstance(item, Evidence) for item in self.evidence):
            raise TypeError("evidence must contain only Evidence values")
        if any(item.step is not self.step for item in self.evidence):
            raise ValueError("step evidence must belong to the same step")
        if self.status is not StepStatus.SUCCEEDED and self.evidence:
            raise ValueError("failed or skipped steps cannot produce evidence")
        object.__setattr__(self, "message", message)


@dataclass(frozen=True)
class AutomationEvent:
    """One deterministic log event emitted by the orchestrator."""

    sequence: int
    step: StepName
    event_type: EventType
    message: str

    def __post_init__(self) -> None:
        if type(self.sequence) is not int:
            raise TypeError("sequence must be an integer")
        if self.sequence < 1:
            raise ValueError("sequence must be at least 1")
        if not isinstance(self.step, StepName):
            raise TypeError("step must be a StepName")
        if not isinstance(self.event_type, EventType):
            raise TypeError("event_type must be an EventType")
        object.__setattr__(
            self,
            "message",
            _normalize_text(self.message, field_name="event message"),
        )


@dataclass(frozen=True)
class AutomationResult:
    """Complete immutable result of one simulated automation run."""

    request: AutomationRequest
    status: RunStatus
    steps: tuple[StepResult, ...]
    events: tuple[AutomationEvent, ...]
    output_items: tuple[str, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.request, AutomationRequest):
            raise TypeError("request must be an AutomationRequest")
        if not isinstance(self.status, RunStatus):
            raise TypeError("status must be a RunStatus")
        if not isinstance(self.steps, tuple):
            raise TypeError("steps must be a tuple")
        if not isinstance(self.events, tuple):
            raise TypeError("events must be a tuple")
        if not isinstance(self.output_items, tuple):
            raise TypeError("output_items must be a tuple")
        if any(not isinstance(step, StepResult) for step in self.steps):
            raise TypeError("steps must contain only StepResult values")
        if any(not isinstance(event, AutomationEvent) for event in self.events):
            raise TypeError("events must contain only AutomationEvent values")
        if tuple(step.step for step in self.steps) != STEP_ORDER:
            raise ValueError("steps must contain the complete canonical step order")

        expected_processed_items = tuple(item.upper() for item in self.request.items)
        statuses = tuple(step.status for step in self.steps)
        if self.status is RunStatus.SUCCEEDED:
            if any(status is not StepStatus.SUCCEEDED for status in statuses):
                raise ValueError("successful runs require every step to succeed")
            if self.output_items != expected_processed_items:
                raise ValueError("successful output_items must match processed items")
            if len(expected_processed_items) != len(set(expected_processed_items)):
                raise ValueError("successful output_items must be unique")
        else:
            failed_indexes = [
                index
                for index, step_status in enumerate(statuses)
                if step_status is StepStatus.FAILED
            ]
            if len(failed_indexes) != 1:
                raise ValueError("failed runs require exactly one failed step")
            failed_index = failed_indexes[0]
            if any(
                step_status is not StepStatus.SUCCEEDED
                for step_status in statuses[:failed_index]
            ):
                raise ValueError("steps before a failure must have succeeded")
            if any(
                step_status is not StepStatus.SKIPPED
                for step_status in statuses[failed_index + 1 :]
            ):
                raise ValueError("steps after a failure must be skipped")
            if self.output_items:
                raise ValueError("failed runs must not publish output_items")

        for step_result in self.steps:
            if step_result.status is not StepStatus.SUCCEEDED:
                continue
            processed_items = (
                ()
                if step_result.step is StepName.PREPARE
                else expected_processed_items
            )
            expected_evidence = _success_evidence(
                step_result.step,
                self.request,
                processed_items,
            )
            if step_result.evidence != expected_evidence:
                raise ValueError(
                    "successful step evidence must match the enclosing request"
                )

        expected_events: list[tuple[StepName, EventType, str]] = []
        for step in self.steps:
            if step.status is StepStatus.SUCCEEDED:
                expected_events.extend(
                    [
                        (
                            step.step,
                            EventType.STARTED,
                            f"{step.step.value} started.",
                        ),
                        (step.step, EventType.SUCCEEDED, step.message),
                    ]
                )
            elif step.status is StepStatus.FAILED:
                expected_events.extend(
                    [
                        (
                            step.step,
                            EventType.STARTED,
                            f"{step.step.value} started.",
                        ),
                        (step.step, EventType.FAILED, step.message),
                    ]
                )
            else:
                expected_events.append(
                    (step.step, EventType.SKIPPED, step.message)
                )

        actual_events = [
            (event.step, event.event_type, event.message)
            for event in self.events
        ]
        if actual_events != expected_events:
            raise ValueError(
                "events must match the canonical step lifecycle and messages"
            )
        if tuple(event.sequence for event in self.events) != tuple(
            range(1, len(self.events) + 1)
        ):
            raise ValueError("event sequences must be contiguous starting at 1")

    @property
    def evidence(self) -> tuple[Evidence, ...]:
        """Return all successful-step evidence in execution order."""

        return tuple(item for step in self.steps for item in step.evidence)


def _success_evidence(
    step: StepName,
    request: AutomationRequest,
    processed_items: tuple[str, ...],
) -> tuple[Evidence, ...]:
    if step is StepName.PREPARE:
        return (
            Evidence(step, "request_id", request.request_id),
            Evidence(step, "input_count", str(len(request.items))),
        )
    if step is StepName.PROCESS:
        return (
            Evidence(step, "processed_count", str(len(processed_items))),
            Evidence(step, "transformation", "uppercase"),
        )
    if step is StepName.VERIFY:
        return (
            Evidence(step, "verified_count", str(len(processed_items))),
            Evidence(step, "verification", "count-and-uniqueness"),
        )
    return (
        Evidence(step, "published_count", str(len(processed_items))),
        Evidence(step, "result", "ready"),
    )


def _append_event(
    events: list[AutomationEvent],
    step: StepName,
    event_type: EventType,
    message: str,
) -> None:
    events.append(
        AutomationEvent(
            sequence=len(events) + 1,
            step=step,
            event_type=event_type,
            message=message,
        )
    )


def run_automation(
    request: AutomationRequest,
    *,
    policy: SimulationPolicy | None = None,
) -> AutomationResult:
    """Run the deterministic simulated automation from validation to result."""

    if not isinstance(request, AutomationRequest):
        raise TypeError("request must be an AutomationRequest")
    if policy is None:
        policy = SimulationPolicy()
    if not isinstance(policy, SimulationPolicy):
        raise TypeError("policy must be a SimulationPolicy or None")

    step_results: list[StepResult] = []
    events: list[AutomationEvent] = []
    processed_items: tuple[str, ...] = ()
    failed = False

    for step in STEP_ORDER:
        if failed:
            message = "Skipped because an earlier step failed."
            step_results.append(
                StepResult(
                    step=step,
                    status=StepStatus.SKIPPED,
                    message=message,
                )
            )
            _append_event(events, step, EventType.SKIPPED, message)
            continue

        _append_event(events, step, EventType.STARTED, f"{step.value} started.")

        if policy.fail_at is step:
            message = f"Simulated failure at {step.value}."
            step_results.append(
                StepResult(
                    step=step,
                    status=StepStatus.FAILED,
                    message=message,
                )
            )
            _append_event(events, step, EventType.FAILED, message)
            failed = True
            continue

        if step is StepName.PROCESS:
            processed_items = tuple(item.upper() for item in request.items)

        if step is StepName.VERIFY and len(processed_items) != len(
            set(processed_items)
        ):
            message = "Verification failed: processed items must be unique."
            step_results.append(
                StepResult(
                    step=step,
                    status=StepStatus.FAILED,
                    message=message,
                )
            )
            _append_event(events, step, EventType.FAILED, message)
            failed = True
            continue

        evidence = _success_evidence(step, request, processed_items)
        message = f"{step.value} completed."
        step_results.append(
            StepResult(
                step=step,
                status=StepStatus.SUCCEEDED,
                message=message,
                evidence=evidence,
            )
        )
        _append_event(events, step, EventType.SUCCEEDED, message)

    status = RunStatus.FAILED if failed else RunStatus.SUCCEEDED
    output_items = () if failed else processed_items
    return AutomationResult(
        request=request,
        status=status,
        steps=tuple(step_results),
        events=tuple(events),
        output_items=output_items,
    )


def render_text_report(result: AutomationResult) -> str:
    """Render a stable human-readable report for the simulated run."""

    if not isinstance(result, AutomationResult):
        raise TypeError("result must be an AutomationResult")

    lines = [
        "Simulated Automation Flow",
        f"Request: {result.request.request_id}",
        f"Run status: {result.status.value}",
        "",
        "Steps",
    ]
    for step in result.steps:
        lines.append(f"[{step.status.value.upper()}] {step.step.value}: {step.message}")

    lines.extend(["", "Events"])
    for event in result.events:
        lines.append(
            f"{event.sequence:03d} {event.step.value} "
            f"{event.event_type.value}: {event.message}"
        )

    lines.extend(["", "Evidence"])
    for evidence in result.evidence:
        lines.append(f"{evidence.step.value}.{evidence.key}={evidence.value}")

    lines.extend(["", "Output"])
    if result.output_items:
        lines.extend(result.output_items)
    else:
        lines.append("<not published>")

    return "\n".join(lines) + "\n"
