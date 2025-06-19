import gradio as gr


def job_recommendation_interface(cv_text):
    """
    Mock function
    """
    return f"🧠 Suggested job for: {cv_text[:50]}... => Not for you!"


demo = gr.Interface(
    fn=job_recommendation_interface, inputs="textbox", outputs="textbox"
)

if __name__ == "__main__":
    demo.launch()
