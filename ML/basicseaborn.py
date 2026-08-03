import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.rand(12)

sns.histplot(data, kde=True)

plt.show()