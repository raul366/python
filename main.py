from fastapi import FastAPI, Response, Path, Query, status, Body
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse, RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

class Company(BaseModel):
    name: str
 
class Person(BaseModel):
    name: str
    company: Company

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.get("/root")
def root():
    data = "Hello METANIT.COM"
    return Response(content=data, media_type="text/plain")
 
@app.get("/about")
def about():
    return {"message": "О сайте"}

@app.get("/text", response_class = PlainTextResponse)
def root_text():
    return "Hello METANIT.COM"
 
@app.get("/html", response_class = HTMLResponse)
def root_html():
    return "<h2>Hello METANIT.COM</h2>"

@app.get("/file")
def root_file():
    return FileResponse("public/index.html", 
                        filename="mainpage.html", 
                        media_type="application/octet-stream")

@app.get("/users/admin")
def admin():
    return {"message": "Hello admin"}
 
@app.get("/users")
def get_model(name: str = "Undefined", age: int = 18):
    return {"user_name": name, "user_age": age}
 
@app.get("/users/{name}")
def users(name:str  = Path(min_length=3, max_length=20)):
    return {"name": name}

@app.get("/user")
def users(people: list[str]  = Query()):
    return {"people": people}

@app.get("/user/{name}")
def users(name:str  = Path(min_length=3, max_length=20), 
            age: int = Query(ge=18, lt=111)):
    return {"name": name, "age": age}

@app.get("/notfound", status_code=status.HTTP_404_NOT_FOUND)
def notfound():
    return  {"message": "Resource Not Found"}

@app.get("/user1/{id}", status_code=200)
def users(response: Response, id: int = Path()):
    if id < 1:
        response.status_code = 400
        return {"message": "Incorrect Data"}
    return  {"message": f"Id = {id}"}

@app.get("/old")
def old():
    return RedirectResponse("/new", status_code=302)
 
@app.get("/new")
def new():
    return PlainTextResponse("Новая страница")

app.mount("/static", StaticFiles(directory="public"))

@app.post("/hello")
def hello(person: Person):
    return {"message": f"{person.name} ({person.company.name})"}