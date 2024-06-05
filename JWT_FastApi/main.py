import uvicorn
import requests
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
app = FastAPI()

users = []
posts = []


#add new post
@app.get("/posts", tags=["posts"])
def get_post():
    if len(posts):
        return {
            "data": posts
        }
    else:
        return {
        "info": "Nothing to show you!"
        }  

#add new post
@app.post("/posts", dependencies = [Depends(jwtBearer())], tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post Added!"
    }  


#create a new user
@app.post("/user/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


#login a registered user
@app.post("/user/login", tags=["user"])
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details!"
        }

#temporary post
@app.get("/product/{pattern}", tags=["posts"])
def add_post(pattern):
    results = requests.get(f'https://nodejs-mysql-restapi-production-5162.up.railway.app/api/products/{pattern}')
    return {
        "value returned": results.json()
    }


# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}