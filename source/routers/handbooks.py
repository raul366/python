from fastapi import Depends,APIRouter, Body
from sqlalchemy.orm import Session

from source.core import handbooks

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/")
async def get_people(db: Session = Depends(handbooks.get_db)):
    return await handbooks.get_people(db)

@router.get("/{id}")
async def get_person(id, db: Session = Depends(handbooks.get_db)):
    return await handbooks.get_person(id, db)

@router.post("/")
async def create_person(data = Body(), db: Session = Depends(handbooks.get_db)):
    return await handbooks.create_person(data, db)

@router.put("/")
async def edit_person(data = Body(), db: Session = Depends(handbooks.get_db)):
    return await handbooks.edit_person(data, db)

@router.delete("/{id}")
async def delete_person(id, db: Session = Depends(handbooks.get_db)):
    return await handbooks.delete_person(id, db)