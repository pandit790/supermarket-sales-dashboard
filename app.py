import streamlit as st

st.set_page_config(page_title="Supermarket App", page_icon="🛒", layout="wide")

# ✅ Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ✅ If logged in → Dashboard
if st.session_state.logged_in:
    st.switch_page("pages/3_Dashboard.py")
else:
    st.switch_page("pages/1_Login.py")
