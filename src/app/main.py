from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from gradio.routes import mount_gradio_app
from app.recommender import recommend
import gradio as gr

app = FastAPI()

gradio_ui = gr.Interface(
    fn=recommend, inputs="text", outputs="text", title="Crypto Assistant"
)
app = mount_gradio_app(app, gradio_ui, path="/ui")


@app.get("/")
def index():
    """
    Index method.
    """
    return RedirectResponse(url="/ui")


@app.get("/ping")
def ping():
    """
    Ping method.
    """
    return {"status": "ok"}
