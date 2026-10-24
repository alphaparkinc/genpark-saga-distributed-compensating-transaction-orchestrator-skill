"""Saga Distributed Compensating Transaction Orchestrator.
100% Python Standard Library.
"""

class SagaCompensatingOrchestrator:
    """Coordinates multi-step distributed agent actions and executes reverse compensations upon failure."""

    @staticmethod
    def execute_saga(steps: list) -> dict:
        executed = []
        compensations_triggered = []
        saga_status = "COMPLETED"

        for st in steps:
            name = st.get("name")
            should_fail = bool(st.get("simulate_failure", False))
            comp_action = st.get("compensate_action")

            if should_fail:
                saga_status = "FAILED_ROLLED_BACK"
                for executed_step in reversed(executed):
                    if executed_step.get("compensate_action"):
                        compensations_triggered.append(executed_step["compensate_action"])
                break
            else:
                executed.append({"name": name, "compensate_action": comp_action})

        return {
            "saga_status": saga_status,
            "successful_steps_count": len(executed),
            "compensations_executed": compensations_triggered
        }
