import matplotlib.cm as cm 
import numpy as np
import matplotlib.pyplot as plt

MAX = 10

col = cm.rainbow(np.linspace(0, 1, MAX))
for i in range(MAX):
  a = []
  for j in range(0, MAX):
    a.append(i)
  
  plt.plot(np.array( list(range(0, MAX)) ), np.array( a ), 'r-', lw=20, color = col[i])
plt.show()