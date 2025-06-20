from fastapi import FastAPI

app = FastAPI()

# gradio_ui = gr.Interface(
#     fn=recommend, inputs="text", outputs="text", title="Crypto Assistant"
# )
# app = mount_gradio_app(app, gradio_ui, path="/ui")


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
