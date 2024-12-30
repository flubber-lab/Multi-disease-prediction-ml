import streamlit as st
import numpy as np
import pickle

st.title("Kidney Lab 🫘")
st.divider()

st.markdown("***Please Enter the values below***")

model = pickle.load(open("kidney.pkl",'rb'))

def kid(tests):
    ip = np.array(tests).reshape(1,-1)
    result = model.predict(ip)
    return result [0]

def main():
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.number_input("Age",min_value=1,max_value=120,value=28,step=1)
    with col2:
        bp = st.number_input("BP",step=1)
    with col3:
        sg = st.number_input("SG",value = 0.0, format = "%.2f")
    
    with col1:
        al = st.number_input("Al")
    with col2:
        su = st.number_input("SU")
    with col3:
        rbc = st.selectbox("RBC",options=["Normal","Abnormal"])
        rbc_map = {"Normal":1,"Abnormal":0}
        rbc_val = rbc_map[rbc]
   
    with col1:
        pc = st.selectbox("PC",options=["Normal","Abnormal"])
        pc_map = {"Normal":1,"Abnormal":0}
        pc_val = pc_map[pc]
    with col2:
        pcc = st.selectbox("PCC",options=["Not Present","Present"])
        pcc_map = {"Not Present":0,"Present":1}
        pcc_val = pcc_map[pcc]
    with col3:
        ba = st.selectbox("BA",options=["Not Present","Present"])
        ba_map = {"Not Present":0,"Present":1}
        ba_val = ba_map[ba]
    
    with col1:
        bgr = st.number_input("BGR")
    with col2:
        bu = st.number_input("BU")
    with col3:
        sc = st.number_input("SC")

    with col1:
        sod = st.number_input("Sodium")
    with col2:
        pot = st.number_input("Pottasium")
    with col3:
        hemo = st.number_input("Hemoglobin")

    with col1:
        pcv = st.number_input("PCV",step = 1)
    with col2:
        wc = st.number_input("WC", step = 1)
    with col3:
        rc = st.number_input("RC")

    with col1:
        htn= st.selectbox("Hypertension",options=["Yes","No"])
        htn_map = {"Yes":0,"No":1}
        htn_val = htn_map[htn]
    with col2:
        dm = st.selectbox("DM",options=["Yes","No"])
        dm_map = {"Yes":1,"No":0}
        dm_val = dm_map[dm]
    with col3:
        cad = st.selectbox("CAD",options=["Yes","No"])
        cad_map = {"Yes":1,"No":0}
        cad_val = cad_map[cad]

    with col1:
        appet= st.selectbox("Appetite",options=["Good","Poor"])
        appet_map = {"Good":0,"Poor":1}
        appet_val = appet_map[appet]
    with col2:
        pe = st.selectbox("PE",options=["Yes","No"])
        pe_map = {"Yes":1,"No":0}
        pe_val = pe_map[pe]
    with col3:
        ane = st.selectbox("Anemia",options=["Yes","No"])
        ane_map = {"Yes":1,"No":0}
        ane_val = ane_map[ane]

    if st.button("Predict"):
        try:
            tests = (age,bp,sg,al,su,rbc_val,pc_val,pcc_val,ba_val,bgr,
                     bu,sc,sod,pot,hemo,pcv,wc,rc,htn_val,dm_val,cad_val,
                     appet_val,pe_val,ane_val)
            prediction = kid(tests)
            if prediction == 1:
                st.error("You have Chronic Kidney Disease",icon="🚑")
            else:
                st.success("Your Kidney looks good",icon="🙂")

        except ValueError as e:
            st.error(f"Error:{e}")


if __name__ == "__main__":
    main()
