import gradio as gr
def greet(name): return f"Hello {name}!"
print("starting")
gr.Interface(fn=greet, inputs="text", outputs="text")
