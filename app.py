import streamlit as st

# Page setup
st.set_page_config(page_title="AI Disease Detection", page_icon="🩺", layout="centered")

# School and project header
st.markdown("## 🏫 Rand Schools for Education")
st.markdown("### 👩‍🎓 Developed by Grade 9C Girls")
st.markdown("#### 🧠 AI Medical Project")

st.write("---")

# Main title
st.title("AI Disease Detection 🩺")
st.write("Please answer the questions below:")

# Warning
st.warning("⚠️ This is not a medical diagnosis. This is an educational project only.")

# Symptoms
st.subheader("Enter your symptoms:")

fever = st.selectbox("Do you have fever?", ["No", "Yes"])
cough = st.selectbox("Do you have cough?", ["No", "Yes"])
headache = st.selectbox("Do you have headache?", ["No", "Yes"])
sore_throat = st.selectbox("Do you have sore throat?", ["No", "Yes"])
runny_nose = st.selectbox("Do you have runny nose?", ["No", "Yes"])
fatigue = st.selectbox("Do you feel tired or fatigued?", ["No", "Yes"])
body_pain = st.selectbox("Do you have body pain?", ["No", "Yes"])
short_breath = st.selectbox("Do you have shortness of breath?", ["No", "Yes"])
nausea = st.selectbox("Do you have nausea?", ["No", "Yes"])
stomach_pain = st.selectbox("Do you have stomach pain?", ["No", "Yes"])

# Prediction button
if st.button("Predict"):
    symptoms = [
        fever, cough, headache, sore_throat, runny_nose,
        fatigue, body_pain, short_breath, nausea, stomach_pain
    ]
    yes_count = symptoms.count("Yes")

    # Serious respiratory condition
    if short_breath == "Yes" and fever == "Yes" and cough == "Yes":
        st.error("⚠️ Possible serious respiratory condition. Please seek medical advice.")

    # COVID-like / viral infection
    elif fever == "Yes" and cough == "Yes" and fatigue == "Yes":
        st.warning("😷 Possible COVID-19 or viral infection.")

    # Flu
    elif fever == "Yes" and cough == "Yes" and body_pain == "Yes":
        st.warning("🤒 Possible flu.")

    # Common cold
    elif sore_throat == "Yes" and runny_nose == "Yes" and fever == "No":
        st.info("🤧 Possible common cold.")

    # Allergies
    elif runny_nose == "Yes" and fever == "No" and cough == "No":
        st.info("🌼 Possible allergies.")

    # Stomach illness / food poisoning
    elif nausea == "Yes" and stomach_pain == "Yes":
        st.warning("🤢 Possible stomach illness or food poisoning.")

    # Stress / fatigue
    elif fatigue == "Yes" and headache == "Yes" and fever == "No":
        st.info("😴 Possible stress or fatigue.")

    # Healthy / no symptoms
    elif yes_count == 0:
        st.success("😊 You seem fine based on the selected symptoms.")

    # Unclear
    else:
        st.info("🤔 Symptoms are unclear. Please consult a healthcare professional if needed.")

    # Symptom count
    st.write(f"🧾 Total symptoms selected: {yes_count}/10")

# Footer
st.write("---")
st.markdown("💙 Project by Grade 9C Girls - Rand Schools for Education")
