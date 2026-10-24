"""MCP server for Saga Compensating Orchestrator."""
import sys
import json
from client import SagaCompensatingOrchestrator

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "orchestrate_saga_transaction",
                "description": "Executes multi-step saga workflow and triggers reverse compensations on failure",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "steps": {"type": "array"}
                    },
                    "required": ["steps"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "orchestrate_saga_transaction":
            steps = params.get("arguments", {}).get("steps", [])
            res = SagaCompensatingOrchestrator.execute_saga(steps)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
