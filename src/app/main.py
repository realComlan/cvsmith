import gradio as gr
from fastapi import FastAPI
from app.recommender import recommend

app = FastAPI()

gradio_ui = gr.Interface(
    fn=recommend, inputs="text", outputs="text", title="Crypto Assistant"
)
app = gr.mount_gradio_app(app, gradio_ui, path="/")


@app.get("/")
def index():
    """
    Index method.
    """
    return {"text": "Welcome"}


@app.get("/ping")
def ping():
    """
    Ping method.
    """
    return {"status": "ok"}
