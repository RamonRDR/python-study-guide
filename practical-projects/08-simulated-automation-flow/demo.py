"""Deterministic demo for Project 08: Simulated Automation Flow."""

from automation_flow import (
    AutomationRequest,
    SimulationPolicy,
    StepName,
    render_text_report,
    run_automation,
)


def main() -> None:
    request = AutomationRequest(
        request_id="DEMO-001",
        items=("alpha", "beta", "gamma"),
    )

    print("=== Successful run ===")
    print(render_text_report(run_automation(request)), end="")

    print("\n=== Controlled failure ===")
    failed = run_automation(
        request,
        policy=SimulationPolicy(fail_at=StepName.VERIFY),
    )
    print(render_text_report(failed), end="")


if __name__ == "__main__":
    main()
