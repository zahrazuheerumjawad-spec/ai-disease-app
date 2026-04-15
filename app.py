import streamlit as st

st.title("AI Disease Detection 🩺")

st.write("Enter your symptoms:")

fever = st.selectbox("Do you have fever?", ["No", "Yes"])
cough = st.selectbox("Do you have cough?", ["No", "Yes"])
headache = st.selectbox("Do you have headache?", ["No", "Yes"])

if st.button("Predict"):
    if fever == "Yes" and cough == "Yes":
        st.success("You may have Flu 🤒")
    elif headache == "Yes":
        st.warning("You might be tired or stressed 😴")
    else:
        st.success("You are likely fine 😊")
