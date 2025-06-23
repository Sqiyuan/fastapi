from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"], responses={404: {"description": "Not found users"}})

@router.get("/{username}")
async def read_item(username: str):
    return {"username": username}