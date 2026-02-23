from pydantic import BaseModel, Field


class TaskAddSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=30, description='Name of the task')
    description: str = Field(None, min_length=1, max_length=100, description='Description of the task')
    deadline: int = Field(None, description='Days before the deadline')

class TaskSchema(TaskAddSchema):
    id: str