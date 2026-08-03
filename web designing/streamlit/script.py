import os

import streamlit as st

st.markdown("""
    <style>
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 28px;
        font-size: 16px;
        border: none;
        border-radius: 50px;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)
import sys
# Real Streamlit button (fully supported)
if st.button("Click Me"):
    st.success("✅ You clicked the round button!")
    os.system("streamlit run main.py")
    sys.exit()



a=st.text_input("input")
