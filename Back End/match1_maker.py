def compat(file1,file2):
    import os
    import pandas as pd
    #Equation for finding similarity between two strings out of 1
    #for example: 0.8 score would be 80% similar
    from difflib import SequenceMatcher
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()
    
    #create pd dataframe from json file
    df_person1 = pd.read_json(file1)
    df_person2 = pd.read_json(file2)

    #processing data into dict
    person1 = {}
    for i, value in enumerate(df_person1['Value']):
        person1[i] = value
    person2 = {}
    for i, value in enumerate(df_person2['Value']):
        person2[i] = value

    #turn pd dataframe into list format for easier use
    #this list only has the value in order
    person1_list = []
    person2_list = []
    for i in person1:
        person1_list.append(person1[i])
    for i in person2:
        person2_list.append(person2[i])
    
    #This algo compares the 
    counter = 0
    total = 0
    for a,b in zip(person1_list,person2_list): # zip is used to iterate over two items
        if type(a) != int:
            counter = counter + 1
            total = total + similar(a,b)
        if type(a) == int:
            counter = counter + 1
            dif = abs(a-b)
            if dif > 5:
                total = total
            if dif > 10:
                tota = total - 1
            if dif <= 5 & dif > 0:
                total = total + 1*(1/dif)
            if dif == 0:
                total = total + 1.2
    average = float(total / counter)
    percent = "%d" %(average*100)

    return percent