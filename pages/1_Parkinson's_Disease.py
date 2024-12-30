import streamlit as st
import pickle
import numpy as np

st.title("Parkinson's Disease Lab 🌷")
st.divider()
st.markdown("***Kindly input the fields below***")

model = pickle.load(open("/workspaces/multi-disease-prediction-model/Randompark.pkl",'rb'))

def park(tests):
    inp = np.array(tests).reshape(1,-1)
    result = model.predict(inp)
    return result [0]

def main():

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        MDVP_FO = st.number_input("MDVP:Fo",value=None)
        st.caption("Enter the value in Hz")
    with col2:
        MDVP_Fhi = st.number_input("MDVP:Fhi",value=None)
        st.caption("Enter the value in Hz")
    with col3:
        MDVP_Flo = st.number_input("MDVP:Flo",value=None)
        st.caption("Enter the value in Hz")
    with col4:
        MDVP_jit = st.number_input("MDVP:Jitter(%)",value=None)
        st.caption("Jitter Percentage")

    with col1:
        Mjabs = st.number_input("MDVP:Jitter(Abs)",value=None)
        st.caption("Absolute Jitter Value")
    with col2:
        MDVP_RAP = st.number_input("MDVP:RAP",value=None)
        st.caption("Please Enter the Value")
    with col3:
        MDVP_ppq = st.number_input("MDVP:PPQ",value=None)
        st.caption("Please Enter the Value")
    with col4:
        jitddp = st.number_input("Jitter:DDP",value=None)
        st.caption("Please Enter the Value")

    with col1:
        Mdvpshim = st.number_input("MDVP:Shimmer",value=None)
        st.caption("Please Enter the Value")
    with col2:
        MDVPshimdb = st.number_input("MDVP:Shimmer(dB)",value=None)
        st.caption("Please Enter the Value")
    with col3:
        shimapq = st.number_input("Shimmer:APQ3",value=None)
        st.caption("Please Enter the Value")
    with col4:
        shimapqf = st.number_input("Shimmer:APQ5",value=None)
        st.caption("Please Enter the Value")

    with col1:
        Mdvpapq = st.number_input("MDVP:APQ",value=None)
        st.caption("Please Enter the Value")
    with col2:
        shimdda = st.number_input("Shimmer:DDA",value=None)
        st.caption("Please Enter the Value")
    with col3:
        NHR = st.number_input("NHR",value=None)
        st.caption("Please Enter the Value")
    with col4:
        HNR = st.number_input("HNR",value=None)
        st.caption("Please Enter the Value")

    with col1:
        RPDE = st.number_input("RPDE",value=None)
        st.caption("Please Enter the Value")
    with col2:
        DFA = st.number_input("DFA",value=None)
        st.caption("Please Enter the Value")
    with col3:
        spreadone = st.number_input("Spread 1",value=None)
        st.caption("Please Enter the Value")
    with col4:
        sprdtwo = st.number_input("Spread 2",value=None)
        st.caption("Please Enter the Value")

    with col1:
        dtwo = st.number_input("D2",value=None)
        st.caption("Please Enter the Value")
    with col2:
        ppe = st.number_input("PPE",value=None)
        st.caption("Please Enter the Value")

    if st.button("Predict",icon="🔮"):
        try:
            tests = (MDVP_FO,MDVP_Fhi,MDVP_Flo,MDVP_jit,Mjabs,MDVP_RAP,MDVP_ppq,jitddp,
                     Mdvpshim,MDVPshimdb,shimapq,shimapqf,Mdvpapq,shimdda,NHR,HNR,RPDE,
                     DFA,spreadone,sprdtwo,dtwo,ppe)
            
            prediction = park(tests)
            if prediction == 1:
                st.markdown("You are most likely to have Parkinson's Disease 🚑")
            else:
                st.markdown("***You don't have Parkinson's Disease!***")

        except ValueError as e:
            st.error(f"Error:{e}")

if __name__ == "__main__":
    main()