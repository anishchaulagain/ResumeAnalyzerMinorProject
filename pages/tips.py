import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Resume Reviser - A Free Resume Analyzer Tool",
    layout='wide',
    page_icon='./Logo/logo.ico',
    initial_sidebar_state="collapsed"
)

# Custom CSS to hide certain elements and add animation
custom_css = """
    <style>
    footer {visibility:hidden;}
    header {visibility: hidden;}
    sidebar {visibility:hidden;}
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .animatedTitle {
        animation: fadeIn 6s ease-out;
    }
    </style>
    """

# Function to display resume tips
def display_resume_tips():
    # Main title with animation
    st.markdown("<h1 style='text-align: center;font-size:60px' class=' font-weight-bold'>Resume Writing Tips and Tricks</h1>",
                unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True
    )

    # Using columns to display content side by side
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class='container'>
                <div class='row'>
                    <div class='col-md-12'>
                        <h2 style='text-align: ;font-size:45px' class='font-weight-bold'>Some key points are as:</h2>
                        <ul class='font-weight-normal'>
                            <li style='font-size: 25px;'>Include keywords from the Job Description.</li>
                            <li style='font-size: 25px;'>Keep your Resume Subheading Simple.</li>
                            <li style='font-size: 25px;'>Use Quantifiable numbers.</li>
                            <li style='font-size: 25px;'>Create a separate section for Notable Achievements.</li>
                            <li style='font-size: 25px;'>Check for errors such as Grammars, Spelling, Punctuation, Formatting,Headings,etc. </li>
                            <li style='font-size: 25px;'>Follow up.</li>
                        </ul>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image('./assets/resumetips.jpg', use_column_width=True, caption='Resume Writing Tips')


 # Add References section
    st.markdown("<h2 style='text-align: center;font-size:45px;' class='font-weight-bold'>References:</h2>", unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("""
        <p style='font-size: 30px; text-align: justify;' class='font-weight-normal'>
        If you'd like to explore more about resume writing, consider checking out these resources:
        </p>
        <ul style='font-size: 30px;'>
            <li style='font-size: 25px;'><a href="https://www.linkedin.com" target="_blank">linkedin.com </a></li>
            <li style='font-size: 25px;'><a href="https://www.resumegenius.com" target="_blank">resumegenius.com</a></li>
        </ul>
    """, unsafe_allow_html=True)


# Main function
def main():
    display_resume_tips()
    # Applying custom CSS to hide certain elements and add animation
    st.markdown(custom_css, unsafe_allow_html=True)


if __name__ == "__main__":
    main()