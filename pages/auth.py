import streamlit as st
import mysql.connector

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="anees@123",
        database="smart",
        auth_plugin='mysql_native_password'
    )

# Function to create a user table if not exists
def create_user_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users_verification (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL, 
            password VARCHAR(255) NOT NULL
        );
    ''')
    connection.commit()
    cursor.close()

# Function to check if email already exists
def is_email_exists(connection, email):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users_verification WHERE email = %s', (email,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

# Function to signup a new user
def signup(connection, username, email, password):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users_verification (username, email, password) VALUES (%s, %s, %s)',
                   (username, email, password))
    connection.commit()
    cursor.close()

# Function to signin an existing user
def signin(connection, email, password):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users_verification WHERE email = %s AND password = %s', (email, password))
    result = cursor.fetchone()
    cursor.close()
    return result

st.set_page_config(initial_sidebar_state="collapsed", page_title='Resume Reviser - A Free Resume Analyzer Tool')
hide_st_style = """ 
    <style>
    footer {visibility:hidden;}
    header {visibility: hidden;}
    sidebar {visibility:hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Streamlit app
def main():
    st.title("Authentication")

    # Create MySQL connection and user table
    connection = create_connection()
    create_user_table(connection)

    # Page selection (Signup or Signin)
    page = authentication_option = st.selectbox("Choose an option:", ["Signin", "Signup"])

    if page == "Signup":
        st.header("Signup")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Signup"):
            if not username or not email or not password:
                st.error("Please fill in all fields.")
            elif is_email_exists(connection, email):
                st.error("Email already exists. Please use a different email.")
            else:
                signup(connection, username, email, password)
                st.success("Signup successful. You can now signin.")

    elif page == "Signin":
        st.header("Signin")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Signin"):
            if not email or not password:
                st.error("Please fill in all fields.")
            else:
                user = signin(connection, email, password)
                if user:
                    st.success("Logged in successfully!")
                    st.markdown(
                        f"<a href='/resumeanalyzer?userid={user[0]}' target='_self' style=' display: inline-block; padding: 10px 20px; background-color: #3498db; color: #ffffff; text-align: center; text-decoration: none; border-radius: 5px; cursor: pointer; margin-top: 20px;' >Click here</a>",
                        unsafe_allow_html=True)
                else:
                    st.error("Invalid email or password. Please try again.")

    # Close MySQL connection
    connection.close()

if __name__ == "__main__":
    main()