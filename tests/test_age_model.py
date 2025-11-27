import os
import joblib
from src.train import train_model
from src.predict import predict_age

def test_model_training():
    model = train_model()
    assert os.path.exists("age_model.pkl"), "Model file not created"
    assert hasattr(model, "predict"), "Model has no predict method"

def test_predict_adult():
    train_model()
    assert predict_age(20) == "Adult"

def test_predict_minor():
    train_model()
    assert predict_age(10) == "Minor"
