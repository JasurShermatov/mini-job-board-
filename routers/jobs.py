from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from schemas.job import JobCreate, JobResponse
from services.job import JobService

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get(
    "",
    response_model=list[JobResponse],
    summary="Get all jobs",
    description="Returns all job listings sorted by newest first.",
    response_description="List of job listings",
)
async def get_jobs(db: AsyncSession = Depends(get_db)) -> list[JobResponse]:
    return await JobService.get_all_jobs(db)


@router.post(
    "",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new job",
    description="Creates a new job listing with validated payload fields.",
    response_description="Created job record",
    responses={500: {"description": "Database error while creating job"}},
)
async def create_job(job_in: JobCreate, db: AsyncSession = Depends(get_db)) -> JobResponse:
    try:
        return await JobService.create_job(db, job_in)
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create job",
        ) from exc
