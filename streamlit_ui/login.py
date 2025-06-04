
import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Login Page")

users = {
    "admin": "admin123",
    "hari": "hari123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful! ✅")
                st.switch_page("pages/app.py")  # Requires Streamlit >=1.22
            else:
                st.error("Invalid credentials ❌")
