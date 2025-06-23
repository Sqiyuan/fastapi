<<<<<<< HEAD
from ctypes import sizeof
from fastapi import Depends, FastAPI, Header, Path, Cookie, Response
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel, field_validator, Field

from routers import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
=======
from fastapi import FastAPI, Path, Cookie, Response
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel, field_validator, Field

app = FastAPI()

print("http://127.0.0.1:8000/docs")
>>>>>>> 18335e1dff5df06e8d714775d3f94cf633900f6e

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
<<<<<<< HEAD
    return response

@app.get('/header')
async def get_header(
    user_agent: str | None = Header(default=None),
    host: str | None = Header(default=None),
    ):
    """
    获取header
    :param user_agent: user_agent
    :return: header
    """
    print(f"user_agent:{user_agent}")
    print(f"host:{host}")
    return "success"


####################函数依赖注入####################
async def list_common(page: int = 1, size: int = 10, q: str | None = None):
    """
    函数依赖注入
    :param page: page
    :param size: size
    :param q: q
    :return: list
    """
    return {'page': page, 'size': size, 'q': q}

@app.get('/list')
async def list_get(list_common: dict = Depends(list_common)):
    """
    函数依赖注入
    :param list_common: list_common
    :return: list
    """
    print(f"page:{list_common['page']}, size:{list_common['size']}, q:{list_common['q']}")
    return list_common
####################函数依赖注入####################


####################类依赖注入####################
class CommonQueryParams:
    def __init__(self, page: int = 1, size: int = 10, q: str | None = None):
        self.page = page
        self.size = size
        self.q = q

    def get_q_len(self):
        return {'q_len': len(self.q) if self.q is not None else 0}

@app.get('/class_list')
async def class_list(class_list = Depends(CommonQueryParams)):
    """
    类依赖注入
    :param class_list: class_list
    :return: list
    """
    print(f"page:{class_list.page}, size:{class_list.size}, q:{class_list.get_q_len()}")
    return "success"

####################类依赖注入####################
=======
    return response
>>>>>>> 18335e1dff5df06e8d714775d3f94cf633900f6e
