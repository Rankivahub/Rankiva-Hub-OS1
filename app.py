import streamlit as st
from utils.logo_handler import display_logo

st.set_page_config(page_title="My Ranking Hub", layout="wide")

display_logo() # Logo handler se logo load karein
st.title("Ranking Hub Tool")

st.write("Welcome to the main dashboard!")
