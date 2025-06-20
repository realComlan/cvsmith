import gradio as gr
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from ui.ui import ui


app = FastAPI()

gradio_ui = ui()
app = gr.mount_gradio_app(app, gradio_ui, path="/ui")


@app.get("/")
def home():
    """
    Index page
    """
    return RedirectResponse(status_code=302, url="/ui")


@app.get("/ping")
def ping():
    """
    Ping method.
    """
    return {"status": "ok"}
