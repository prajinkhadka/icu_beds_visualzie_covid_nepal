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


    
