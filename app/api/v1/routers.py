from fastapi import APIRouter, HTTPException

from app.database.database import task_db


router = APIRouter(prefix="/main_task", tags=["Main actions with tasks"])


@router.get('/')
def get_tasks():
    return task_db.items()


@router.get('/{num_task}')
def get_special_task(num_task: int):
    if num_task in task_db:
        return task_db[num_task]
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/")
def add_new_task(task: str):
    num= max(task_db.keys()) + 1
    task_db[num] = task
    return {"message: Task added"}


@router.delete('/{num_task}')
def delete_task(num_task: int):
    if num_task not in task_db:
        raise HTTPException(status_code=404, detail="Task not found")

    del task_db[num_task]
    return {'message': 'Task deleted'}