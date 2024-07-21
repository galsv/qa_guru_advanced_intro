import random
import json
from datetime import datetime, UTC
from fastapi import FastAPI, Form, Request
from fastapi_server.data.schemas.user import UserListResponse
from fastapi_server.data.schemas.new_user import NewUser, NewUserResponse
from typing import Optional


app = FastAPI()


def get_data():
    with open('fastapi_server/data/users.json') as file_data:
        return json.load(file_data)


def response_user(name:str, job: str):
    return {
        "name": name,
        "job": job,
        "id": str(random.randint(100, 999)),
        "createdAt": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    }


@app.get("/api/users", response_model=UserListResponse)
def get_users(page: int = 1, per_page: int = 12):
    data = get_data()
    start = (page - 1) * per_page
    end = start + per_page
    response_data = {
        "page": page,
        "per_page": per_page,
        "total": len(data),
        "total_pages": len(data) // per_page,
        "data": data[start:end],
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    return response_data


@app.post("/api/users", response_model=NewUserResponse, status_code=201)
async def post_create_users(new_user: NewUser):
    return response_user(name=new_user.name, job=new_user.job)


@app.post("/api/user", response_model=NewUserResponse, status_code=201)
async def post_create_user(
    name: str = Form(...),
    job: str = Form(...),
):
    return response_user(name=name, job=job)
