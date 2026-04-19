import pandas as pd
import numpy as np
import math
from statistics import mode
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# Part 1: KNN Class
class KNN:
    """K-Nearest Neighbors classifier implemented from scratch."""

    def __init__(self, k):
        """Initialize the KNN model."""
        self.k = k

    def fit(self, X, y):
        """Store training data and labels."""
        self.X_train = X
        self.y_train = y

    def euclidean_distance(self, x1, x2):
        """
        Compute the Euclidean distance between two data points.

        Args: x1, x2 - two data points
        Returns: the Euclidean distance
        """
        total = 0

        for i in range(len(x1)):
            total += (x1[i] - x2[i]) ** 2
        return math.sqrt(total)

    def compute_distances(self, x):
        """
        Compute distance from a single point x to every training point.

        Args: x - a single data point
        Returns: list of (distance, label) tuples
                 (Euclidian distance & training label)
        """
        distances = []

        for ix, point in enumerate(self.X_train):
            distance = self.euclidean_distance(x, point)
            label = self.y_train[ix]
            distances.append((distance, label))
        return distances

    def get_kneighbors(self, distances):
        """
        Sort (distance, label) tuples by distance and return the K closest.
        Sorted in ascending order (closest to farthest)

        Args: distances - list of (distance, label) tuples
        Returns: list of the K nearest (distance, label) tuples
        """
        sorted_distances = sorted(distances)
        return sorted_distances[:self.k]

    def classification(self, k_nearest):
        """
        Take K nearest neighbors & return most frequent class

        Args: k_nearest - list of (distance, label) tuples
        Returns: single predicted label
        """
        labels = []

        for neighbor in k_nearest:
            labels.append(neighbor[1])
        return mode(labels)

    def predict_single(self, x):
        """
        Full prediction pipeline for a single data point.

        Args: x - a single data point
        Returns: predicted class label
        """
        distances = self.compute_distances(x)
        k_nearest = self.get_kneighbors(distances)
        return self.classification(k_nearest)

    def predict(self, X):
        """
        Generate predictions for all data points in X.

        Args: X - 2D list of data points
        Returns: list of predicted labels, one per data point
        """
        predictions = []

        for x in X:
            predictions.append(self.predict_single(x))
        return predictions

# PART 2.a.1: Load Data & Run EDA
def load_data():
    """Load all three CSV files and return them."""
    X_train = pd.read_csv("HW_03_train_features.csv").drop(columns=["ROW_ID"])
    y_train = pd.read_csv("HW_03_train_target.csv")["Target"]
    X_test  = pd.read_csv("HW_03_test_features.csv").drop(columns=["ROW_ID"])
    return X_train, y_train, X_test

def run_eda(X_train, y_train):
    """Explore the training data before modeling."""
    print("Shape:", X_train.shape)
    print("\nDescriptive Statistics:")
    print(X_train.describe())
    print("\nMissing Values:\n", X_train.isnull().sum())
    print("\nClass Distribution:\n", y_train.value_counts())

def train_val_split(X, y, val_size=0.2, random_state=42):
    """
    Split training data into train and validation sets.

    Returns: X_tr, X_val, y_tr, y_val as numpy arrays
    """
    np.random.seed(random_state)
    n = len(X)
    indices = np.random.permutation(n)
    cutoff = int(n * (1 - val_size))

    train_indices = indices[:cutoff]
    val_indices = indices[cutoff:]

    X_tr = X.iloc[train_indices].values
    X_val = X.iloc[val_indices].values
    y_tr = y[train_indices]
    y_val = y[val_indices]

    return X_tr, X_val, y_tr, y_val

# Part 2.a.2: Preprocessing & Manipulation Functions
def zscore_standardize(X_train, X_val, X_test):
    """
    Z-score standardize all features.

    Fit on X_train only to avoid data leakage, then apply to val and test.
    Returns: X_train, X_val, X_test
    """
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    return X_train, X_val, X_test

def minmax_normalize(X_train, X_val, X_test):
    """
    Min-max normalize all features to [0, 1].

    Fit on X_train only to avoid data leakage, then apply to val and test.
    Returns: X_train, X_val, X_test
    """
    scaler = MinMaxScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    return X_train, X_val, X_test

# PART 2b: Model Development
def train_model(k, X_train, y_train):
    """Create and fit a KNN model."""
    model = KNN(k)
    model.fit(X_train, y_train)
    return model

def make_predictions(model, X):
    """Return predictions for X."""
    return model.predict(X)

def evaluate(y_pred, y_val):
    """Print and return F1 score"""
    score = f1_score(y_val, y_pred)
    print(f"F1 Score: {score:.4f}")
    return score

def find_best_k(X_train, y_train, X_val, y_val, max_k=30):
    """
    Try all values of k until max_k, return the k with the highest validation F1.
    Also plots F1 vs k so you can visualize the elbow.
    """
    scores = []
    k_vals = range(1, max_k + 1)

    for k in k_vals:
        model = train_model(k, X_train, y_train)
        preds = make_predictions(model, X_val)
        scores.append(f1_score(y_val, preds))

    best_k = k_vals[np.argmax(scores)]
    print(f"Best k: {best_k}  |  Best F1: {max(scores):.4f}")

    plt.figure()
    plt.plot(list(k_vals), scores, marker='o')
    plt.xlabel("k")
    plt.ylabel("Validation F1")
    plt.title("F1 Score vs. k")
    plt.tight_layout()
    plt.show()

    return best_k

# PART 2c: Save Predictions
def save_predictions(y_pred, filename="predictions.csv"):
    """Save predictions in CSV file."""
    out = pd.DataFrame({
        "ROW_ID": range(len(y_pred)),
        "Target": y_pred
    })
    out.to_csv(filename, index=False)
    print(f"Predictions saved to {filename}")

if __name__ == "__main__":
    # 1. Load the Data
    X_train, y_train, X_test = load_data()

    # 2. EDA
    run_eda(X_train, y_train)

    # 3. Train / Val Split
    X_tr, X_val, y_tr, y_val = train_val_split(X_train, y_train.values.ravel())

    # 4. Preprocess
    X_tr, X_val, _ = zscore_standardize(X_tr, X_val, X_test.values)

    # 5. Find Best k
    best_k = find_best_k(X_tr, y_tr, X_val, y_val, max_k=30)

    # 6. Retrain on Full Training Data with Best k
    X_train_final, _, X_test_final = zscore_standardize(X_train.values, X_train.values, X_test.values)
    final_model = train_model(best_k, X_train_final, y_train.values.ravel())

    # 7. Predict on Test Set and Save
    test_preds = make_predictions(final_model, X_test_final)
    save_predictions(test_preds)