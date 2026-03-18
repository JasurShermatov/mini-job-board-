from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config import settings
from core.database import Base, engine
from routers.jobs import router as jobs_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Mini Job Platform backend API. Use /jobs to list and create job posts.",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(jobs_router)
