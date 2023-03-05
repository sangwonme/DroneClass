import matplotlib.pyplot as plt
import numpy as np

y = []
for x in range(100):
    y.append(x*2 + 10)

y = np.array(y)

plt.plot(y)
plt.show()