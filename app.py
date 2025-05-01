import streamlit as st
import os
import together

st.title("Together AI Python Code Generator")

together.api_key = os.getenv("TOGETHER_API_KEY")

prompt = st.text_area("Enter a prompt for Python code:", placeholder="e.g., Write a Python script to reverse a string.")

if st.button("Generate"):
    if prompt:
        response = together.Complete.create(
            prompt=f"Write a Python script: {prompt}",
            model="togethercomputer/CodeLlama-13b",
            max_tokens=256,
            temperature=0.7,
        )
        st.code(response['output']['choices'][0]['text'], language='python')
    else:
        st.warning("Please enter a prompt.")
