import dataset as dataset
import numpy as np
import matplotlib.pyplot as plt

alpha=0.8
bins=dataset.sampleno/20
tickfreq=20

for i in range(dataset.dim-1,-1,-1):
    plt.subplot(dataset.dim,1,i+1)
    plt.ylabel(dataset.dim_names[i])
    plt.xticks([i/tickfreq for i in range(tickfreq)])
    plt.hist(np.array(dataset.dataN)[:,i],bins=bins,alpha=alpha,color="red",range=(0,1))
    plt.hist(np.array(dataset.dataP)[:,i],bins=bins,alpha=alpha,color="green",range=(0,1))
    
plt.show()
