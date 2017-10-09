#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time
import codecs
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

from mastodon import Mastodon

import dateutil.parser

from random import Random
random=Random()

if(len(sys.argv)<=3):
	sys.stderr.write("Usage: masto_followbot client_token_file user_token_file api_base_url\nSee https://mastodonpy.readthedocs.io/en/latest/ for information about how to create token files\n")
	sys.exit(1)

mastodon=Mastodon(sys.argv[1], access_token=sys.argv[2], api_base_url=sys.argv[3])

followers=[]
creds=mastodon.account_verify_credentials()
my_id=creds["id"]

suggested={}
notification_pool=[]

def stupidDateToEpoch(d):
    try:
      return time.mktime(dateutil.parser.parse(d).timetuple())
    except:
        return time.mktime(d.timetuple())
def get_followers(account_id):
    followers=mastodon.account_followers(account_id)
    #f=mastodon.account_followers(account_id, since_id=followers[-1]["id"])
    #while(len(f)>0):
    #    followers.extend(f)
    #    f=mastodon.account_followers(account_id, since_id=followers[-1]["id"])
    return followers
def get_follower_ids(account_id):
    followers=get_followers(account_id)
    fids=[]
    for item in followers:
        fids.append(item["id"])
    return fids
def get_mentions(account_id, last=None):
    global followers, last_notification, last_update_time
    notifications=mastodon.notifications(since_id=last)
    mentions=[]
    new_follows=False
    ls=0
    for n in notifications:
        if(stupidDateToEpoch(n["created_at"])>last_update_time) and n["id"]>last_notification:
            if "status" in n:
                if stupidDateToEpoch(n["status"]["created_at"])<=last_update_time:
                    next
            if(n["type"]=="follow"):
                new_follows=True
                try:
                    mastodon.notifications_dismiss(n["id"])
                except:
                    pass
            elif(n["type"]=="mention"):
                if(stupidDateToEpoch(n["status"]["created_at"])>=last_update_time):
                    mentions.append(n)
                    #print(n["created_at"])
                    #print(n["status"]["created_at"])
                    if(ls<stupidDateToEpoch(n["status"]["created_at"])):
                        ls=stupidDateToEpoch(n["status"]["created_at"])
            else:
                try:
                    mastodon.notifications_dismiss(n["id"])
                except:
                    pass
    last_update_time=ls
    if(new_follows):
        new_followers=get_follower_ids(account_id)
        followers=new_followers
    if(len(notifications)>0):
        last_notification=notifications[-1]["id"]
    return mentions
def evert_relationships(rdict):
    ids=[]
    for item in rdict:
        ids.append(item["id"])
    return ids
def reply_to_mentions(mentions):
    for m in mentions:
        mid=m["status"]["id"]
        acct=m["account"]
        acct_id=acct["id"]
        acct_name=acct["acct"]
        relationships=evert_relationships(mastodon.account_relationships(acct_id))
        eligable_followers=[]
        for item in followers:
            if not item in relationships:
                if item!=acct_id:
                    if(not acct_id in suggested):
                        suggested[acct_id]=[]
                    if(not item in suggested[acct_id]):
                        eligable_followers.append(item)
                        suggested[acct_id].append(item)
        if(len(eligable_followers)==0):
            mastodon.status_post("@"+acct_name+" There are no users following me who you are not following, followed by, blocking, or muting.", in_reply_to_id=mid, visibility="direct")
            #print("@"+acct_name+" There are no users following me who you are not following, followed by, blocking, or muting.")
        else:
            chosen_follower=random.choice(eligable_followers)
            pretty_name=mastodon.account(chosen_follower)["acct"]
            mastodon.status_post("@"+acct_name+" I recommend following @"+pretty_name, in_reply_to_id=mid, visibility="direct")
            #print("@"+acct_name+" I recommend following @"+pretty_name)
        try:
            mastodon.notifications_dismiss(m["id"])
        except:
            pass
    mastodon.notifications_clear()


followers=get_follower_ids(my_id)
notification_pool=mastodon.notifications()
notification_id_pool=[]
for item in notification_pool:
    notification_id_pool.append(item["id"])
last_notification=0
if(len(notification_pool)>0):
    last_notification=notification_id_pool[-1]
last_ff=0
last_update_time=time.time()
for n in notification_pool:
    if "status" in n:
        l=stupidDateToEpoch(n["status"]["created_at"])
        if(l>last_update_time):
            last_update_time=l
    l=stupidDateToEpoch(n["created_at"])
    if(l>last_update_time):
        last_update_time=l
    try:
        mastodon.notifications_dismiss(n["id"])
    except:
        pass
#mastodon.notifications_clear()
#print(notification_id_pool)
#print(notification_pool[-1])
#
#print(last_update_time)
#print(stupidDateToEpoch(notification_pool[-1]["created_at"]))
#print(time.time())
#
#sys.exit()

while True:
#	try:
        reply_to_mentions(get_mentions(my_id, last_notification))
        if(time.localtime()[6]==4): # if it's friday
            if(last_ff-time.time())>(60*60*2):
                last_ff=time.time()
                samplesize=6
                if(len(followers)<samplesize):
                    samplesize=len(followers)
                chosen_followers=random.sample(followers, samplesize)
                msg=["#ff #followfriday"]
                for f in chosen_followers:
                    msg.append("@"+mastodon.account(f)["acct"])
                mastodon.toot(" \n".join(msg))
        time.sleep(600)
#	except Exception as e:
#            print(e)
#	    pass

