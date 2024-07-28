from http import HTTPStatus

from fastapi import FastAPI

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
    user_with_id = UserDB(id=pk, **user.model_dump())
    database[pk - 1] = user_with_id
    return user_with_id
