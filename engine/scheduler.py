from apscheduler.schedulers.background import BackgroundScheduler
from engine.runner import run_task
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()


def start_scheduler():
    if not scheduler.running:
        scheduler.start()
        logger.info("Scheduler started")


def schedule_task(payload: dict, interval_minutes: int = 60):
    """
    Schedule a recurring automation task.
    """

    job = scheduler.add_job(
        run_task,
        "interval",
        minutes=interval_minutes,
        args=[payload],
        replace_existing=True
    )

    logger.info(
        f"Scheduled task '{payload.get('task')}' "
        f"every {interval_minutes} minutes"
    )

    return {
        "job_id": job.id,
        "interval_minutes": interval_minutes,
        "status": "scheduled"
    }
