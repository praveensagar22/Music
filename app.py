import streamlit as st
import pymongo

# import the pages
import login
import register
import home

# set up the MongoDB client
client = pymongo.MongoClient('localhost', 27017)
db = client["hello"]

# set up the navigation
PAGES = {
    "Login": login,
    "Register": register,
    "Home": home
}

# create the main app
def main():
    st.set_page_config(page_title='My App', page_icon=':pencil:')
    st.title('My App')
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # initialize the session state
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    # display the selected page with the session state
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        page.show(db)

if __name__ == "__main__":
    main()
