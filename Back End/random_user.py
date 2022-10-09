#!/usr/bin/python
from randomuser import RandomUser
import pandas as pd
import os
import sys
import getopt

def usage():
    print("""

example command line:   

    ./random_user.py

This program generates random users

    """)

r = RandomUser()

numPeople = int(input("How many people would you like to generate? "))

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(numPeople):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

df1 = pd.DataFrame(get_users())  

print('Successfully generated %d' %numPeople)
print('')
print('')
print('')
print(df1.head())

fileName = str(input("Type File Name (do not include .json): "))

df1.to_json('.\people_bank\\%s.json' %fileName)
