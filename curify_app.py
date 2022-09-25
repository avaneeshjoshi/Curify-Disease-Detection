import pickle
import streamlit as st
from streamlit_option_menu import option_menu 
import base64
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
import random
import string

img = Image.open('logo.png')
st.set_page_config(page_title='Curify', page_icon=img)
diabetes_m = pickle.load(open('/Users/avaneeshjoshi/Documents/GitHub/Curify-Disease-Detection/diabetes.sav', 'rb'))
heartdisease_m = pickle.load(open('/Users/avaneeshjoshi/Documents/GitHub/Curify-Disease-Detection/heart_diseaseM.sav','rb'))
parkinsons_m = pickle.load(open('/Users/avaneeshjoshi/Documents/GitHub/Curify-Disease-Detection/parkinsons_m.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Curify Disease Prediction System',
                          ['Home',
                          'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'
                           ], 
                          menu_icon="cast", default_index=0,
                          styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#586a7e", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#212759"},
    }

)



# Home


if (selected == 'Home'):
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('cell.jpg') 
    st.markdown("<h1 style='text-align: center; color: #212759; font-size: 200px; font-family: Arial; background-color: #e0e8f0; border-radius: 25px;'>Curify</h1>", unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown("<h1 style='text-align: center; color: #ffffff; font-size: 20px; font-family: Arial;'>A program that detects diseases by using Machine Learning</h1>", unsafe_allow_html=True)


# Diabetes

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if (selected == 'Diabetes Prediction'):
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('images.jpg')

    st.title('Diabetes Prediction')
    col1 = st.columns(1)

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value') 
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age') 

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_m.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Success! We have your results!'
        else:
          diab_diagnosis = 'Person is not diabetic'
    if (diab_diagnosis == 'Success! We have your results!'):
        st.error("You are most likely diabetic. Please go visit a doctor immediately!")
    elif (diab_diagnosis == 'Person is not diabetic'):
        st.success("You are most likely not diabetic.. Keep eating healthy!")
        st.balloons()

    # Heart Disease

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
if (selected == 'Heart Disease Prediction'):
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('heart.png')

    st.title('Heart Disease Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    heart_diagnosis = ''
    if st.button('Heart Disease Prediction Result'):
        heartPrediction = heart_diseaseM.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            
        if (heartPrediction[0] == 1):
            heart_diagnosis = 'Person is having heart disease'
        else: 
            heart_diagnosis = 'Person does not have any heart disease'
    st.success(heart_diagnosis)


# Parkinson's

if (selected == "Parkinsons Prediction"):
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('parksinson.png') 
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://api.time.com/wp-content/uploads/2014/06/182682597.jpg");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; color: #ffffff; font-size: 37px; font-family: Arial;'>Parkinson's Disease Prediction</h1>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)  
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
            
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_m.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease" 
        st.success(parkinsons_diagnosis)