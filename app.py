#!/usr/bin/env python

# ## Is it a cat?

# In[ ]:

#|export

# Make sure we've got the latest version of fastai:
get_ipython().system("pip install -Uqq fastai")

import gradio as gr
from fastai.vision.all import *


def is_cat(x):
	return x[0].isupper()


# In[2]:

#|export
learn = load_learner("model.pkl")

# In[3]:

im = PILImage.create("cat.jpg")
im.thumbnail((200, 200))
#im = im.resize((192,192))

type(im)

# In[4]:

learn.predict(im)

# In[5]:

#|export
categories = ["dog", "cat"]


def classify_image(img):
	#img = img.resize((192,192))
	pred, idx, probs = learn.predict(img)
	return dict(zip(categories, map(float, probs)))


# In[6]:

classify_image(im)

# In[7]:

#|export
image = gr.Image()
label = gr.Label()
examples = ["dog.jpg", "forest.jpg", "cat.jpg"]
demo = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
demo.launch()

# In[9]:

import notebook2script

notebook2script.convert_notebook("predict.ipynb", "app.py")
