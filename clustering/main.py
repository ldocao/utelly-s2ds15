import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from common import Event, Collection, Cluster

    
event_a = Event(name="a",value=1)
event_b = Event(name="b",value=1)
event_c = Event(name="c",other=True)
col = Collection()
clu = Cluster([event_a,event_b,event_c],keywords="name")

col.add([event_a,event_b,event_c])

