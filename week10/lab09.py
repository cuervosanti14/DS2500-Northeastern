# LAB EXERCISE 09

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Predefined dataset
data = {
    'ID': list(range(1, 101)),
    'Hours_worked': [150, 72, 168, 55, 30, 10, 158, 60, 170, 128, 120, 115, 50,
145, 118, 58, 172, 110, 70, 140, 85, 95, 102, 66, 134, 143, 77, 89, 160, 121, 109,
97, 53, 147, 112, 59, 165, 108, 73, 138, 92, 101, 104, 69, 132, 141, 79, 87, 162,
119, 107, 99, 56, 148, 114, 61, 167, 105, 75, 136, 90, 100, 106, 67, 133, 142, 78,
88, 161, 122, 110, 98, 54, 146, 113, 60, 166, 107, 74, 137, 91, 103, 105, 68, 131,
139, 80, 86, 159, 123, 111, 96, 52, 144, 117, 62, 169, 109, 76, 135],
    'Coffee_intake': [3.1, 2.9, 5.0, 2.5, 4.4, 2.0, 3.6, 3.0, 5.3, 2.4, 5.9, 3.2,
1.9, 5.7, 2.7, 4.6, 4.8, 5.4, 4.1, 3.5, 3.0, 2.7, 4.9, 2.8, 5.6, 5.2, 3.3, 3.8,
4.2, 2.6, 3.4, 2.9, 2.1, 5.5, 2.8, 4.3, 5.1, 5.0, 3.7, 3.6, 2.9, 3.1, 4.8, 2.7,
5.4, 5.3, 3.2, 3.9, 4.0, 2.5, 3.3, 2.8, 2.2, 5.6, 2.9, 4.4, 5.2, 5.1, 3.8, 3.7,
3.0, 3.2, 4.7, 2.6, 5.5, 5.4, 3.1, 3.8, 4.1, 2.7, 3.5, 2.9, 2.3, 5.7, 2.8, 4.5,
5.3, 5.2, 3.6, 3.5, 2.8, 3.0, 4.6, 2.7, 5.3, 5.2, 3.4, 3.9, 4.2, 2.6, 3.6, 2.8,
2.4, 5.8, 2.9, 4.6, 5.4, 5.3, 3.7, 3.6],
    'Stress_level': [6.2, 5.5, 7.7, 5.3, 6.8, 4.9, 6.1, 5.8, 7.5, 6.4, 8.1, 5.6,
5.0, 7.5, 5.9, 6.6, 7.2, 7.8, 6.2, 6.0, 5.7, 5.4, 7.3, 5.6, 7.6, 7.4, 6.1, 6.3,
6.5, 5.5, 5.9, 5.7, 5.1, 7.4, 5.8, 6.5, 7.3, 7.2, 6.2, 6.1, 5.8, 6.0, 7.1, 5.5,
7.5, 7.3, 6.0, 6.2, 6.4, 5.4, 5.8, 5.6, 5.2, 7.6, 5.7, 6.6, 7.4, 7.3, 6.3, 6.2,
5.9, 6.1, 7.0, 5.5, 7.4, 7.2, 6.1, 6.3, 6.5, 5.6, 5.9, 5.7, 5.3, 7.7, 5.8, 6.7,
7.5, 7.4, 6.2, 6.1, 5.7, 5.9, 6.9, 5.4, 7.3, 7.2, 6.0, 6.3, 6.6, 5.5, 6.0, 5.8,
5.4, 7.8, 5.9, 6.8, 7.6, 7.5, 6.3, 6.2],
}
df = pd.DataFrame(data)

def split_data(df):
    """
    Splits dataset into training (64%), validation (16%), & test (20%) sets

    Parameters: pandas dataframe
    Returns: training feature, validation features, test features
             training labels, validation labels, test labels
    """
    X = df.drop(columns=["Stress_level"])
    y = df["Stress_level"]

    X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=2500)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.2, random_state=2500)

    return X_train, X_val, X_test, y_train, y_val, y_test

def feature_selection(X_train, X_val, X_test, features):
    """
    Selects specific features from the feature sets

    Parameters: training features, validation features, test features,
                list of column names to select
    Returns: 3 dataframes w/ only selected features (columns)
        1. training features
        2. validation features
        3. test features
    """
    X_train = X_train[features]
    X_val = X_val[features]
    X_test = X_test[features]

    return X_train, X_val, X_test

def train_model(X_train, y_train):
    """
    Trains a linear regression model on the training data

    Parameters: training features, training labels
    Returns: trained model object
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X, y):
    """
    Evaluates a trained model on a dataset & returns performance

    Parameters: trained linear regression model, feature data, true labels
    Returns: mean squared error (MSE)
    """
    y_pred = model.predict(X)

    return mean_squared_error(y, y_pred)

def main():
    print("Problem 1: Splitting Data")
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)
    print(f"Training set: {len(X_train)} samples")
    print(f"Validation set: {len(X_val)} samples")
    print(f"Test set: {len(X_test)} samples")
    print(f"Feature columns: {X_train.columns.tolist()}")

    print("\nProblem 2: Feature Selection (both features)")
    X_train_sel, X_val_sel, X_test_sel = feature_selection(X_train, X_val, X_test, ['Hours_worked', 'Coffee_intake'])
    print(f"Selected features: {X_train_sel.columns.tolist()}")

    print("\nProblem 3: Training Model")
    model = train_model(X_train_sel, y_train)
    print(f"Model coefficients: {model.coef_}")
    print(f"Model intercept: {model.intercept_:.4f}")

    print("\nProblem 4: Evaluating Model")
    train_mse = evaluate_model(model, X_train_sel, y_train)
    val_mse = evaluate_model(model, X_val_sel, y_val)
    test_mse = evaluate_model(model, X_test_sel, y_test)

    print(f"Training Set - MSE: {train_mse:.4f}")
    print(f"Validation Set - MSE: {val_mse:.4f}")
    print(f"Test Set - MSE: {test_mse:.4f}")

    # Compare with single feature model
    print("\nComparing with single feature (Hours_worked only)")
    X_train_hours, X_val_hours, X_test_hours = feature_selection(X_train, X_val, X_test, ['Hours_worked'])
    model_hours = train_model(X_train_hours, y_train)
    test_mse_hours = evaluate_model(model_hours, X_test_hours, y_test)
    print(f"Single feature model - MSE: {test_mse_hours:.4f}")

if __name__ == "__main__":
    main()