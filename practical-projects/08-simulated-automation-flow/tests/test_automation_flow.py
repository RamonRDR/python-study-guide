import pytest

from automation_flow import (
    AutomationEvent,
    AutomationRequest,
    AutomationResult,
    EventType,
    RunStatus,
    SimulationPolicy,
    StepName,
    StepResult,
    StepStatus,
    render_text_report,
    run_automation,
)


def make_request() -> AutomationRequest:
    return AutomationRequest(" RUN-001 ", ("alpha", " beta ", "gamma"))


def test_request_normalizes_text_and_rejects_duplicate_items() -> None:
    request = make_request()
    assert request.request_id == "RUN-001"
    assert request.items == ("alpha", "beta", "gamma")

    with pytest.raises(ValueError, match="unique"):
        AutomationRequest("RUN-002", (" alpha ", "alpha"))


def test_request_requires_immutable_non_empty_items() -> None:
    with pytest.raises(TypeError, match="tuple"):
        AutomationRequest("RUN-001", ["alpha"])  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="at least one"):
        AutomationRequest("RUN-001", ())


def test_successful_run_is_deterministic_and_complete() -> None:
    request = make_request()
    first = run_automation(request)
    second = run_automation(request)

    assert first == second
    assert first.status is RunStatus.SUCCEEDED
    assert tuple(step.step for step in first.steps) == tuple(StepName)
    assert all(step.status is StepStatus.SUCCEEDED for step in first.steps)
    assert first.output_items == ("ALPHA", "BETA", "GAMMA")
    assert tuple(event.sequence for event in first.events) == tuple(range(1, 9))
    assert len(first.evidence) == 8


def test_failure_stops_execution_and_preserves_prior_evidence() -> None:
    result = run_automation(
        make_request(),
        policy=SimulationPolicy(fail_at=StepName.VERIFY),
    )

    assert result.status is RunStatus.FAILED
    assert tuple(step.status for step in result.steps) == (
        StepStatus.SUCCEEDED,
        StepStatus.SUCCEEDED,
        StepStatus.FAILED,
        StepStatus.SKIPPED,
    )
    assert result.output_items == ()
    assert tuple(evidence.step for evidence in result.evidence) == (
        StepName.PREPARE,
        StepName.PREPARE,
        StepName.PROCESS,
        StepName.PROCESS,
    )
    assert tuple(event.event_type for event in result.events) == (
        EventType.STARTED,
        EventType.SUCCEEDED,
        EventType.STARTED,
        EventType.SUCCEEDED,
        EventType.STARTED,
        EventType.FAILED,
        EventType.SKIPPED,
    )


@pytest.mark.parametrize("fail_at", tuple(StepName))
def test_every_step_can_be_failed_deterministically(fail_at: StepName) -> None:
    result = run_automation(make_request(), policy=SimulationPolicy(fail_at=fail_at))
    failed_index = tuple(StepName).index(fail_at)

    assert result.status is RunStatus.FAILED
    assert result.steps[failed_index].status is StepStatus.FAILED
    assert all(
        step.status is StepStatus.SKIPPED
        for step in result.steps[failed_index + 1 :]
    )


def test_result_rejects_inconsistent_success_contract() -> None:
    request = make_request()
    valid = run_automation(request)

    with pytest.raises(ValueError, match="output_items"):
        AutomationResult(
            request=request,
            status=RunStatus.SUCCEEDED,
            steps=valid.steps,
            events=valid.events,
            output_items=("WRONG",),
        )


def test_result_rejects_non_contiguous_event_sequence() -> None:
    valid = run_automation(make_request())
    first = valid.events[0]
    invalid_first = AutomationEvent(
        sequence=2,
        step=first.step,
        event_type=first.event_type,
        message=first.message,
    )

    with pytest.raises(ValueError, match="contiguous"):
        AutomationResult(
            request=valid.request,
            status=valid.status,
            steps=valid.steps,
            events=(invalid_first, *valid.events[1:]),
            output_items=valid.output_items,
        )


def test_failed_or_skipped_steps_cannot_publish_evidence() -> None:
    valid = run_automation(make_request())
    evidence = valid.steps[0].evidence

    with pytest.raises(ValueError, match="cannot produce evidence"):
        StepResult(
            step=StepName.PREPARE,
            status=StepStatus.FAILED,
            message="failed",
            evidence=evidence,
        )


def test_runtime_type_contracts_are_explicit() -> None:
    with pytest.raises(TypeError, match="AutomationRequest"):
        run_automation("RUN-001")  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="SimulationPolicy"):
        run_automation(make_request(), policy="verify")  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="StepName"):
        SimulationPolicy(fail_at="verify")  # type: ignore[arg-type]


def test_text_report_is_stable_and_contains_no_memory_addresses() -> None:
    result = run_automation(
        make_request(),
        policy=SimulationPolicy(fail_at=StepName.VERIFY),
    )

    rendered = render_text_report(result)
    assert rendered == render_text_report(result)
    assert "Run status: failed" in rendered
    assert "006 verify failed: Simulated failure at verify." in rendered
    assert "007 finalize skipped: Skipped because an earlier step failed." in rendered
    assert "<not published>" in rendered
    assert "0x" not in rendered
