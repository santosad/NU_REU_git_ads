#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

def plot_freaking_sine_boi():
    '''
    This is very sine-tific
    '''
    
    x_div = 50.0
    x_step = 2 * np.pi / x_div
    x = 0
    xs = []
    ys = []
    
    while x < 2 * np.pi:
        xs.append(x)
        ys.append(np.cos(x))
        x += x_step
    
    plt.plot(xs, ys, 'green')
    plt.show()

plot_freaking_sine_boi()

