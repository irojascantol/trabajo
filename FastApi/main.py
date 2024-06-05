from fastapi import FastAPI


import uvicorn
from app.routers import user, item
 
app = FastAPI()

app.include_router(item.router)
app.include_router(user.router)



#run server with: python -m uvicorn main:app --reload


# def run_api():
#     uvicorn.run(app, host="127.0.0.1", port=8000)

# if __name__=="__main__":
#     run_api()