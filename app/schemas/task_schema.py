from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    tittle: str = Field(..., min_length=1, max_length=30, description='Name of the task')
    description: str = Field(..., min_length=1, max_length=100, description='Description of the task')
    deadline: int = Field(..., min_length=1, description='Days before the deadline')