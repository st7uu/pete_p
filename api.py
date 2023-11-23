from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from kobkunkub import get_img
app = FastAPI()
app.mount("/image", StaticFiles(directory="image"), name="image")

@app.get("/")
async def root():
    return get_img
