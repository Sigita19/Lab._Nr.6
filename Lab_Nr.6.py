#!/usr/bin/env python
# coding: utf-8

# <h1>Lab. Nr. 6 <h1>
# 

# <h4> Sigita Stanevičiūtė <h4>

# In[17]:



import plotly.express as px
import pandas as pd

df = pd.read_csv('PS4_GamesSales1.csv', encoding="ISO-8859-1")
df.head()


# In[25]:


fig = px.treemap(data_frame=df, path=['Genre'], values='Global', color='Global', color_continuous_scale='rdbu')
fig.show()


# In[3]:


import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

d=df[['Europe', 'Japan', 'North America','Genre']]
plt.figure()

parallel_coordinates(d,'Genre')
plt.legend(bbox_to_anchor=(1.5,1), loc="upper left")
plt.show()


# In[147]:


import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from pandas.plotting import andrews_curves

d=df[['Europe', 'Japan', 'North America','Genre']]

andrews_curves(d,'Genre')
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
plt.figure()
plt.show()


# In[ ]:




