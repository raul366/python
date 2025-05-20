from fastapi import FastAPI, Response, Path, Query
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
 
app = FastAPI()
 
@app.get("/")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)

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