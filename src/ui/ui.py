import gradio as gr

from app.recommender import recommend


def ui():
    gradio_ui = gr.Interface(
        fn=recommend, inputs="text", outputs="text", title="Crypto Assistant"
    )
    return gradio_ui
