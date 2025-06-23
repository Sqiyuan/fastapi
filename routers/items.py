from fastapi import APIRouter, Header, Depends
from fastapi.exceptions import HTTPException


async def login_token(token: str = Header(...)):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return {"token": token}


router = APIRouter(
    prefix="/login",
    tags=["login"], 
    dependencies=[Depends(login_token)], 
    responses={404: {"description": "Not found"}}
    )


@router.get("/{login_id}")
async def read_item(login_id: str):
    """
    类依赖注入
    :param login_id: login_id
    :return: login_id
    """
    return {"login_id": login_id}
