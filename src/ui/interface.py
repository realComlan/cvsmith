import gradio as gr
from app.recommender import recommend


with gr.Blocks() as demo:
    gr.Markdown("# 🔍 Job CV Assistant")
    inp = gr.Textbox(label="What is the CV content?")
    out = gr.Textbox(label="Assistant says:")
    btn = gr.Button("Ask")
    btn.click(fn=recommend, inputs=inp, outputs=out)

demo.launch()
