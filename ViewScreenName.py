import json

with open("D:/FYP/newsnet/Politifact/Fake/OtherNews/News-13806/13806.json", 'r',encoding="utf-8-sig") as json_file:
    data = json_file.read()

jsondata=json.loads(data)

for item in jsondata:
    print(item["user"]["screen_name"])
