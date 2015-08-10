#Type of clustering available in sklearn
===========================


# K-means
1. Start with a random number K of centroids.
2. Compute for each point the distance to each centroid and assign it to the closest one.
3. Compute the new position of the centroid based on its assigned points
4. Reiterate until convergence


# MiniBatch K-Means
Same as K-means but use only a sub-sample of points to make an estimation of the centroids. Has been invented to save computational time.

#Affinity propagation
Labeled as message passing algorithm. For a given set of datapoints (x1,... xN), we define the *similary* s such that s(xi, xj) > s(xi ,xk) iff xi is more similar to xj than to xk. So, if s(xi,xj) is high, it means that xj is a good exemplar for xi. We could choose for example minus the euclidean distance, s(xi,xj) = - (xi -xj)^2. The choice of the similarity is arbitrary. We can also assign negative similarities in the process.

1. Compute the *responsability* matrix r(i,k) that quantify how well xk can be an examplar of a cluster compare to other candidate exemplars xi.
2. Compute the *availability* matrix a(i,k) that quantify how "appropriate" it would be for xi to pick xk as its exemplar among other exemplar. it's basically the opposite to responsability. These two matrices are initialized with zeroes everywhere, meaning that every data points are equal candidates to be exemplars.
3. Update the r and a matrices, and make emerge the exemplars.

In other words, exemplars emerge as representative of a set of data points.


#Mean shift
It looks like the K-means without setting up the number of clusters. It also chooses the centroid as the most dense regions.



#Spectral Clustering
Convex sets: In Euclidean space, an object is convex if for every pair of points within the object, every point on the straight line segment that joins them is also within the object. see this page : https://pafnuty.wordpress.com/2013/08/14/non-convex-sets-with-k-means-and-hierarchical-clustering/

Useful when the clusters are not convex

#Hierarchical clustering
Tree-like clustering


#DBSCAN
Density-Based Spatial Clustering of Applications with Noise. Areas of high density separated by areas of low density. Two parameters:

* eps: The maximum distance between two samples for them to be considered as in the same neighborhood.
* min_sample: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself.


#Birch
Tree based algorithm which reduce the number of datapoints by grouping them into branches.
