import xarray as xr

xr.load_dataarray('0.nc')

from dask.distributed import Client

if __name__ == '__main__':
    
    client = Client(threads_per_worker=1)
    
    xr.open_mfdataset(('1.nc','2.nc'),
                      parallel = True,
                     )
