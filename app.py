import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import os

# Function to load Lottie file
def loadLottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to load CSS file
def loadCss(url):
    with open(url) as f:
        st.markdown(f"<style>{f.read()} </style>",unsafe_allow_html=True)

# Construct the file path for the image
base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "images", "img_01.jpg")

# Check if the image file exists
if os.path.exists(image_path):
    image_01 = Image.open(image_path)
    # Continue with your Streamlit app code
    # Load CSS file
    loadCss('styles/main.css')

    # Load Lottie files
    lottie_file1 = loadLottie("https://lottie.host/c8c63c42-ec0a-457a-ab64-b77a1c1e5fdc/aAqxACFvlA.json")
    lottie_file2 = loadLottie("https://lottie.host/ef8ed336-a48c-4849-a67e-18eca03c4bfa/zKk2zpTiQy.json")

    #header section --------------------------------
    with st.container():
        st.subheader("Hi ! I'm Dinesh :wave:")
        st.title("Senior Software Engineer")
        st.write("I love to new technologies and I'm following AI/ML")
        st.write("[Learn more >>](https://docs.streamlit.io/knowledge-base/using-streamlit/remove-streamlit-app-title)")

    # what I do ------------------------------------
    with st.container():
        st.write("###") #divider
        left_column,right_column = st.columns(2)
        st.write("##") #divider
        st.write( 
            """ 
            I Have experienced with,
            
            - AI.ML Projects
            - Software Engineering
            - Project Management
            - Database Designing
            
            exploring new languages, frameworks, and technologies.
            
            """
            
        ) 
        st.write("[Learn more >>](https://docs.streamlit.io/knowledge-base/using-streamlit/remove-streamlit-app-title)")

        with right_column:
            st_lottie(lottie_file1,height=300,key="coding")
                
    #project sections ---------------------------------------------
    with st.container():
        st.write("--")
        st.header("My Projects ..")
        st.write("##")
        img_col,text_col = st.columns((1,2))
        with img_col:
            st.image(image_01)
        with text_col:
            st.write('''
                     lorem In publishing and graphic design, Lorem ipsum is a placeholder 
                     text commonly used to demonstrate the visual form of a document or a 
                     typeface without relying on 
                     meaningful content. Lorem ipsum may be used as a placeholder before 
                     the final copy is available.
                     lorem In publishing and graphic design, Lorem ipsum is a placeholder 
                     text commonly used to demonstrate the visual form of a document or a 
                     typeface without relying on 
                     meaningful content. Lorem ipsum may be used as a placeholder before 
                     the final copy is available.
                     ''')
            st.markdown('[view more >>](https://github.com/)')

    #form sections ----------------------------------------------------
    with st.container():
        st.header('Contact me')
        st.write('##')
        left_col,right_col = st.columns((2))
        with left_col:
            contact_form = """
                <form>
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                    </div>
                    <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                        <label class="form-check-label" for="exampleCheck1">Check me out</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)
       
        with right_col:
            st_lottie(lottie_file2,height=200,key="mail")
        
else:
    st.error("Image file not found. Please check the file path.")

