from sqlalchemy.orm import Session
from fastapi import Depends, Body, status
from fastapi.responses import JSONResponse

from source.db.database import *

# определяем зависимость
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()

async def get_person(id: int, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person==None:  
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    #если пользователь найден, отправляем его
    return person

async def create_person(data = Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], age=data["age"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person

async def edit_person(data = Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None: 
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    db.commit() # сохраняем изменения 
    db.refresh(person)
    return person

async def delete_person(id: int, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
   
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse( status_code=404, content={ "message": "Пользователь не найден"})
   
    # если пользователь найден, удаляем его
    db.delete(person)  # удаляем объект
    db.commit()     # сохраняем изменения
    return person