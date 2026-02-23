from fastapi import APIRouter
from app.schemas.task_schema import TaskAddSchema
from app.core.database import SessionDep, engine
from app.model.base_model import TaskModel, Base


router = APIRouter(prefix="/main_task", tags=["Main actions with tasks"])


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

@router.post("/setup_database")
async def create_db():
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@router.get('/')
def get_tasks():
    ...



@router.get('/{num_task}')
def get_special_task():
    ...




@router.delete('/{num_task}')
def delete_task():
    ...