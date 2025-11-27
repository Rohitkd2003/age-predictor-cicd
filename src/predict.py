import joblib

def load_model():
    return joblib.load("age_model.pkl")

def predict_age(age):
    model = load_model()
    result = model.predict([[age]])[0]

    return "Adult" if result == 1 else "Minor"
