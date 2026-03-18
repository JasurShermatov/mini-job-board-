from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from models.job import Job
from schemas.job import JobCreate


class JobService:
    @staticmethod
    async def get_all_jobs(db: AsyncSession) -> list[Job]:
        result = await db.execute(select(Job).order_by(Job.id.desc()))
        return list(result.scalars().all())

    @staticmethod
    async def create_job(db: AsyncSession, job_data: JobCreate) -> Job:
        job = Job(**job_data.model_dump())
        db.add(job)

        try:
            await db.commit()
        except SQLAlchemyError:
            await db.rollback()
            raise

        await db.refresh(job)
        return job
