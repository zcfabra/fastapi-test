

from typing import Union 
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    user_id: str
    text: str
    likes: int

class User(BaseModel):
    id: str
    name:str
    age: int




@app.get("/")
def root():
    return {"data": 90}





@app.post("/create")
def create_user(body:User,request:Request):
    print(request)
    b = body.dict()
    print(b)

    return b

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None]= None):
    # so the
    return {"item_id": item_id, "q": q}