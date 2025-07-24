import streamlit as st
import joblib
import numpy as np 

st.title("Salary Prediction App")
st.divider()

st.write("with this app, you can get estimations for the salaries of the company employees")

years = st.number_input("Enter the years at compny",value=1, step=1, min_value=0)

jobrate=st.number_input("Enter the job rate ",value=3.5, step=0.5, min_value=0.0)

x=[years,jobrate]

model = joblib.load("Linearmodel.pkl")

st.divider()
predict=st.button("Press the button for Salary Prediction")

st.divider()
if predict:
    st.balloons()
    x1=np.array([x])
    prediction = model.predict(x1)
    st.write(f"Salary prediction is {prediction}")


else:
    "Please press the button to make the prediction"