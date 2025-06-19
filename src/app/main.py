from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    """
    Index method.
    """
    return {"message": "Welcome to AI Job Assistant"}


@app.get("/ping")
def ping():
    """
    Ping method.
    """
    return {"status": "ok"}
