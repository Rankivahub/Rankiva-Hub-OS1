import sys
import os

# Ye line aapke project path ko system mein add karti hai taake imports kaam karein
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import streamlit as st
from utils.logo_handler import display_logo

# Page configuration
st.set_page_config(page_title="My Ranking Hub", layout="wide")

# Display logo (Ensure display_logo function is defined in utils/logo_handler.py)
display_logo() 

st.title("Ranking Hub Tool")

st.write("Welcome to the main dashboard!")
