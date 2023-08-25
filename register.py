import streamlit as st
import hashlib
import pymongo

def show(db):
    st.write("# Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    if st.button("Register"):
        if not username or not password or not confirm_password:
            st.warning("Please enter a username and password.")
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # check if the username already exists in the database
        existing_user = db.users.find_one({"username": username})
        if existing_user:
            st.error("Username already exists.")
            return

        # insert the new user into the database
        new_user = {"username": username, "password": hashed_password}
        db.users.insert_one(new_user)

        st.success("Registration successful!")
