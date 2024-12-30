# --- Liver Disease Lab

import streamlit as st
import numpy as np
import pickle

st.title("Liver Lab 🎗")
st.divider()
st.markdown("***Please Enter the values below***")

model = pickle.load(open("/workspaces/multi-disease-prediction-model/XGBliver.pkl",'rb'))

def liv(tests):
    ip = np.array(tests).reshape(1,-1)
    result = model.predict(ip)
    return result [0]

def main():

    Age = st.number_input("Age",min_value=1,max_value=120,value=28,step=1)
    
    Gender = st.selectbox("Gender",options=["Male","Female"])
    Gender_map = {"Male":1,"Female":0}
    Gender_val = Gender_map[Gender]

    col1,col2,col3 = st.columns(3)
    with col1:
        TB = st.number_input("Total Bilirubin",max_value=50)
    with col2:
        db = st.number_input("Direct Bilirubin")
    with col3:
        ap = st.number_input("Alkaline Phosphotase",max_value=1000,step=1)
    with col1:
        ala = st.number_input("Alamine Aminotransferase",max_value=200,step=1)
    with col2:
        aat = st.number_input("Aspartate Aminotransferase",max_value=200,step=1)
    with col3:
        tp = st.number_input("Total Protiens")
    with col1:
        alb = st.number_input("Albumin")
    with col2:
        agr = st.number_input("Albumin and Gloublin Ratio")

    if st.button("Predict"):
        try:
            tests = (Age,Gender_val,TB,db,ap,ala,aat,tp,alb,agr)
            prediction = liv(tests)
            if prediction == 1:
                st.error("You have Liver Disease",icon="🚑")
            else:
                st.success("Your liver seems fine",icon="🙂")

        except ValueError as e:
            st.error(f"Error:{e}")

if __name__ == "__main__":
    main()