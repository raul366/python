from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, HTMLResponse, JSONResponse
 
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