import streamlit as st
import sys
import os

# Ye line folder path ko confirm karti hai
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ab yahan se import karein
from utils.logo_handler import display_logo

st.set_page_config(page_title="My Ranking Hub", layout="wide")

display_logo() 
st.title("Ranking Hub Tool")
st.write("Welcome to the main dashboard!")
