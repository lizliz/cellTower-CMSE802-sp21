
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
from random import randint

def mapplot(locations, colors):
    xs = locations[:,0]
    ys = locations[:,1]
    X = xs
    Y = ys
    labels = range(1,len(X)+1)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for x,y,lab in zip(X,Y,labels):
            ax.scatter(x,y,label=lab)

    colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired  
    colorst = [colormap(i) for i in np.linspace(0, 0.9,len(ax.collections))]       
    for t,j1 in enumerate(ax.collections):
        j1.set_color(colorst[t])
    ax.legend(fontsize='small')

