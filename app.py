import streamlit as st

st.set_page_config(page_title="AI Disease Detection", page_icon="🩺")

# 🎀 عنوان رئيسي
st.title("AI Disease Detection 🩺")

# 👩‍🎓 تعريف الطالبات
st.markdown("### 👩‍🎓 Developed by Grade 9C Girls")
st.markdown("#### 🌸 Project by 9C Students")

st.write("---")

# ⚠️ تنبيه
st.warning("⚠️ This is not a medical diagnosis. It is only an educational project.")

# 🧠 بداية الأسئلة
st.subheader("Enter your symptoms:")

fever = st.selectbox("Do you have fever?", ["No", "Yes"])
cough = st.selectbox("Do you have cough?", ["No", "Yes"])
headache = st.selectbox("Do you have headache?", ["No", "Yes"])
sore_throat = st.selectbox("Do you have sore throat?", ["No", "Yes"])
runny_nose = st.selectbox("Do you have runny nose?", ["No", "Yes"])
fatigue = st.selectbox("Do you feel tired?", ["No", "Yes"])
body_pain = st.selectbox("Do you have body pain?", ["No", "Yes"])

if st.button("Predict"):
    if fever == "Yes" and cough == "Yes":
        st.warning("Possible flu-like illness 🤒")
    elif sore_throat == "Yes" and runny_nose == "Yes":
        st.info("Possible common cold 🤧")
    else:
        st.success("You seem fine 😊")

# 👇 تذييل (Footer)
st.write("---")
st.markdown("💙 Made with care by Grade 9C Girls")
