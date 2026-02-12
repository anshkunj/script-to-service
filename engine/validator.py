from typing import Dict
from fastapi import HTTPException, status


def validate_payload(payload: Dict):
    """
    Validate incoming automation payload.
    Keeps services predictable and safe.
    """

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Payload cannot be empty"
        )

    if "task" not in payload:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Missing required field: task"
        )

    if not isinstance(payload["task"], str):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Field 'task' must be a string"
        )

    return True
