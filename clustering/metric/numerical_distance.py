###PURPOSE: compute the distance for numerical variables
import numpy as np
from itertools import compress
import pdb
from utils import is_type


def _euclidean(event_a, event_b):
    """Return the euclidean distance between two points

    Parameters:
    ----------
    event_a, event_b: Event
        Event point

    Output:
    ------
    result: Distance()
    """

    ##some shortcuts
    values_a = event_a.__dict__.values()
    values_b = event_b.__dict__.values()

    ##check if attributes are float to compute euclidean distance
    which_a_attribute_float = is_type(values_a, np.float)
    which_b_attribute_float = is_type(values_b, np.float)
    if which_a_attribute_float == which_b_attribute_float:
        x = np.array(list(compress(values_a, which_a_attribute_float)))
        y = np.array(list(compress(values_b, which_b_attribute_float)))

        return np.linalg.norm(x-y)




