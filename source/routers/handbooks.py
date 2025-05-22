from fastapi import Body
from source import handbooks
from main import app

@app.get("/api/users")
def get_people():
    return handbooks.get_people()

@app.get("/api/users/{id}")
def get_person(id):
    return handbooks.get_person(id)

@app.post("/api/users")
def create_person(data  = Body()):
    return handbooks.create_person(data  = Body())

@app.put("/api/users")
def edit_person(data  = Body()):
    return handbooks.edit_person(data  = Body())

@app.delete("/api/users/{id}")
def delete_person(id):
    return handbooks.delete_person(id)