import xarray as xr
import numpy as np

for i in range(3):
    data = xr.DataArray(np.random.normal(0,1,(100))) # Generate some data
    data = data.expand_dims('dim1').assign_coords({'dim1':np.array((i,))}) # Make it so it can combine by coords easily
    data.to_netcdf(str(i)+'.nc')