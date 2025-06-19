from fastapi import FastAPI
from ui.interface import demo

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Job Assistant"}


@app.get("/ping")
def ping():
    return {"status": "ok"}


