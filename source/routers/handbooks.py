from fastapi import APIRouter, Body
from source.core import handbooks

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/")
async def get_people():
    return await handbooks.get_people()

@router.get("/{id}")
async def get_person(id: int):
    return await handbooks.get_person(id)

@router.post("/")
async def create_person(data = Body()):
    return await handbooks.create_person(data)

@router.put("/")
async def edit_person(data = Body()):
    return await handbooks.edit_person(data)

@router.delete("/{id}")
async def delete_person(id: int):
    return await handbooks.delete_person(id)