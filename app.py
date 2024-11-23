#!/usr/bin/env python

# ## Is it a cat?

# In[ ]:

import gradio as gr
#|export
from fastai.vision.all import *


def is_cat(x):
	return x[0].isupper()


# In[ ]:

#|export
learn = load_learner("model.pkl")

# In[ ]:

im = PILImage.create("cat.jpg")
im.thumbnail((200, 200))
#im = im.resize((192,192))

type(im)

# In[ ]:

learn.predict(im)

# In[ ]:

#|export
categories = ["dog", "cat"]


def classify_image(img):
	#img = img.resize((192,192))
	pred, idx, probs = learn.predict(img)
	return dict(zip(categories, map(float, probs)))


# In[ ]:

classify_image(im)

# In[ ]:

#|export
image = gr.Image()
label = gr.Label()
examples = ["dog.jpg", "forest.jpg", "cat.jpg"]
demo = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
demo.launch()
