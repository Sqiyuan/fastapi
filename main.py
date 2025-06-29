from fastapi import FastAPI

app = FastAPI()

DB_URL = 'mysql+asyncmy://root:123123@127.0.0.1:3306/fastapi?charset=utf8mb4'

@app.get("/")
def read_root():
    return {"Hello": "World"}
