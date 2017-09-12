#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time
import codecs
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

from mastodon import Mastodon

from random import Random
random=Random()

if(len(sys.argv)<=3):
	sys.stderr.write("Usage: masto_followbot client_token_file user_token_file api_base_url\nSee https://mastodonpy.readthedocs.io/en/latest/ for information about how to create token files\n")
	sys.exit(1)

mastodon=Mastodon(sys.argv[1], access_token=sys.argv[2], api_base_url=sys.argv[3])

followers=[]
creds=mastodon.account_verify_credentials()
my_id=creds["id"]

def get_followers(account_id):
    followers=mastodon.account_followers(account_id)
    f=mastodon.account_followers(account_id, since_id=followers[-1]["id"])
    while(len(f)>0):
        followers.extend(f)
        f=mastodon.account_followers(account_id, since_id=followers[-1]["id"])
    return followers
def get_follower_ids(account_id):
    followers=get_followers(account_id)
    fids=[]
    for item in followers:
        fids.append(item["id"])
    return fids
def get_mentions(account_id, last=None):
    global followers, last_notification
    notifications=mastodon.notifications(since_id=last)
    mentions=[]
    new_follows=False
    for n in notifications:
        if(n.type=="follow"):
            new_follows=True
        elif(n.type=="mention"):
            mentions.append(n)
    if(new_follows):
        new_followers=get_follower_ids(account_id)
        followers=new_followers
    last_notification=notifications[-1]["id"]
    return mentions
def evert_relationships(rdict):
    ids=[]
    for item in rdict:
        ids.append(rdict["id"])
    return ids
def reply_to_mentions(mentions):
    for m in mentions:
        mid=m["id"]
        acct=m["account"]
        acct_id=acct["id"]
        acct_name=acct["acct"]
        relationships=evert_relationships(mastodon.account_relationships(acct_id))
        eligable_followers=[]
        for item in followers:
            if not item in relationships:
                if item!=acct_id:
                    eligable_followers.append(item)
        if(len(eligable_followers)==0):
            mastodon.status_post("@"+acct_name+" There are no users following me who you are not following, followed by, blocking, or muting.", in_reply_to_id=mid, visibility="direct")
        else:
            chosen_follower=random.choice(eligable_followers)
            pretty_name=mastodon.account(chosen_follower)["acct"]
            mastodon.status_post("@"+acct_name+" I recommend following @"+pretty_name, in_reply_to_id=mid, visibility="direct")


followers=get_follower_ids(my_id)
last_notification=None
last_ff=0

while True:
	try:
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
	except Exception as e:
            print(e)
	    pass

