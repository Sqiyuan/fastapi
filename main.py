from fastapi import FastAPI, Path, Cookie, Response
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel, field_validator, Field

app = FastAPI()

print("http://127.0.0.1:8000/docs")

class Item(BaseModel):
    name: str = Field(max_length=10, title="Name of the item", description="Name of the item")
    price: float
    is_offer: Optional[bool] = None

    @field_validator("name")
    @classmethod
    def name_val(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("name must be at least 3 characters long")
        if ' ' in value:
            raise ValueError("name must not contain spaces")
        return value

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
    return {"item_id": item_id, "q": q}  

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    """
    测试请求体参数
    :param item: item
    :return: item
    """
    print(f"item_id:{item_id}")
    print(f"item.name:{item.name}, item.price:{item.price}, item.is_offer:{item.is_offer}")
    return item

@app.get('/cookie/get')
async def get_cookie(username: str | None = Cookie()):
    """
    获取cookie
    :param 
    :return: cookie
    """
    print(f"username:{username}")
    return "success"

@app.get('/cookie/set')
async def set_cookie():
    """
    设置cookie
    :param response: response
    :return: cookie
    """
    response = JSONResponse(content={"message": "set cookie success"})
    response.set_cookie(key="username", value="Kieran")
    return response