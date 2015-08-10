import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler




def normalize_std(x):
    """Return the input normalized by its standard deviation, with mean zero"""
    return (x-np.nanmean(x))/np.nanstd(x)





##STEP 1
#return here a 1D array with all values for all events
csvfile = "/Users/ldocao/Google Drive/Documents/Professionnel/2015 08 03 S2DS/utelly-s2ds15/clustering/io/phoenix.event.csv"
df = pd.read_csv(csvfile)
colnames = df.columns.values


duration = np.array(df["||metadata||duration"])
imdb_rating = np.array(df['||metadata||imdb||value'])
topic_type = np.array(df['||topic||type'])
topic_type[topic_type == "TV"] = 1.
topic_type[topic_type == "Movie"] = 0.


#normalize
duration = normalize_std(duration)
imdb_rating = normalize_std(imdb_rating)

#what to do here for o_d_events ?
data = np.array([duration, imdb_rating, topic_type.astype(np.float)]).transpose()
data = data[~np.isnan(data).any(axis=1)] #remove all rows with nan

X = data



#compute distance
# Compute DBSCAN
eps=0.5
db = DBSCAN(eps=eps, min_samples=20).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)

##############################################################################
# Plot result


# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)
    
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=4, alpha=0.1)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=2,alpha=0.1)

plt.title('eps='+str(eps)+'; Estimated number of clusters: %d' % n_clusters_)
plt.xlabel("Duration [min]")
plt.ylabel("IMDB Rating")
plt.savefig("main_"+str(eps)+".png")
