import numpy as np
import pandas as pd
from common import Event, Distance, Metric
import metric.numerical_distance as numdist

event_a = Event(duration=1., rating=2.)
event_b = Event(duration=2., rating=3.)
metric_euclidean = Metric("euclidean", numdist._euclidean)
dist_a_b = Distance(event_a, event_b, metric_euclidean)


##STEP 1
#return here a 1D array with all values for all events
csvfile = "/Users/ldocao/Google Drive/Documents/Professionnel/2015 08 03 S2DS/utelly-s2ds15/clustering/io/phoenix.event.csv"
df = pd.read_csv(csvfile)
duration = np.array(df["||metadata||duration"])

#what to do here for o_d_events ?


#compute distance


#grouping


#label
