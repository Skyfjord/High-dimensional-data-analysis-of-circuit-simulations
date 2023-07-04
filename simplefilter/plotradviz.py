import matplotlib.pyplot as plt
import numpy as np
import dataset3 as dataset
import radviz

alpha=0.2
size=20
plt.rcParams['figure.figsize'] = [8, 8]

radviz.to2d(dataset.dim,dataset.dataN,color="red",dimlabel=dataset.dim_names,alpha=alpha,marker='o',s=size,label='Fail')
radviz.to2d(dataset.dim,dataset.dataP,color="green",dimlabel=dataset.dim_names,alpha=alpha,marker='o',s=size,label='Pass')
plt.legend()
plt.show()