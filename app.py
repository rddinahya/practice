import streamlit as st
import numpy as np
import joblib

model = joblib.load("best_model.pkl")

st.title("student Exam Score Predictor")

study_hours = st.slider("Study Hours per Day", 0.0, 12.0, 2.0)
attendance 
mental_health
sleep_hours
part_time_job 