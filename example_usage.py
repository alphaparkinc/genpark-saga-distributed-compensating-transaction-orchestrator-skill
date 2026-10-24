"""Example usage for Saga Compensating Orchestrator."""
from client import SagaCompensatingOrchestrator

if __name__ == "__main__":
    res = SagaCompensatingOrchestrator.execute_saga([
        {"name": "reserve_flight", "compensate_action": "cancel_flight"},
        {"name": "charge_card", "simulate_failure": True}
    ])
    print("Saga Status:", res["saga_status"], "Compensations:", res["compensations_executed"])
