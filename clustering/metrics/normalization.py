import numpy as np

def normalize_std(x):
    """Return the input normalized by its standard deviation, with mean zero"""
    return (x-np.nanmean(x))/np.nanstd(x)


def normalize_max(x):
    """Return the input normalized by its maximum value with mean zero"""
    return (x-np.nanmean(x))/np.nanmax(x)
