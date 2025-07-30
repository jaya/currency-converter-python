from fastapi import FastAPI

from validators import Convert

app = FastAPI()


@app.post("/convert/")
async def convert(data: Convert):
    return {}
