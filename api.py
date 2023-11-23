from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/image", StaticFiles(directory="image"), name="image")

@app.get("/")
async def root():
    return {"message": "Hello World"}
