import problem
import xarray as xr

from dask.distributed import Client

if __name__ == '__main__':
    client = Client(threads_per_worker=1)
    
    filenames = ['0.nc','1.nc']

    xr.open_mfdataset(filenames,
                      parallel = True,
                     )