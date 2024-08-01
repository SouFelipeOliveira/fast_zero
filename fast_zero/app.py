from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get("/", response_model=Message, status_code=HTTPStatus.OK)
def read_root():
    return {"message": "Hello World"}


@app.post("/users/", response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get("/users/", response_model=UserList)
def read_users():
    return {"user": database}


@app.put("/users/{id}/", response_model=UserPublic)
def update_users(pk: int, user: UserSchema):
    if pk < 1 or pk > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    user_with_id = UserDB(id=pk, **user.model_dump())
    database[pk - 1] = user_with_id
    return user_with_id


@app.get("/HelloWorldHtml/", response_class=HTMLResponse)
def hello_world_html():
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """
