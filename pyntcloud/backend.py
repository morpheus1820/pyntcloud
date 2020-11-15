import os
import numpy 
import pandas


DATAFRAME_BACKENDS = {"CPU": pandas}
ARRAY_BACKENDS = {"CPU": numpy}

try:
    import cudf
    DATAFRAME_BACKENDS["GPU"] = cudf
    import cupy
    ARRAY_BACKENDS["GPU"] = cupy 
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

DATAFRAME_BACKEND = DATAFRAME_BACKENDS[os.environ.get("PYNTCLOUD_BACKEND")]
if DATAFRAME_BACKEND is None:
    raise ImportError(
        f"{missing_package} is required for {os.environ.get("PYNTCLOUD_BACKEND")}")

ARRAY_BACKEND = ARRAY_BACKENDS[os.environ.get("PYNTCLOUD_BACKEND").split("MULTI-")[-1]]