xr.open_mfdataset with parallel = True seems to struggle if xarray has already been used to read a file before the dask client is started
script.py shows an example of this error.
Weirdly, equivalent code in a jupyter notebook works fine

0.nc, 1.nc and 2.nc contain 100 random floats, and were created with setup.py
