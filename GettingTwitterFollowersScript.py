import tweepy
import time 

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit_notify=True,wait_on_rate_limit_notify=True)
    
list_of_followers=[]


f=open("Desktop/test9.txt", "r")
for name in f:
    name = name.strip()  # Strips whitespace characters from start and end (spaces, tabs, newlines etc.)
    
    print("Fetching followers of " + name + " ... ", end="")
    try:
        for page in tweepy.Cursor(api.followers_ids, screen_name=name).pages():
            list_of_followers.extend(page)
            time.sleep(60)
    except tweepy.TweepError as ex:
        if ex.reason == "Not authorized.":
            with open("C:/Users/Mansoor ul Islam/Downloads/New Folder/NotAuthorized.txt","a") as fol:
                fol.write(name) 
                fol.write("\n") 
                continue
                    
    if not list_of_followers:
        with open("C:/Users/Mansoor ul Islam/Downloads/New Folder/NoFollowers.txt","a") as fi:
                fi.write(name) 
                fi.write("\n")
    else:
        with open("C:/Users/Mansoor ul Islam/Downloads/New Folder/%s_Followers.txt" %(name),"w") as fo:
                for followers in list_of_followers:
                    fo.write(str(followers))
                    fo.write("\n")
    
                fo.close()
    print("DONE!") 
    list_of_followers=[]
    
