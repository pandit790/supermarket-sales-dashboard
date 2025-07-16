import streamlit as st
import pandas as pd

st.title("📝 Register")

email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if password == confirm_password:
        df = pd.read_csv("users.csv")
        if email in df['email'].values:
            st.error("Email already exists!")
        else:
            new_user = pd.DataFrame({"email": [email], "password": [password]})
            new_user.to_csv("users.csv", mode='a', header=False, index=False)
            st.success("Registration successful!")
            st.switch_page("pages/1_Login.py")
    else:
        st.error("Passwords do not match!")

if st.button("Go to Login"):
    st.switch_page("pages/1_Login.py")


