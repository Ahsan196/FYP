import json
import os
import csv

# Path to folder that contains the News folders (only folder names that start with "News-" are processed)
path = ""

folders = []

for root, dirs, files in os.walk(path, topdown=False):
    folders = dirs

folders = [folder for folder in folders if folder.startswith("News-")]
        
# Python program to convert JSON file to C
#Specify the columns required in csv
keys=["screen_name","created_at","location","verified","followers_count","friends_count","favourites_count","statuses_count","listed_count"]
with open('PathWhereWantToCreateCSVFile/File.csv', 'a', encoding="utf-8-sig") as data_file:
    writer=csv.DictWriter(data_file,fieldnames=keys)
    writer.writeheader()

    for folder in folders:
        serial = folder.replace("News-", "")
        json_file_path = F"{path}\\{folder}\\{serial}.json"
        print(F" -- Processing {serial}.json")
        
        with open(json_file_path, "r", encoding="utf-8-sig") as json_file:
            data = json.load(json_file)
        #For user in each Tweet Object,getting the User Object
        for item in data:
            user= item['user']
            #Reading the row consisting of specifc columns in user as mentioned in keys
            vdata = {key: value for key, value in user.items() if key in keys}
            #Writing row to csv file
            writer.writerow(vdata)

data_file.close()             
