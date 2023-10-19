import numpy as np
import pandas as pd
import lingam

# To run causal discovery, we create a DirectLiNGAM object and call the fit method.
model = lingam.DirectLiNGAM()
model2 = lingam.ICALiNGAM()
model.fit(X)

# Using the causal_order_ properties, 
# we can see the causal ordering as a result of the causal discovery.
print(model.causal_order_)

# Also, using the adjacency_matrix_ properties, 
# we can see the adjacency matrix as a result of the causal discovery.
print(model.adjacency_matrix_)