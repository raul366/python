from fastapi import FastAPI
from fastapi.responses import FileResponse

from source.routers import handbooks

app = FastAPI()

app.include_router(handbooks.router)

@app.get("/")
async def main():
    return FileResponse("source/public/index.html")