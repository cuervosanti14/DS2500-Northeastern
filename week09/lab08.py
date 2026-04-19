# LAB EXERCISE 08
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

# Problem 1
def perform_kmeans(X, n_clusters):
    """
    Perform K-Means clustering on given data

    Parameters: X (list of lists - feature data)
                n_clusters (int - # of clusters)
    Returns: cluster labels for each sample (list)
    """
    # Create the KMeans model
    model = KMeans(n_clusters=n_clusters, random_state=2500)

    # Fit the model to the data
    model.fit(X)

    # Return cluster labels as a list
    return model.labels_.tolist()

# Problem 2
def perform_hierarchical(X, n_clusters):
    """
    Perform hierarchical (agglomerative) clustering on the given data

    Parameters: X (list of lists - feature data)
                n_clusters (int - # of clusters)
    Returns: cluster labels for each sample (list)
    """
    # Create the Hierarchical (agglomerative) Model w/ average linkage
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage='average')

    # Fit the model to the data
    model.fit(X)

    # Return cluster labels as a list
    return model.labels_.tolist()

# Problem 3
def find_optimal_clusters(X, clustering_option="kmeans", max_k=10):
    """
    Finds optimal # of clusters by testing different values of k &
    comparing their silhouette scores

    Parameters: X (list of lists - feature data)
                clustering_option (str - clustering method to use (default = "kmeans"))
                max_k (maximum # of clusters to test (default = 10))
    Returns: optimal # of clusters (k-value w/ the highest silhouette score)
    """
    best_k = 2
    best_score = -1

    for k in range(2, max_k + 1):
        # Get cluster labels using specified clustering method
        if clustering_option == "kmeans":
            cluster_labels = perform_kmeans(X, k)
        else:
            cluster_labels = perform_hierarchical(X, k)

        # Calculate & print silhouette score for this k-value
        score = silhouette_score(X, cluster_labels)
        score = float(score)
        print(f"Silhouette Score: {score:.3f}")

        # Update best k-value if score is highest seen so far
        if score > best_score:
            best_score = score
            best_k = k

    return best_k

# Problem 4
def save_clustering_results(labels, filename):
    """
    Saves clustering results to a CSV file with a single column
    Header is cluster_label & each label should appear on a new line

    Parameters: labels (predicted cluster labels)
                filename (name of output CVS file)
    Returns: None
    """
    with open(filename, 'w') as f:
        # Writen the column header
        f.write("cluster_label\n")
        # Write each label on a new line in original order
        for label in labels:
            f.write(f"{label}\n")

# Extra Problem
def min_max_scaling(X):
    """
    Perform Min-Max Scaling on the data

    Parameters: X (feature data; list of lists)
    Returns: data scaled to min-max [0,1] range
    """
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled.tolist()

def main():
    data = load_iris()
    X = data.data.tolist()

    # Testing Problem 1
    kmeans_labels = perform_kmeans(X, n_clusters=3)
    print(kmeans_labels)

    # Testing Problem 2
    hierarchical_labels = perform_hierarchical(X, n_clusters=3)
    print(hierarchical_labels)

    # Testing Problem 3
    kmeans_best_k = find_optimal_clusters(X, max_k=5)
    print(f"Optimal number of clusters using kmeans: {kmeans_best_k}")

    hierarchical_best_k = find_optimal_clusters(X, clustering_option="hierarchical", max_k=5)
    print(f"Optimal number of clusters using hierarchical: {hierarchical_best_k}")

    # Testing Problem 4
    kmeans_labels = perform_kmeans(X, n_clusters=kmeans_best_k)
    save_clustering_results(kmeans_labels, "kmeans_results.csv")
    # A new file "kmeans_results.csv" should be generated in your working directory

    # Extra Problem: Min-Max Scaling
    X_scaled = min_max_scaling(X)
    print(X_scaled)
    kmeans_best_k = find_optimal_clusters(X_scaled, max_k=5)
    print(kmeans_best_k)

if __name__ == "__main__":
    main()