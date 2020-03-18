import time
import json

consumer_key=""
consumer_secret=""
access_key=""
access_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)    
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
a=[]
with open("path/any.txt",'r') as fle:           
            for item in fle:
                try:
                    a=api.retweeters(item)
                    print("Retweeters of " +item)
                    print(a)
                except tweepy.TweepError as ex:
                    if ex.reason == "Sorry, that page does not exist.":
                        with open("path/notexist.txt","a") as fol:
                            fol.write(item) 
                            fol.write("\n")
                            
                if len(a) > 0 and len(a) <=10:
                    with open('path/reaTweet_IDs_having_retweets_counts_1-10.txt','a', encoding='utf8') as fi:
                        fi.write(item)
                        fi.write("\n")
                        with open('path/realRetweeters of tweet %s.txt' %item.strip(),'a', encoding='utf8') as flei:
                            for it in a:
                                flei.write(str(it))
                                flei.write("\n") 
                if len(a) > 10 and len(a) <=20:
                     with open('path/realTweet_IDs_having_retweets_counts_11-20.txt','a', encoding='utf8') as fie:
                        fie.write(item)
                        fie.write("\n")
                        with open('path/realRetweeters of tweet %s.txt' %item.strip(),'a', encoding='utf8') as flei:
                            for it in a:
                                flei.write(str(it))
                                flei.write("\n")
                if len(a) > 20 and len(a) <=30:
                    with open('path/realTweet_IDs_having_retweets_counts_21-30.txt','a', encoding='utf8') as fli:  
                        fli.write(item)
                        fli.write("\n")
                        with open('path/realRetweeters of tweet %s.txt' %item.strip(),'a', encoding='utf8') as flei:
                            for it in a:
                                flei.write(str(it))
                                flei.write("\n")
                if len(a) > 30 and len(a) <=40:
                    with open('path/realTweet_IDs_having_retweets_counts_31-40.txt','a', encoding='utf8') as fli:
                        fli.write(item)
                        fli.write("\n")
                        with open('path/realRetweeters of tweet %s.txt' %item.strip(),'a', encoding='utf8') as flei:
                            for it in a:
                                flei.write(str(it))
                                flei.write("\n")
                if len(a) > 40:
                    with open('path/realTweet_IDs_having_retweets_counts_41_Onwards.txt','a', encoding='utf8') as flie:
                        flie.write(item)
                        flie.write("\n")
                        with open('path/realRetweeters of tweet %s.txt' %item.strip(),'a', encoding='utf8') as flei:
                            for it in a:
                                flei.write(str(it))
                                flei.write("\n")
                a=[]
