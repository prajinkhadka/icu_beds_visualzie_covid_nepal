import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime, date, time
import os 

from main import data_from_date
data = pd.read_csv("Nepal_ICU_Ventilators - Sheet1 (7).csv")
start_date = date(2021, 4, 12)

def main():
    st.sidebar.title("Choose the State")
    app_mode = st.sidebar.selectbox("",
        ["Choose State", "Pradesh-1", "Pradesh-2", "Bagmati", "Gandaki", "Lumbini", "Karnali", "Sudur-Paschim"])
    
    st.text("Choose date after April 12 2021")
    date = st.date_input('Date')
    print("type", type(date))
    print("type", type(start_date))
    process = st.button("Process")
    if process:
        data_from_date(data = data, curring_date=date, start_date=start_date, state= "app_mode")

        st.image("Image.png")
        os.remove("Image.png")

    st.text("Github Link:")


if __name__ == "__main__":
    main()
   