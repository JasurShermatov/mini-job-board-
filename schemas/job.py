from pydantic import BaseModel, ConfigDict, Field


class JobBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=255)
    company: str = Field(min_length=1, max_length=255)
    salary: str | None = Field(default=None, max_length=100)
    description: str | None = None


class JobCreate(JobBase):
    pass


class JobResponse(JobBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
