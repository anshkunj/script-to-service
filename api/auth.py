import os
from fastapi import Header, HTTPException, status

SERVICE_TOKEN = os.getenv("SERVICE_TOKEN")


def verify_token(x_service_token: str = Header(...)):
    """
    Very lightweight token-based auth.
    Suitable for internal services and automation APIs.
    """
    if SERVICE_TOKEN is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="SERVICE_TOKEN not configured"
        )

    if x_service_token != SERVICE_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid service token"
        )
