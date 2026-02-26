from pydantic import BaseModel


class AllTasksResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes=True


class TaskResponse(AllTasksResponse):
    description: str
    deadline: int