#importing all packages
import pandas as pd
import requests
import time
import datetime
import os.path


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
    df_clean = df.drop(columns=['Last_Updated_Time', 'Migrated_Other', 'State_code', 'State_Notes', 'Delta_Deaths', 'Delta_Recovered', 'Delta_Confirmed'])

    #selecting the paricular state from all rows in the dataframe
    df1 = df_clean[df_clean['State'] == name]
        
    #writting name of the csv file to a variable
    file = ("data-" + name)
    
    if os.path.exists(file + '.csv'):
        df2 = pd.read_csv(file + '.csv')
        #Get Confirmed cases value from both old and new dataframes
        confirmed1 = df1.iloc[0]['Confirmed']
        confirmed2 = df2.iloc[0]['Confirmed']
        #Get Recovered cases value from both old and new dataframes
        recovered1 = df1.iloc[0]['Recovered']
        recovered2 = df2.iloc[0]['Recovered']
        #Get Death values from both old and new dataframes
        deaths1 = df1.iloc[0]['Deaths']
        deaths2 = df2.iloc[0]['Deaths']
        #Get Active cases value from both old and new dataframes
        active1 = df1.iloc[0]['Active']
        active2 = df2.iloc[0]['Active']
        #create 2 tuples containing new and old data values
        new_data = (confirmed1, recovered1, deaths1, active1)
        old_data = (confirmed2, recovered2, deaths2, active2)
        #compare both data values
        if (new_data == old_data):
            print("No new changes found in newly fetched data, skipping save")
            print(str(t) + " data save skipped " + " Type >> " + name)
        else:
            print("Data change detected, saving the new data")
            #saving the pandas datafram as a csv file
            df1.to_csv(file + '.csv')
            print(str(t) + " data colected " + " Type >> " + name)

    else:
        print("No old data file found, skipping Value comparison")
        #saving the pandas datafram as a csv file
        df1.to_csv(file + '.csv')
        
        #printing info
        print(str(t) + " data colected " + " Type >> " + name)

    #setting sleep time to 1 min
    time.sleep(60)