import gradio as gr
def greet(name): return f"Hello {name}!"
print("starting"i)
gr.Interface(fn=greet, inputs="text", outputs="text")
