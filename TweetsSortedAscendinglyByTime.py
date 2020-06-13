import json
import pandas as pd
import os
import xlwt 
from xlwt import Workbook 
import xlsxwriter 

with open("D:/FYP/newsnet/Politifact/Fake/OtherNews/News-14376/14376.json",'r',encoding="utf-8-sig") as json_file:
    data = json_file.read()

tweets=json.loads(data)

dict_ = {'user': [],'user_id':[], 'date': []}
for status in tweets:
    dict_['user'].append(status['user']['screen_name'])
    dict_['user_id'].append(status['user']['id'])
    dict_['date'].append(status['created_at'])
            
pd.set_option('display.max_rows', None)
# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='date', inplace=True, ascending=True)
print(df)

df.to_csv(r"D:\FYP\newsnet\Time Based Analysis\14376.csv",index=False)
