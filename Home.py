import streamlit as st

st.logo("/workspaces/multi-disease-prediction-model/ml.png",size="large")
st.title("Multi-Disease Prediction Model ")
st.header("Get your results predicted 👨🏻‍🔬🔬🧬🧫🧪",divider = "blue")
st.write(
"""A user-friendly web application for predicting the likelihood of 
                **Liver Disease**, **Kidney Disease**, or **Parkinson's Disease** based on user inputs. 
                This app is built with [Streamlit](https://streamlit.io/) and employs **Random Forest**, 
         **XGBoost (XGB)**, and **Logistic Regression** machine learning models.""")
st.subheader("Features:")
st.write("""      
         - **Liver Disease Prediction**: Determines whether a user is likely to have liver disease based on medical parameters.
         - **Kidney Disease Prediction**: Assesses the risk of kidney disease.
         - **Parkinson's Disease Prediction**: Identifies the likelihood of Parkinson's disease using voice measurements and other inputs.
         
         """)



st.page_link("/workspaces/multi-disease-prediction-model/Home.py",label="Home",icon="🏠")
st.page_link("/workspaces/multi-disease-prediction-model/pages/1_Parkinson's_Disease.py", label="Parkinson's Disease Lab",icon="🌷")
st.page_link("/workspaces/multi-disease-prediction-model/pages/2_Liver_Lab.py",label = "Liver Disease Lab",icon="🎗")
st.page_link("/workspaces/multi-disease-prediction-model/pages/3_Kidney_Lab.py",label ="Kidney Disease Lab", icon="🫘")



