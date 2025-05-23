from fastapi import FastAPI
from fastapi.responses import FileResponse

from source.db.database import *
from source.routers import handbooks

# создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(handbooks.router)

@app.get("/")
async def main():
    return FileResponse("source/public/index.html")