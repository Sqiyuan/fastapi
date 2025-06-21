from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Kieran"}

# 路由上的路径参数
@app.get("/items/{item_id}")
async def read_item(item_id: str = Path(max_length=6, description='这是一个item_id'), q: Optional[str] = None):
    """
    测试路径参数
    :param item_id: id
    :param q: q
    :return: item_id, q
    """
    print("http://127.0.0.1:8000/docs")
    return {"item_id": item_id, "q": q}  
