import streamlit as st

st.set_page_config(page_title="AI Disease Detection", page_icon="🩺")

st.title("AI Disease Detection 🩺")
st.write("Enter your symptoms below:")
st.warning("⚠️ This is not a medical diagnosis. It is only an educational symptom checker.")

fever = st.selectbox("Do you have fever?", ["No", "Yes"])
cough = st.selectbox("Do you have cough?", ["No", "Yes"])
headache = st.selectbox("Do you have headache?", ["No", "Yes"])
sore_throat = st.selectbox("Do you have sore throat?", ["No", "Yes"])
runny_nose = st.selectbox("Do you have runny nose?", ["No", "Yes"])
fatigue = st.selectbox("Do you feel tired/fatigue?", ["No", "Yes"])
body_pain = st.selectbox("Do you have body pain?", ["No", "Yes"])
short_breath = st.selectbox("Do you have shortness of breath?", ["No", "Yes"])
nausea = st.selectbox("Do you have nausea?", ["No", "Yes"])
stomach_pain = st.selectbox("Do you have stomach pain?", ["No", "Yes"])

if st.button("Predict"):
    yes_count = [
        fever, cough, headache, sore_throat, runny_nose,
        fatigue, body_pain, short_breath, nausea, stomach_pain
    ].count("Yes")

    if short_breath == "Yes" and fever == "Yes" and cough == "Yes":
        st.error("Possible respiratory infection. Please seek medical advice.")
    elif fever == "Yes" and cough == "Yes" and fatigue == "Yes" and body_pain == "Yes":
        st.warning("Possible flu-like illness.")
    elif sore_throat == "Yes" and runny_nose == "Yes" and fever == "No":
        st.info("Possible common cold.")
    elif nausea == "Yes" and stomach_pain == "Yes":
        st.warning("Possible stomach-related illness.")
    elif yes_count == 0:
        st.success("You seem fine based on the selected symptoms.")
    else:
        st.info("Symptoms are unclear. Please consult a healthcare professional if needed.")

    st.write(f"Total symptoms selected: {yes_count}/10")
