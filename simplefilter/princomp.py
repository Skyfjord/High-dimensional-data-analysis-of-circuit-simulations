import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import decomposition

from pca import pca


def analysis(dim,data,label,target):

    X = pd.DataFrame(data=data, columns=label, index=target) # Creating pandas Dataframe

    model = pca(n_components=dim)

    results = model.fit_transform(X,verbose=0)

    dec = decomposition.PCA(n_components=dim)
    X = dec.fit_transform(X)
    loadings = pd.DataFrame(dec.components_.T, columns=[f'PC{i+1}' for i in range(dim)], index=label)

    return loadings,model



# fig, ax = model.plot()
# plt.show()

# # 2D plot
# fig, ax = model.scatter()

# plt.show()

# # 3d Plot
# fig, ax = model.scatter3d()

# plt.show()

# plt.rcParams['figure.figsize'] = [8, 8]
# radviz.to2d(5,dataset2.data,color="green",dimlabel=label,alpha=0.2)
# radviz.to2d(5,dataset2.dataP,color="red",dimlabel=label,alpha=0.2)
# plt.show()