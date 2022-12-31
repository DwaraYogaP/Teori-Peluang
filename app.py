import streamlit as st
import joblib,os
import numpy as np

def predict(file):
    load = joblib.load(open(os.path.join(file), "rb"))
    return load

st.title("Prakiraan Cuaca")
temp_min = st.number_input("Suhu Minimum", 0, 50)
temp_max = st.number_input("Suhu Maksimum", 0, 50)
temp_avg = st.number_input("Suhu Rata-Rata", 0, 50)

air = st.number_input("Kelembaban Udara", 0, 500)
wind = st.number_input("Kecepatan Angin", 0, 30)

if st.button("Proses"):
    regresi = predict("weather.pkl")
    result = regresi.predict([[temp_avg, temp_min, temp_max, air, wind]])

    num = float(np.asarray(result))
    st.info(num)
    if num < 1:
        st.info("Berawan")
    elif num <20:
        st.info("Hujan Ringan")
    elif num <50:
        st.info("Hujan Sedang")
    elif num <100:
        st.info("Hujan Lebat")
    elif num <150:
        st.info("Hujan sangat lebat")
    else:
        st.info("Hujan ekstrem")
