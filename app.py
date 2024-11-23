import gradio as gr
def greet(name): return f"Hello {name}!"
print("starting")
try:
    gr.Interface(fn=greet, inputs="text", outputs="text")
except Exception as ex:
    print ("ex:" + str(ex))
print ("after")
