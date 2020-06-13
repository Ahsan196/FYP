import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
import time
import json
import os 
import shutil
#Twitter API credentials
consumer_key=""
consumer_secret=""
access_key=""
access_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=False)

def get_all_followers(fil,userid):
    
    userfollowers = []
    
    try:
        for pages in tweepy.Cursor(api.followers_ids, user_id=userid).pages():
            userfollowers.extend(pages)
    except tweepy.TweepError as ex:
         with open(r"D:/FYP/New folder (23)/Errors1.txt","a") as fol:
            fol.write('%s_%s'% (fil, userid))
            fol.write("\n")
            return

    if not userfollowers:
        return
    else:
        with open(r"D:/FYP/New folder (23)/%s_%s_followers.txt" % (fil,userid) ,'w', encoding='utf-8') as fi:
            for follower in userfollowers:
                fi.write(str(follower))
                fi.write("\n")
        fi.close()
        return
if __name__ == '__main__':
    os.chdir(r"C:\Users\Mansoor ul Islam\Downloads\New Folder (16)")
    done_files = set()
    done_users=set()
for file in os.listdir('.'):
    print("<---file name %s"%(file))
    if file in done_files:
        continue

    done_files.add(file)
    file1=open(file,'r')
    for user in file1:
        if user in done_users:
            continue       
        done_users.add(user)
        user=user.strip()
        file=os.path.splitext(file)[0]+'.txt'
        get_all_followers(file,user)
        
     
    file1.close()
file.close()
