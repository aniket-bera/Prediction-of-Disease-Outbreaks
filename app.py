import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='material/male-doctor:')

# Get the base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths for models and dataset
MODEL_PATH = os.path.join(BASE_DIR, "Data_models")
DATASET_PATH = os.path.join(BASE_DIR, "Dataset")

diabetes_model = pickle.load(open(os.path.join(MODEL_PATH, "diabetes_model.sav"), "rb"))
heart_disease_model = pickle.load(open(os.path.join(MODEL_PATH, "heart_disease_model.sav"), "rb"))
parkinsons_model = pickle.load(open(os.path.join(MODEL_PATH, "parkinsons_model.sav"), "rb"))

with st.sidebar:
    selected=option_menu('Prediction of disease outbreak system',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         menu_icon='hospital-fill',
                         icons=['activity','heart','person'],
                         default_index=0)

if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('No. of Pregnancies')
        SkinThickness=st.text_input('Skin Thickness Value')
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Functione Value')
    with col2:
        Glucose=st.text_input('Glucose Level')
        Insulin=st.text_input('Insulin Level')
        Age=st.text_input('Age of The Person')

    with col3:
        BloodPressure=st.text_input('Blood Pressure Value')
        BMI=st.text_input('BMI Value')
    
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,
                    Insulin,BMI,DiabetesPedigreeFunction,Age]
        try:
            user_input=[float(i) for i in user_input]
            diab_prediction=diabetes_model.predict([user_input])
            if diab_prediction[0]==1:
                diab_diagnosis='The person is diabetic'
            else:
                diab_diagnosis='The person is not diabetic'
            st.success(diab_diagnosis)
        except ValueError:
                st.error('Invalid input!!')

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic Results')
        oldpeak = st.text_input('ST Depression Induced by Exercise')
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholesterol in mg/dl')
        thalach = st.text_input('Maximum Heart Rate Achieved')
        slope = st.text_input('Slope of The Peak Exercise ST Segment')
    with col3:
        cp = st.text_input('Chest Pain Types')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        exang = st.text_input('Exercise Induced Angina')
        ca = st.text_input('Major Vessels Colored by Fluoroscopy')
        
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,
                      oldpeak, slope, ca, thal]
        try:
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)
        except ValueError:
                st.error('Invalid input!!')


if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        MDVP_Fo = st.text_input('MDVP (Hz)', key="MDVP_Fo")
        MDVP_1 = st.text_input('MDVP', key="MDVP_1")
        Shimmer_1 = st.text_input('Shimmer', key="Shimmer_1")
        HNR = st.text_input('HNR', key="HNR")
        D2 = st.text_input('D2', key="D2")
    with col2:
        MDVP_Fhi = st.text_input('MDVP (Hz)', key="MDVP_Fhi")
        MDVP_2 = st.text_input('MDVP', key="MDVP_2")
        Shimmer_2 = st.text_input('Shimmer', key="Shimmer_2")
        RPDE = st.text_input('RPDE', key="RPDE")
        PPE = st.text_input('PPE', key="PPE")
    with col3:
        MDVP_Flo = st.text_input('MDVP (Hz)', key="MDVP_Flo")
        Jitter = st.text_input('Jitter', key="Jitter")
        MDVP_3 = st.text_input('MDVP', key="MDVP_3")
        DFA = st.text_input('DFA', key="DFA")
    with col4:
        MDVP_Percent = st.text_input('MDVP (%)', key="MDVP_Percent")
        MDVP_4 = st.text_input('MDVP', key="MDVP_4")
        Shimmer_3 = st.text_input('Shimmer', key="Shimmer_3")
        spread1 = st.text_input('spread1', key="spread1")
    with col5:
        MDVP_Abs = st.text_input('MDVP (Abs)', key="MDVP_Abs")
        MDVP_dB = st.text_input('MDVP (dB)', key="MDVP_dB")
        NHR = st.text_input('NHR', key="NHR")
        spread2 = st.text_input('spread2', key="spread2")

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Percent, MDVP_Abs,
                      MDVP_1, MDVP_2, MDVP_3, MDVP_4, MDVP_dB, 
                      Jitter, Shimmer_1, Shimmer_2, Shimmer_3, 
                      HNR, NHR, RPDE, DFA, spread1, spread2, D2, PPE]
        try:
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        except ValueError:
                st.error('Invalid input!!')

