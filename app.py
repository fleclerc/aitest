import gradio as gr
def greet(name): return f"Hello {name}!"
print("starting")
try:
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    demo.launch()
except Exception as ex:
    print ("ex:" + str(ex))
print ("after")
