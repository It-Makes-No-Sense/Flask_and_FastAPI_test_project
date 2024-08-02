import os.path
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from typing import List
import logging
from models import Task
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


def get_base_data():
    logger.info(os.getcwd())
    with open('base/base.json', 'r', encoding='utf-8') as file:
        data = file.read()
    return json.loads(data)


def save_to_base(j: json):
    with open('base/base.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(j))


@app.get("/", response_class=RedirectResponse, status_code=302)
async def root():
    return '/docs'


@app.get("/tasks")
async def tasks():
    logger.info('GET на все задачи.')
    return get_base_data()


@app.get("/tasks/{id}")
async def get_tasks(task_id: int):
    logger.info(f'GET на задачу с id: {task_id}')
    j = get_base_data()
    for item in j['tasks']:
        if item['task_id'] == task_id:
            return j['tasks'][task_id - 1]
    raise HTTPException(404, "Записи с таким id не существует.")


@app.post('/tasks')
async def add_tasks(task_list: List[Task]):
    logger.info('POST на добавление задачи')
    j = get_base_data()
    for task in task_list:
        j['tasks'].append(
            {
                "task_id": len(j['tasks']) + 1,
                "name": task.name,
                "description": task.description,
                "complete_status": task.complete_status
            }
        )
    save_to_base(j)
    return f"Добавлено(а) {len(task_list)} задач(а)"


@app.put("/tasks/{id}")
async def upd_task(task_id: int):
    logger.info(f'PUT на обновление статуса задачи: {task_id}')
    j = get_base_data()
    item = None
    for item in j['tasks']:
        if item['task_id'] == task_id:
            break
    if not item:
        raise HTTPException(404, "Записи с таким id не существует.")
    item['complete_status'] = not item['complete_status']
    save_to_base(j)
    return f'Статус задачи {item["name"]} c id {item["task_id"]} был обновлен.'


@app.delete("/tasks/{id}")
async def delete_task(task_id: int):
    logger.info(f'DELETE на задачу с id: {task_id}')
    j = get_base_data()
    item = None
    for item in j['tasks']:
        if item['task_id'] == task_id:
            j['tasks'].pop(j['tasks'].index(item))
    if not item:
        raise HTTPException(404, "Записи с таким id не существует.")
    save_to_base(j)
    return f'Задача {item["name"]} с id {item["tasks_id"]} была удалена.'
