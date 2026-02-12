import logging
from datetime import datetime
from engine.validator import validate_payload

logger = logging.getLogger(__name__)


def run_task(payload: dict) -> dict:
    """
    Core execution function.
    This is where scripts become services.
    """

    validate_payload(payload)

    task_name = payload["task"]
    start_time = datetime.utcnow()

    logger.info(f"Starting task: {task_name}")

    # ---- placeholder for real automation logic ----
    # Example:
    # result = process_csv(payload)
    result = {
        "message": f"Task '{task_name}' executed successfully"
    }
    # ------------------------------------------------

    end_time = datetime.utcnow()

    logger.info(
        f"Task completed: {task_name} | "
        f"Duration: {(end_time - start_time).seconds}s"
    )

    return {
        "task": task_name,
        "status": "completed",
        "started_at": start_time.isoformat(),
        "finished_at": end_time.isoformat(),
        "result": result
    }
