import os
import pandas as pd


DATAFRAME_BACKENDS = {"CPU": pd}

try:
    import cudf   
    DATAFRAME_BACKENDS["GPU"] = cudf
except ImportError:
    DATAFRAME_BACKENDS["GPU"] = None
    missing_package = "cudf (https://github.com/rapidsai/cudf)"
try:
    import dask
    DATAFRAME_BACKENDS["MULTI-CPU"] = dask
except ImportError:
    DATAFRAME_BACKENDS["MULTI-CPU"] = None
    missing_package = "dask (https://github.com/dask/dask)"
try:
    import dask_cudf
    DATAFRAME_BACKENDS["MULTI-GPU"] = dask_cudf
except ImportError:
    DATAFRAME_BACKENDS["MULTI-GPU"] = None
    missing_package = "dask_cudf (https://github.com/rapidsai/cudf/tree/main/python/dask_cudf)"

BACKEND = DATAFRAME_BACKENDS[os.environ.get("PYNTCLOUD_BACKEND")]

if BACKEND is None:
    raise ImportError(
        f"{missing_package} is required for {os.environ.get("PYNTCLOUD_BACKEND")}")
