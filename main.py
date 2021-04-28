import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv("Nepal_ICU_Ventilators - Sheet1 (7).csv")
x = ['ICU_Patients', 'ICU_Total', 'ICU_Occupancy (IN PERCENT)', 'Ventilators_Patients', 'Ventilators_Total', 'Ventilators_Occupancy (IN PERCENT)']
import datetime

# start_date = datetime.datetime(2021, 4, 12)

# print(start_date)

def data_from_date(data, curring_date, start_date, state):
    print("STATE is", state)
    # Caluclating difference from start_date
    differnce  = curring_date - start_date
    print(differnce.days)
    timeline = differnce.days * 7
    print("timeline is", timeline)
    
    print(data['Date'][timeline: timeline+7 ])
    
    
    # Plot 
    if state == "Pradesh-1":
        timeline = timeline
        
    if state == "Pradesh-2":
        timeline = timeline + 1
        
    if state == "Bagmati":
        timeline = timeline + 2
        
    if state == "Gandaki":
        timeline = timeline + 3
        
    if state == "Lumbini":
        print("here")
        timeline = timeline + 4
        print("time line is", timeline)
    if state == "Karnali":
        timeline = timeline + 5
        
    if state == "Sudur-Paschim":
        timeline = timeline + 6
    
        
    fig = plt.figure(figsize=(10, 10))
    y = list(data.iloc[timeline])
    y_plot = y[2:]
    print(y_plot)

    plt.barh(x, y_plot, color='green')
    
    for index, value in enumerate(y_plot):
        print("index", index)
        print("value", value)
        plt.text(value, index, str(value))

    plt.savefig('Image.png',  bbox_inches='tight')

def get_data_hospital_gandaki(hospital_name, date):
    df = pd.read_excel("{}.xlsx".format(date))
    d = df.columns[1]
    df.rename(columns={'Unnamed: 0': "SN", d: 'Hospital', "Unnamed: 2":"Total ICU Bed", "Unnamed: 3":"Occupied ICU Bed", "Unnamed: 4":"Total Ventilator", "Unnamed: 5":"Occupied Ventilator", "Unnamed: 6":"Remarks"}, inplace=True)
    df.drop(0, inplace=True)
    df.drop(1, inplace=True)
    (df.head(2))
    names_of_hospitals = df.Hospital.unique()
    dicts = df.to_dict(orient='records')
    
    for i in range(len((dicts))):
        if dicts[i]["Hospital"] == hospital_name:
            dict_to_return = (dicts[i])
            data_from_hosp = dict_to_return

            
    x = list(data_from_hosp.keys())[2:6]
    title = list(data_from_hosp.values())[1]
    y = list(data_from_hosp.values())[2:6]
    fig = plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.bar(x, y, color='green')
    plt.savefig("Image2.png",  bbox_inches='tight')
    
  
