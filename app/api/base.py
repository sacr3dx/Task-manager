from fastapi import APIRouter
from app.api.v1.routers import router as v1_endpoints

task_router=APIRouter()

task_router.include_router(v1_endpoints)