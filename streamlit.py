# -- import libraries --
import streamlit as st
import streamlit_lottie
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import streamlit_pdf_reader
from streamlit_pdf_reader import pdf_reader

# -- load assets --
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation = load_lottieurl("https://lottie.host/0f8011fb-c4f1-42d2-848c-fa560174cbde/UkjgMal1fr.json")
img_uci = Image.open('images/uci.png')
img_wgu = Image.open('images/wgu.png')
img_train = Image.open('images/uci_train.png')
rjc = Image.open('images/rjc.jpeg')
img_spotify = Image.open('images/spotify.png')
img_msda = Image.open('images/msda.webp')

# import pdf
resume = 'Ryan James Calabio Resume.pdf'

# -- configure page --
st.set_page_config(page_title="Ryan James Calabio Portfolio", page_icon=":desktop_computer:", layout="wide")

# -- Header Section --
with st.container():
    st.subheader("Hi, my name is RJ :wave:")
    st.title("Data Analytics, Business Intelligence, & Data Science Specialist")
    st.write("---")
    image_column, text_column = st.columns((1,4))

with image_column:
        st.image(rjc)

with text_column:
    st.write("""
             
             I am a BI / Data Analyst with experience at a Fortune 300 company, current graduate student in Master of Science in Data Analytics @ WGU, and BA Economics @ University of California, Irvine. \n
             This portfolio was coded in Python using Streamlit!
             
             """)
    st.write("[Check out my github!](https://github.com/ryanjamestwo)")
    st.write("[Check out my LinkedIn!](https://www.linkedin.com/in/rjcalabio/)")


# -- What I do --
with st.container():
    left_column, right_column = st.columns((3,1))
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            
            I’m a highly motivated and results-driven Business Intelligence and Data Analyst with a passion for data 
            science and a background in economics, data analytics, and experience at a Fortune 300 company. My journey 
            in the world of analytics has been both exciting and rewarding, allowing me to leverage cutting-edge technologies 
            like Snowflake, Power BI, and other tools to drive data-informed decisions.
        

            """
        )

with right_column:
    st_lottie(lottie_animation, height=300, key="coding")


# -- Education --
with st.container():
    st.write("---")
    st.title("Education")
    st.write("---")
    image_column, text_column = st.columns((1,3))
    with image_column:
        st.image(img_uci)

    with text_column:
        st.header("University of California, Irvine")
        st.subheader("Bachelor’s Degree, Economics")
        st.write(
                """
                 I received my bachelor’s degree in economics from UC Irvine: a 
                 top 10 public research university known for its rigorous academics, 
                 cutting-edge research, and leadership and character development.
                 
                 """
                 )
        
with st.container():
    st.write("---")
    text_column, image_column = st.columns((3,1))
    with image_column:
        st.image(img_wgu)

    with text_column:
        st.header("Western Governors University")
        st.subheader("Masters of Science, Data Analytics")
        st.write(
                """
                I am currently enrolled in the WGU Masters of Science in Data Analytics. Through this program I developed a mastery of key data analytics and data science concepts such as data acquisition, data cleaning, exploratory data analysis, predictive modeling, data mining, and data reporting.
                 
                 """
                 )
        
# -- Projects
with st.container():
    st.write("---")
    st.title("Projects")
    st.write("---")

# wgu projects
with st.container():
    image_column, text_column = st.columns((1,3))
    with image_column:
        st.image(img_msda)

    with text_column:
        st.header("Master of Science in Data Analytics Projects")
        st.write(
                """
                 The Masters of Science in Data Analytics explores the entire lifecycle of data through practical work. It covers:
                 - Advanced Data Acquisition
                 - Data Cleaning
                 - Exploratory Data Analysis
                 - Predictive Modeling
                 - Data Mining
                 - Representation & Reporting
                 - Advanced Data Analytics
                 """)
        st.write("[Projects Repository Here!](https://github.com/ryanjamestwo/ms_data_analytics)")

# uci datathon
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1,3))
    with image_column:
        st.image(img_train)

    with text_column:
        st.header("UCI Datathon 2023 Winner – Sepsis: A Case Study")
        st.write(
            """
            UCI hosted its first Datathon in 2023, allowing students to compete against one another and be judged and learn 
            from industry professionals. With my team of 4, we created the best analysis of the dataset of sepsis patients, which was provided by UCI Health.
            """
            )
        st.write(
            """
            **Summary of Project** \n

            For the UCI Datathon 2023, teams were given the option to choose from 4 separate datasets. The dataset that my team decided on was the \n

            **Where We Succeeded** \n

            - Getting the data: we were successfully able to overcome the hurdle of dealing with Azure Data Studio not being able to import data from the database directly into the server by doing our SQL queries separately and then importing our data into tableau
            - Feature Engineering: I was successful in being able to create SQL queries to develop the columns that we planned out in our final table.
            - Data Visualizations: I told my teammates to work on visualizations from the data that we had developed while I worked on setting up the data for the classification model. When people were struggling with creating visualizations within Python, I suggested we move to tableau for some of them which sped up the creation of visualizations among the team \n

            **What I Learned** \n

            - The importance of optimizing SQL queries, especially when on a time crunch and dealing with tens of millions of rows of data.
            - The importance of fully understanding the data and its structure before diving in
            - The importance of being having a full plan for everything but still being able to keep if flexible
            - The importance of having a good understanding of your team’s strengths and weaknesses
            """
        )
        st.write("[View Project](https://devpost.com/software/sepsis-a-case-study?ref_content=my-projects-tab&ref_feature=my_projects)")

# spotify multiple regression paper
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1,3))
    with image_column:
        st.image(img_spotify)

    with text_column:
        st.header("What Metrics Affect a Song’s Popularity on Spotify: An Analysis Using Multiple Regression")
        st.write(
            """
            The topic of this paper is understanding what variables commonly occur in the most popular songs on Spotify. To determine this, I used multiple regression analysis in Excel. This paper draws conclusions using information including Spotify’s statistics about artists and their songs that are accessible to the public through their API.

            """
            )
        st.write("[Read Paper Here](https://github.com/ryanjamestwo/spotify_multiple_regression/blob/main/what-metrics-affects-popularity-of-a-song-on-spotify-an-analysis-using-regression.pdf)")

# -- Resume --
with st.container():
    st.write("---")
    st.header("Resume")
    pdf_reader(resume)

