# Multi-Disease Prediction App

A user-friendly web application for predicting the likelihood of **Liver Disease**, **Kidney Disease**, or **Parkinson's Disease** based on user inputs. This app is built with [Streamlit](https://streamlit.io/) and employs **Random Forest**, **XGBoost (XGB)**, and **Logistic Regression** machine learning models.

## Features

- **Liver Disease Prediction**: Determines whether a user is likely to have liver disease based on medical parameters.
- **Kidney Disease Prediction**: Assesses the risk of kidney disease.
- **Parkinson's Disease Prediction**: Identifies the likelihood of Parkinson's disease using voice measurements and other inputs.

## Models Used

- **Random Forest Classifier**
- **XGBoost Classifier**
- **Logistic Regression**

These models were trained on datasets tailored for each disease type.

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/multi-disease-prediction.git
   cd multi-disease-prediction
2. Install the required dependencies:
      pip install -r requirements.txt
3. Run the app:
      Home.py
## Usage

1. Launch the application in your browser after running the Streamlit command.
2. Select the disease prediction section (Liver, Kidney, or Parkinson's).
3. Fill in the required inputs (e.g., blood test values, voice features, or other medical parameters).
4. Click the "Predict" button to view the result.

## Requirements

Python 3.8 or higher
Required libraries (install via requirements.txt):
Streamlit
Scikit-learn
XGBoost
Pandas
NumPy