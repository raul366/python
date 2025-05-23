from source.public.people import people
from fastapi import Body, status
from fastapi.responses import JSONResponse
from source.scheme.handbooks import Person

async def find_person(id: str):
   for person in people: 
        if person.id == id:
           return person
   return None

async def get_people():
    return [person.dict() for person in people]

async def get_person(id: str):
    # получаем пользователя по id
    person = await find_person(id)
    print(person)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person==None:  
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    #если пользователь найден, отправляем его
    return person.dict()

async def create_person(data  = Body()):
    person = Person(data["name"], data["age"])
    # добавляем объект в список people
    people.append(person)
    return person.dict()

async def edit_person(data  = Body()):
    # получаем пользователя по id
    person = await find_person(data["id"])
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None: 
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    return person.dict()

async def delete_person(id: str):
    # получаем пользователя по id
    person = await find_person(id)
  
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
  
    # если пользователь найден, удаляем его
    people.remove(person)
    return person.dict()