import streamlit as st

st.set_page_config(page_title='Resume Reviser - A Free Resume Analyzer Tool', layout='wide', page_icon='./Logo/logo.ico',
                   initial_sidebar_state="collapsed")


st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

hide_st_style = """ 
    <style>
    footer {visibility:hidden;}
    header {visibility: hidden;}
    sidebar {visibility:hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
# navbar
with st.container():
    st.markdown(""" 

 <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-primary d-flex flex-row justify-content-between mt-1 mx-3 rounded ">
  <a class="navbar-brand text-white font-weight-bold border px-2 rounded hoverable" href="#home">Resume<span class='text-warning'>Reviser</span></a>
   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
   </button>
   <div class="collapse navbar-collapse " id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link text-white" href="#home">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item ">
        <a class="nav-link text-white" href="#services">Services</a>
      </li>
      <li class="nav-item ">
        <a class="nav-link text-white" href="#about" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          About
        </a>
      </li>
      <li class="nav-item ">
        <a class="nav-link text-white" href="#teams">Teams</a>
      </li>
      <li class="nav-item ">
        <a class="nav-link text-white" href="#contact">Contact</a>
      </li>
      <li class="nav-item ">
        <a class="btn btn-light my-2 my-sm-0 text-dark h5" type="submit" href='/tips' target='_self'>Resume Tips and Tricks</a>
      </li>



    </ul>
    <form class="form-inline my-2 my-lg-0">
      <a class="btn btn-success my-2 my-sm-0 text-white" type="submit" href='/auth' target='_self'>Get Started</a>
    </form>
   </div>
  </nav>  """, unsafe_allow_html=True)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(
            """
            <div class='text-dark' id='home'>.</div>
            <div class="text-dark mt-4">.</div>
            <div>
          <h4 class="font-weight-bold">Resume Reviser - A Free Resume Analyzer Tool</h4>
          </div>
          """, unsafe_allow_html=True)
        st.markdown(
            """
              <div class="">
                <h1 class='text-start font-weight-bold '>A Single Platform Built to Analyze your Resume.</h1>
   
                <h5 class="text-muted">Are you ready to take your career to new heights? Presenting the ultimate Resume Analyzer that transforms your Resume into a powerful tool to land your dream job.</h5>
              </div>
              <br>
              <a class="btn btn-success text-white px-5" href="/auth" role="button" target='_self'>Get Started</a>
            """,
            unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.write('')
    with right_column:
        st.image('./assets/resume.png')

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    with st.container():
        left_column, right_column, center_column, column1_column = st.columns(4)
        with left_column:
            st.image('./assets/havard1.png', width=250)
            st.write(' ')
        with center_column:
            st.image('./assets/google.png', width=150)
            st.write('')
        with right_column:
            st.image('./assets/meta.png', width=200)
            st.write('')
        with column1_column:
            st.image('./assets/kathford1.jpg', width=200)
            st.write('')

    st.write("")
    st.write("")
    st.write("")
    # features
    st.markdown("""
 <div class="mb-5 text-dark" id="services">.</div>

<section class="py-5 py-xl-8 bg-muted mt-5 mb-5 rounded" >
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-12 col-md-10 col-lg-8 col-xl-7 col-xxl-6">
        <h2 class="mb-4 display-5 text-center font-weight-bold">Our Services</h2>
        <br>
        <br>
        
      
  </div>

  <div class="container overflow-hidden">
    <div class="row gy-5 gx-md-4 gy-lg-0 gx-xxl-5 justify-content-center">
      <div class="col-11 col-sm-6 col-lg-3">
        <div class="badge bg-primary p-3 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-pie-chart" viewBox="0 0 16 16">
            <path d="M7.5 1.018a7 7 0 0 0-4.79 11.566L7.5 7.793V1.018zm1 0V7.5h6.482A7.001 7.001 0 0 0 8.5 1.018zM14.982 8.5H8.207l-4.79 4.79A7 7 0 0 0 14.982 8.5zM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8z" />
          </svg>
        </div>
        <h4 class="mb-3">Resume Extraction</h4>
        <p class="mb-3 text-secondary">Ensure accurate and reliable extraction to streamline the resume analysis process.</p>
        <a href="#!" class="fw-bold text-decoration-none link-primary">
          Learn More
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-short" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z" />
          </svg>
        </a>
      </div>
      <div class="col-11 col-sm-6 col-lg-3">
        <div class="badge bg-primary p-3 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-aspect-ratio" viewBox="0 0 16 16">
            <path d="M0 3.5A1.5 1.5 0 0 1 1.5 2h13A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 12.5v-9zM1.5 3a.5.5 0 0 0-.5.5v9a.5.5 0 0 0 .5.5h13a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-13z" />
            <path d="M2 4.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1H3v2.5a.5.5 0 0 1-1 0v-3zm12 7a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1 0-1H13V8.5a.5.5 0 0 1 1 0v3z" />
          </svg>
        </div>
        <h4 class="mb-3">Career Recommendation</h4>
        <p class="mb-3 text-secondary">Provide personalized career recommendations based on skills, experience, and industry trends.</p>
        <a href="#!" class="fw-bold text-decoration-none link-primary">
          Learn More
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-short" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z" />
          </svg>
        </a>
      </div>
      <div class="col-11 col-sm-6 col-lg-3">
        <div class="badge bg-primary p-3 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-airplane-engines" viewBox="0 0 16 16">
            <path d="M8 0c-.787 0-1.292.592-1.572 1.151A4.347 4.347 0 0 0 6 3v3.691l-2 1V7.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.191l-1.17.585A1.5 1.5 0 0 0 0 10.618V12a.5.5 0 0 0 .582.493l1.631-.272.313.937a.5.5 0 0 0 .948 0l.405-1.214 2.21-.369.375 2.253-1.318 1.318A.5.5 0 0 0 5.5 16h5a.5.5 0 0 0 .354-.854l-1.318-1.318.375-2.253 2.21.369.405 1.214a.5.5 0 0 0 .948 0l.313-.937 1.63.272A.5.5 0 0 0 16 12v-1.382a1.5 1.5 0 0 0-.83-1.342L14 8.691V7.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v.191l-2-1V3c0-.568-.14-1.271-.428-1.849C9.292.591 8.787 0 8 0ZM7 3c0-.432.11-.979.322-1.401C7.542 1.159 7.787 1 8 1c.213 0 .458.158.678.599C8.889 2.02 9 2.569 9 3v4a.5.5 0 0 0 .276.447l5.448 2.724a.5.5 0 0 1 .276.447v.792l-5.418-.903a.5.5 0 0 0-.575.41l-.5 3a.5.5 0 0 0 .14.437l.646.646H6.707l.647-.646a.5.5 0 0 0 .14-.436l-.5-3a.5.5 0 0 0-.576-.411L1 11.41v-.792a.5.5 0 0 1 .276-.447l5.448-2.724A.5.5 0 0 0 7 7V3Z" />
          </svg>
        </div>
        <h4 class="mb-3">Resume Score Provider</h4>
        <p class="mb-3 text-secondary">A scoring mechanism to objectively evaluate the quality of resumes</p>
        <a href="#!" class="fw-bold text-decoration-none link-primary">
          Learn More
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-short" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z" />
          </svg>
        </a>
      </div>
      <div class="col-11 col-sm-6 col-lg-3">
        <div class="badge bg-primary p-3 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-alarm" viewBox="0 0 16 16">
            <path d="M8.5 5.5a.5.5 0 0 0-1 0v3.362l-1.429 2.38a.5.5 0 1 0 .858.515l1.5-2.5A.5.5 0 0 0 8.5 9V5.5z" />
            <path d="M6.5 0a.5.5 0 0 0 0 1H7v1.07a7.001 7.001 0 0 0-3.273 12.474l-.602.602a.5.5 0 0 0 .707.708l.746-.746A6.97 6.97 0 0 0 8 16a6.97 6.97 0 0 0 3.422-.892l.746.746a.5.5 0 0 0 .707-.708l-.601-.602A7.001 7.001 0 0 0 9 2.07V1h.5a.5.5 0 0 0 0-1h-3zm1.038 3.018a6.093 6.093 0 0 1 .924 0 6 6 0 1 1-.924 0zM0 3.5c0 .753.333 1.429.86 1.887A8.035 8.035 0 0 1 4.387 1.86 2.5 2.5 0 0 0 0 3.5zM13.5 1c-.753 0-1.429.333-1.887.86a8.035 8.035 0 0 1 3.527 3.527A2.5 2.5 0 0 0 13.5 1z" />
          </svg>
        </div>
        <h4 class="mb-3">Analysis Feedback</h4>
        <p class="mb-3 text-secondary">Provide actionable suggestions for improvement, ensuring your can enhance your resumes for better success in job applications.</p>
        <a href="#!" class="fw-bold text-decoration-none link-primary">
          Learn More
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-short" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z" />
          </svg>
        </a>
      </div>
    </div>
  </div>
</section>


<div id="about" class="mb-5 text-dark">.</div>
<div id="about" class="mb-2 text-dark">.</div>


<div class="mt-5 border border-primary h-100 mb-2" id="about">

<div class="py-3 py-md-5 bg-white h-100" >
  <div class="container">
    <div class="row gy-3 gy-md-4 gy-lg-0 align-items-lg-center">
      <div class="col-12 col-lg-6 col-xl-5">
        <img class="img-fluid rounded" loading="lazy" src="https://static.vecteezy.com/system/resources/previews/007/750/535/original/resumes-cv-application-selection-and-management-of-personnel-analysis-of-personnel-resume-vector.jpg" alt="About 1">
      </div>
      <div class="col-12 col-lg-6 col-xl-7">
        <div class="row justify-content-xl-center">
          <div class="col-12 col-xl-11">
            <h2 class="mb-3 text-dark font-weight-bold">Who Are We?</h2>
            <p class="lead fs-4 text-secondary mb-3 text-dark">We, Resume Reviser can be considered as a platform where we aim to revolutionize the resume review process and empower users to optimize their professional profiles. We perform:</p>
            <p class="mb-5 text-dark">.</p>
            <div class="row gy-4 gy-md-0 gx-xxl-5X">
              <div class="col-12 col-md-6">
                <div class="d-flex ">
                  <div class="me-4 text-primary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
                      <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
                    </svg>
                  </div>
                  <div>
                    <h2 class="h4 mb-3 text-dark">Resume Analysis</h2>
                    <p class="text-secondary mb-0 "></p>
                  </div>
                </div>
              </div>
              <div class="col-12 col-md-6">
                <div class="d-flex">
                  <div class="me-4 text-primary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16">
                      <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16Zm0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15Z" />
                    </svg>
                  </div>
                  <div>
                    <h2 class="h4 mb-3 text-dark">Provide Constructive Feedback</h2>
                    <p class="text-secondary mb-0"></p>
                  </div>
                </div>
              </div>
              <div class="col-12 col-md-6">
                <div class="d-flex">
                  <div class="me-4 text-primary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16">
                      <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16Zm0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15Z" />
                    </svg>
                  </div>
                  <div>
                    <h2 class="h4 mb-3 text-dark">Show Skills Assessment</h2>
                    <p class="text-secondary mb-0"></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>



 """, unsafe_allow_html=True)
    st.write("")
    st.write('')
    st.markdown("""

     <div class="py-5 team3 mt-5" id="teams">
  <div class="container">
    <div class="row justify-content-center mb-4">
      <div class="col-md-7 text-center">
        <h3 class="mb-3 font-weight-bold">Experienced & Professional Team</h3>
        <h6 class="subtitle font-weight-normal">You can relay on our amazing features list and also our customer services will be great experience for you without doubt and in no-time</h6>
      </div>
    </div>
    <div class="row">
      <!-- column  -->
      <div class="col-lg-4 mb-4">
        <!-- Row -->
        <div class="row">
          <div class="col-md-12">
            <img src="https://i.ibb.co/FDkrKf2/anish.jpg" alt="wrapkit" class="img-fluid rounded-circle" />
          </div>
          <div class="col-md-12">
            <div class="pt-2">
              <h5 class="mt-4 font-weight-bold mb-0 text-center">Anish Chaulagain</h5>
              <h6 class="subtitle text-center">Front End Developer</h6>
              <p class="text-center" >You can relay on our amazing features list and also our customer services will be great experience.</p>
              <ul class="list-inline">
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-facebook"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-twitter"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-instagram"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-behance"></i></a></li>
              </ul>
            </div>
          </div>
        </div>
        <!-- Row -->
      </div>
      <!-- column  -->
      <!-- column  -->
      <div class="col-lg-4 mb-4">
        <!-- Row -->
        <div class="row">
          <div class="col-md-12 pro-pic">
            <img src="https://i.ibb.co/Kx5j7JW/nuren-edited.png" alt="wrapkit" class="img-fluid rounded-circle" />
          </div>
          <div class="col-md-12">
            <div class="pt-2">
              <h5 class="mt-4 font-weight-bold mb-0 text-center ">Nuren Sherpa</h5>
              <h6 class="subtitle text-center">Back End Developer</h6>
              <p class="text-center">You can relay on our amazing features list and also our customer services will be great experience.</p>
              <ul class="list-inline">
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-facebook"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-twitter"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-instagram"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-behance"></i></a></li>
              </ul>
            </div>
          </div>
        </div>
        <!-- Row -->
      </div>
      <!-- column  -->
      <!-- column  -->
      <div class="col-lg-4 mb-4">
        <!-- Row -->
        <div class="row">
          <div class="col-md-12 pro-pic">
            <img src="https://i.ibb.co/tcwgq8b/lucky.jpg" alt="wrapkit" class="img-fluid rounded-circle" />
          </div>
          <div class="col-md-12">
            <div class="pt-2">
              <h5 class="mt-4 font-weight-bold mb-0 text-center">Lucky Shrestha</h5>
              <h6 class="subtitle text-center">Database Engineer</h6>
              <p class="text-center">You can relay on our amazing features list and also our customer services will be great experience.</p>
              <ul class="list-inline">
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-facebook"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-twitter"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-instagram"></i></a></li>
                <li class="list-inline-item"><a href="#" class="text-decoration-none d-block px-1"><i class="icon-social-behance"></i></a></li>
              </ul>
            </div>
          </div>
        </div>
        <!-- Row -->
      </div>
      <!-- column  -->
    </div>
  </div>
</div>


   """, unsafe_allow_html=True)

    contact_form = """
 <div id="contact">
 <h1 class="font-weight-bold text-center">Contact Us</h1>
<form class="d-flex flex-column align-items-center"  action="https://formsubmit.co/3e0d17ec070bdbb70af59311848f6644" method="POST">
        <input class="w-100 p-2" type="hidden" name="_captcha" value="false">
        <input class="w-100 p-2 border rounded my-2" type="text" name="name" placeholder="Your name" required>
        <input class="w-100 p-2 border rounded my-2" type="email" name="email" placeholder="Your email" required>
        <textarea class="w-100 py-3 border rounded my-2" name="message" placeholder="Your message here" required></textarea>
        <button class="w-25 p-2 font-weight-bold rounded my-3 btn btn-success" type="submit">Send</button>
    </form> 
 </div>
 """
    st.write("")
    st.write("")
    logo = """
  <img src="https://img.freepik.com/free-vector/hand-employer-analyzing-resume-candidate-with-magnifier-document-with-checked-checkboxes-flat-vector-illustration-job-search-recruitment-hr-concept-banner-website-design-landing-page_74855-26016.jpg" alt="Logo" class="h-50 w-50 rounded"></img>
 """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.markdown(logo, unsafe_allow_html=True)

    st.markdown("""
 <div class="text-center text-lg-start mt-5">
  <!-- Copyright -->
  <div class="text-center p-3 text-white" style="background-color: rgba(0, 0, 0, 0.05);">
    © 2023 Copyright:
    <a class=" text-white" href="anishchaulagain.com.np">Team Resume Reviser - Minor Project 2080</a>
  </div>
  <!-- Copyright -->
</div>
 """, unsafe_allow_html=True)
