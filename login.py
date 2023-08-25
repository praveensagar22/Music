import streamlit as st
import hashlib
import pymongo

def show(db):
    st.write("# Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.warning("Please enter your username and password.")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # query the database for the user with the given username and hashed password
        user = db.users.find_one({"username": username, "password": hashed_password})

        if user:
            st.success("Login successful!")
            st.session_state.authenticated = True
            st.session_state.user_id = user["_id"]
        else:
            st.error("Incorrect username or password.")
