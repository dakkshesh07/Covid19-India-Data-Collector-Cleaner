#setting fuction
def covid():
    #importing all packages
    import pandas as pd
    import requests
    import time
    import datetime


    print("Real Time Covid19 Data collector")

    #taking input from user
    name = input("Please Enter Your State (case sensetive)>>> ")
    
    #looping the code
    while True:
        #adding date to a variable
        t = datetime.datetime.now()

        #print info
        print(str(t) + " colecting data " + " Type >> " + name)

        #setting url variable
        url = r'https://api.covid19india.org/csv/latest/state_wise.csv'

        #reading the url for covid data to a pandas dataframe
        df = pd.read_csv(url)
        
        #dropping all uneeded data(cleaning the dataframe)
        df1 = df.drop(columns=['Last_Updated_Time', 'Migrated_Other', 'State_code', 'State_Notes', 'Delta_Deaths', 'Delta_Recovered', 'Delta_Confirmed'])

        #selecting the paricular state from all rows in the dataframe
        df_main = df1[df1['State'] == name]
        
        #writting name of the csv file to a variable
        file = ("data" + name)

        #saving the pandas datafram as a csv file
        df_main.to_csv(file + '.csv')
        
        #printing info
        print(str(t) + " data colected " + " Type >> " + name)

        #setting sleep time to 1 min
        time.sleep(60)
    





