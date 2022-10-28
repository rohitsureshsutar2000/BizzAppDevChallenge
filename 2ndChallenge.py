"""program to read the CSV file"""
import csv

import pandas as pd
import re
from datetime import date

def Calcu(New):
    x=date.today()
    todayDate=re.split('-',str(x))

    return (int(todayDate[0])-int(New[2]))   # calculate age


def read_file():
    df=pd.read_csv('2ndChallenge.csv')
    x=df['DOB']
    person=df['Name']

    for i in range(0,len(x)):
        new=re.split('-',x[i])
        age=Calcu(new)                      # send Date of Birth for Calculate age
        print(person[i],' Age is:- ',age)


with open('2ndChallenge.csv','a')as f:
   data=csv.writer(f)                        # Write Date in csv File
   Name=input("Enter name:-")
   Dob=input("Enter DOB:-")
   Salary=input("Enter Salary:-")
   data.writerow([Name,Dob,Salary])
   f.close()
   read_file()


