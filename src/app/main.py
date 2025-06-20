import gradio as gr
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.recommender import recommend

app = FastAPI()

gradio_ui = gr.Interface(
    fn=recommend, inputs="text", outputs="text", title="Crypto Assistant"
)
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
