from fastapi import FastAPI
from gradio.routes import mount_gradio_app
from app.recommender import recommend
import gradio as gr

app = FastAPI()

gradio_ui = gr.Interface(
    fn=recommend, inputs="text", outputs="text", title="Crypto Assistant"
)
app = mount_gradio_app(app, gradio_ui, path="/")


@app.get("/ping")
def ping():
    """
    Ping method.
    """
    return {"status": "ok"}
