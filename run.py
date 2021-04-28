import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime, date, time
import os 

from main import data_from_date, get_data_hospital_gandaki
data = pd.read_csv("data/main.csv")
start_date = date(2021, 4, 12)

def main():
    st.sidebar.title("Choose the State")
    app_mode = st.sidebar.selectbox("",
        ["Choose State", "Pradesh-1", "Pradesh-2", "Bagmati", "Gandaki", "Lumbini", "Karnali", "Sudur-Paschim"], key="123")
    
    st.text("Choose date after April 12 2021")
    date = st.date_input('Date')
    print("type", type(date))
    print(date)
    print("type", type(start_date))
    
    if app_mode == "Gandaki":
        st.write("Choose Date after After April 28 ( Included). Since, we only have data from hospitals after April 28")
        hosp_name = st.selectbox("",
        ["Choose Hospital", 'Pachhimanchal Community Hospital', 'Mediplus Hospital',
       'Parkland Hospital', 'Gandaki Medical College',
       'Fewacity Hospital', 'Galaxy Hospital', 'Metrocity Hospital',
       'Kaski sewa Hospital', 'Fishtail Hospital', 'Charak Memorial',
       'Lakecity Hospital', 'Pokhara Academy of Health Science',
       'Manipal Teaching Hospital ',
       'Infectious and Communicable Disease Hospital', 'Namaste Hospital',
       'Dhaulagiri Hospital', 'Madhyabindu Hospital',
       'Parbat District Hospital', 'Gorkha District Hospital',
       'Damauli Hospital', 'Lamjung Community Hospital', 'Beni Hosputal'])



    process = st.button("Process")

    if process:
        if app_mode == "Gandaki":
            get_data_hospital_gandaki(hospital_name=hosp_name, date = str(date))
            st.image("Image2.png")
            os.remove("Image2.png")
        else:
            data_from_date(data = data, curring_date=date, start_date=start_date, state= "app_mode")
            st.image("Image.png")
            os.remove("Image.png")

    st.text("Github Link:")


if __name__ == "__main__":
    main()
   
