from pymoo.visualization.pcp import PCP
import dataset as dataset
import numpy as np
import matplotlib.pyplot as plt


plot = PCP()
plot.set_axis_style(color="grey", alpha=0.5)
plot.axis_labels=dataset.dim_names
plot.add(np.array(dataset.dataN), color="green", alpha=0)
plot.add(np.array(dataset.dataP), color="green", alpha=0.1)
plot.show()