from sklearn.tree import DecisionTreeClassifier
import joblib
import os

def train_model():
    # Simple training data
    # age >= 18 → Adult (1)
    # age < 18  → Minor (0)
    X = [[10], [15], [17], [18], [20], [25], [30]]
    y = [0, 0, 0, 1, 1, 1, 1]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    # Save model
    joblib.dump(model, "age_model.pkl")

    return model


if __name__ == "__main__":
    train_model()
