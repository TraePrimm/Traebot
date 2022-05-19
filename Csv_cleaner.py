import pandas as pd
import os
import unicodedata
import numpy as np
import re


dirt = "data/csvs/dm/"
file = 'dm.txt'
def clean_csv():


    maindf = pd.DataFrame()

    for file in os.listdir(dirt):
        if file.endswith(".csv"):
            df = pd.read_csv(dirt + file)
            maindf = pd.concat([maindf, df], ignore_index=True)



    maindf = maindf.dropna(subset=['Content'])
    maindf = maindf.dropna(axis=1)
    maindf = maindf.drop(['AuthorID', 'Date'], axis=1)
    maindf = maindf[~maindf.Content.str.contains('http')]
    


    savedir = "data/csvs/clean_dm_csvs/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)


    maindf['Content'].apply(lambda val: unicodedata.normalize('NFKD', val).encode('ascii', 'ignore').decode())

    maindf.to_csv("data/csvs/clean_csvs/dm_nolinks.csv", index=False)



def write_to_file():
    '''
    while running this script it will run into errors with some unicode characters if that is the case search for the unicode error and dlete the offending row
    otherwise if you know unicode strings you can add them to the emoji pattern to delete them automatically

    '''
    maindf = pd.read_csv("data/csvs/clean_csvs/dm_nolinks.csv")
    test = maindf.values.tolist()
    list_for_file = []
    for i in range(len(test)):
        if 'Trae' in test[i][0]: # or 'Trae' in test[i][1]:
            
            emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags=re.UNICODE)
            x = (f"{test[i-1][1]}\t{test[i][1]}")  
            x = emoji_pattern.sub(r'', x)                
            list_for_file.append(x) 

            
    with open(file, 'w') as f:
        for item in list_for_file:
            print(item)
            f.write("%s\n" % item)
    

if __name__ == "__main__":
    #clean_csv()
    write_to_file()
