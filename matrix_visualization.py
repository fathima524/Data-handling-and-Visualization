# -*- coding: utf-8 -*-
"""Matrix_visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EKUhtkB3KGyvDbyZW-Qm1rwewwr3aLYN
"""

import numpy as np
import matplotlib.pyplot as plt
data=np.random.random((13,6))
plt.imshow(data,cmap="plasma")
plt.title("2-D Heat Map")
plt.colorbar()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.randint(low=14,high=100,size=(10,10))
hm=sns.heatmap(data=data,annot=True)
plt.show()



import pandas as pd
import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'], values='total_bill', color='day')
fig.update_layout(margin=dict(t=50,l=25, r=25, b=25))
fig.show()