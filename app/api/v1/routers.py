from fastapi import APIRouter, HTTPException

from app.model.responce_model import TaskResponse, AllTasksResponse
from app.schemas.task_schema import TaskAddSchema
from app.core.database import SessionDep, engine
from app.model.base_model import TaskModel, Base
from pathlib import Path
from sqlalchemy import select

router = APIRouter(prefix="/main_task", tags=["Main actions with tasks"])

@router.get('/tasks', response_model=list[AllTasksResponse])
async def get_tasks(session: SessionDep):
    result = await session.execute(
        select(TaskModel)
    )

    tasks = result.scalars().all()
    return tasks


@router.get('/{task_id}', response_model=TaskResponse)
async def get_special_task(task_id: int, session: SessionDep):
    task = await session.get(TaskModel, task_id)
    if task is not None:
        return task
    raise HTTPException(404, 'Task not found')


@router.post("/")
async def add_new_task(data: TaskAddSchema, session: SessionDep):
    new_task=TaskModel(
        title=data.title,
        description=data.description,
        deadline=data.deadline
    )

    session.add(new_task)
    await session.commit()
    return {'message': 'New task added'}


@router.delete('/{task_id}')
async def delete_task(task_id: int, session: SessionDep):
    task = await session.get(TaskModel, task_id)
    if task is not None:
        await session.delete(task)
        await session.commit()
        return {"message": "Task has been deleted"}

    raise HTTPException(404, 'Task not found')



@router.post("/setup_database")
async def create_db():
    db_path=Path('tasks.db')
    if not db_path.exists():
        async with engine.connect() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            return {"message": "Database has been created"}

    raise HTTPException(422, 'Database already in project')