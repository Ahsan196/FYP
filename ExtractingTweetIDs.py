import csv
import sys

#news_source = "politifact"
news_source = "gossipcop"

label = "real"
#label = "fake"

class News:

    def __init__(self, info_dict, label, news_platform):
        self.news_id = info_dict["id"]
        self.news_url = info_dict["news_url"]
        self.news_title = info_dict["title"]
        self.tweet_ids =[]
        
        try:
            tweets =  [int(tweet_id) for tweet_id in info_dict["tweet_ids"].split("\t")]
            for item in tweets:
                print(self.news_id,"\t",item)
                
            self.tweet_ids = tweets
        except:
            pass

        self.label = label
        self.platform = news_platform


maxInt = sys.maxsize
while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


news_list = []
with open('path/politifact_real.csv'.format("dataset", news_source,label),mode="r", encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for news in reader:
            news_list.append(News(news, label, news_source))

ids = []
for item in news_list:
    if len(item.tweet_ids) > 0:
        ids.extend(item.tweet_ids)
             
set_ids = set(ids)
ids = list(set_ids)

file = open("path/politifact_real.txt","a")
for idd in ids:
    file.write("%s\n" % idd)
