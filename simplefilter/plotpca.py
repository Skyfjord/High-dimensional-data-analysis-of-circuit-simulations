import numpy as np
import pandas as pd
import dataset3 as dataset
import matplotlib.pyplot as plt
from sklearn import decomposition

import radviz

# Load pca
from pca import pca

dim = 5

# Load dataset
label = dataset.dim_names
y = dataset.targetP #number of datapoints

X = pd.DataFrame(data=dataset.dataP, columns=label, index=y)

# Initialize to reduce the data up to the nubmer of componentes that explains 95% of the variance.
# model = pca(n_components=0.95)

# Reduce the data towards 3 PCs
model = pca(n_components=5)

# Fit transform
results = model.fit_transform(X,verbose=0)

dec = decomposition.PCA(n_components=dim)
X = dec.fit_transform(X)
loadings = pd.DataFrame(dec.components_.T, columns=[f'PC{i+1}' for i in range(dim)], index=label)



fig, ax = model.plot()
plt.show()

# 2D plot
fig, ax = model.scatter()

plt.show()

# 3d Plot
fig, ax = model.scatter3d()

plt.show()

# plt.rcParams['figure.figsize'] = [8, 8]
# radviz.to2d(5,dataset2.data,color="green",dimlabel=label,alpha=0.2)
# radviz.to2d(5,dataset2.dataP,color="red",dimlabel=label,alpha=0.2)
# plt.show()