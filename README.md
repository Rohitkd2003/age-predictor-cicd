<!-- Problem Statement: Build CI/CD for a Simple ML Model That Predicts If a Person Is Adult or Minor

Objective:
Create a CI/CD pipeline using GitHub Actions for a beginner-level machine learning project that predicts whether a person is an Adult (age ≥ 18) or Minor (age < 18).

Project Structure
age-predictor-ci-cd/
├── src/
│   ├── train.py
│   └── predict.py
├── tests/
│   └── test_age_model.py
├── requirements.txt
└── README.md

🎯 Tasks You Need to Do
CI (Continuous Integration)

When code is pushed to GitHub:

Setup Python 3.10

Install dependencies (scikit-learn, joblib, pytest)

Run unit tests:

Model file (age_model.pkl) must be created

Model must have a .predict method

Predicting age 20 should output Adult

Predicting age 10 should output Minor

CD (Continuous Deployment)

If tests pass:

Generate a simple HTML page:

Age Prediction Model
Status: All tests passed 


Deploy it to GitHub Pages automatically. -->