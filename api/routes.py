from fastapi import APIRouter, Depends
from api.auth import verify_token

router = APIRouter(
    prefix="",
    tags=["automation"]
)


@router.post("/run/csv-report", dependencies=[Depends(verify_token)])
def run_csv_report():
    """
    Example automation endpoint.
    In real usage, this will call the automation engine.
    """
    # Placeholder logic
    return {
        "status": "started",
        "message": "CSV report automation triggered"
    }


@router.get("/status/{job_id}", dependencies=[Depends(verify_token)])
def job_status(job_id: str):
    """
    Check status of a running or completed job.
    """
    return {
        "job_id": job_id,
        "status": "completed"
    }
