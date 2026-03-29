import streamlit as st
import requests

st.set_page_config(page_title="AI Content Ops", layout="wide")

st.title("🧠 AI Content Operations (Offline Demo)")

topic = st.text_input("Enter topic")

if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic")
    else:
        try:
            response = requests.post(
                "http://localhost:8000/process",
                params={"topic": topic}
            )

            data = response.json()

            if data["status"] == "rejected":
                st.error("❌ Compliance Failed")
                st.write(data["issues"])
                st.write(data["content"])
            else:
                st.success("✅ Approved Content")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Original")
                    st.write(data["original"])

                with col2:
                    st.subheader("Translated")
                    st.write(data["translated"])

        except Exception as e:
            st.error(f"Error: {e}")
