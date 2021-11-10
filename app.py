import datetime
import streamlit as st

st.set_page_config(layout="wide")
st.title("Bitcoin Prediction with Machine Learning")
st.write("This project is not to predict the accurate price of bitcoin, \
    it is meant to learn MLOps to topic Git action, Docker compose and mlflow")

row1_1, row1_2, row1_3 = st.columns((3, 1, 1))

with row1_1:
    
    st.image("/home/trojrobert/Downloads/bitcoin_ether_training_test.png")

with row1_2:
    today = datetime.date.today() 
    st.title("Today")
    st.write(f"{str(today.strftime('%Y-%m-%d'))} - $61,970")

    st.title("Predictions")
    st.write(f"{str(today + datetime.timedelta(days = 1))} - $62,000")

with row1_3:

    n_forecast_days = st.slider("Select the number of days you want to predict \n", 1, 5)