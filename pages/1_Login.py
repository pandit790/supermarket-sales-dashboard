import streamlit as st
import pandas as pd
import os

st.title("🔐 Login")

# Create users.csv if not exists
if not os.path.exists("users.csv"):
    pd.DataFrame(columns=["email", "password"]).to_csv("users.csv", index=False)

df = pd.read_csv("users.csv")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if ((df['email'] == email) & (df['password'] == password)).any():
        st.session_state.logged_in = True
        st.success("Login successful!")
        st.switch_page("pages/3_Dashboard.py")
    else:
        st.error("Invalid credentials!")

if st.button("Go to Register"):
    st.switch_page("pages/2_Register.py")
