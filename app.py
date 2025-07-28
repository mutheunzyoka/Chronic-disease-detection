import streamlit as st
import pandas as pd
import pickle



# #inference prediction new data


model_gbc = pickle.load(open("models/model_gbc.pkl", 'rb'))
scaler = pickle.load(open("models/scaler.pkl", 'rb')) 


def predict_chronic_disease(age,bp,sg,al,hemo,sc,htn,dm,cad,appet,pc):
    df_dict= {
    'age':[age],
    'bp':[bp],
    'sg':[sg],
    'al':[al],
    'hemo':[hemo],
    'sc':[sc],
    'htn':[htn],
    'dm':[dm],
    'cad':[cad],
    'appet':[appet],
    'pc':[pc]
    
    }
    df= pd.DataFrame(df_dict)

#ecoding
    df['htn']= df['htn'].map({"yes":1,"no":0})
    df['dm']=df['dm'].map({"yes":1,"no":0})
    df['cad']=df['cad'].map({"yes":1,"no":0})
    df['appet'] = df['appet'].map({"good":1,"poor":0})
    df['pc'] =df['pc'].map({"normal":1,"abnormal":0})

#scaling
    numeric_cols=['age','bp','sg','al','hemo','sc']
    df[numeric_cols]= scaler.transform(df[numeric_cols])

#prediction
    prediction = model_gbc.predict(df)

#return the prediction
    return prediction[0]




#ui
st.title("Chronic Kidney Disease Prediction App")

col1,col2=st.columns(2)

with col1:
    age = st.number_input("Enter Age", min_value=1, max_value=120, value=30)
    bp = st.number_input("Enter Blood Pressure", min_value=0, max_value=200, value=80)
    sg = st.number_input("Enter Specific Gravity", min_value=1.005, max_value=1.030, value=1.010, step=0.001)
    al = st.number_input("Enter Albumin Level", min_value=0, max_value=5, value=0)
    hemo = st.number_input("Enter Hemoglobin Level", min_value=0, max_value=20, value=15)
    sc = st.number_input("Enter Serum Creatinine", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

with col2:
    
    htn = st.selectbox("Hypertension", options=["yes", "no"])
    dm = st.selectbox("Diabetes Mellitus", options=["yes", "no"])
    cad = st.selectbox("Coronary Artery Disease", options=["yes", "no"])
    appet = st.selectbox("Appetite", options=["good", "poor"])
    pc = st.selectbox("Pus Cell", options=["normal", "abnormal"])

if st.button("Predict"):
    result = predict_chronic_disease(age, bp, sg, al, hemo, sc, htn, dm, cad, appet, pc)
    
    if result == 1:
        st.success("The patient is likely to have Chronic Kidney Disease.")
    else:
        st.success("The patient is likely to be healthy.")