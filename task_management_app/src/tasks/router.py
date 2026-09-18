from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix="/tasks")

# https//127.0.0.1:8000/task/create_task

@task_routes.post("/create")
# def create_task():
#     return controller.create_task()

def create_task(body: TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)