#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:15:21 2019

@author: trejimmy5562
"""

from instapy import InstaPy
from instapy import smart_run
import csv


# login credentials
insta_username = 'USERNAME'
insta_password = 'PASSWORD'
#friendlist = data['friendlist']

#open csv file of banned hashtags and make a table object to hold it
csvfile = open('Book1.csv', 'r')
Table = csv.reader(csvfile)
#we will take the data from the csv and put it into the 'badtags' variable
bad_tags = []

for row in Table:
    print(row[0])
    bad_tags.append(row[0])

bad_tags.append('naked')
bad_tags.append('sex')
bad_tags.append('fight')





#set some crappy auto comments
comments = ['Nice pic! @{}',
        'I love this photo! @{}',
        'looks awesome :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        ':raised_hands: Yes!',
        'Great Post! :raised_hands:',
        'Love it! @{}',
        'Haha love this :raised_hands:',
        'Amazing :raised_hands:',
        'Dope picture @{}',
        'Cool Photo :raised_hands:']

#another way of setting up a session with a proxy - haven't tried this yet
#session = InstaPy(username=insta_username, password=insta_password, proxy_address='8.8.8.8', proxy_port=8080)


# get an InstaPy session
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  disable_image_load=False) #use this to decrease bandwidth if not actively watching

with smart_run(session):
  """ Activity flow """	
  #SET PARAMETERS#
  
  session.set_do_like(enabled=True, percentage=94)
  #This is used to choose which type of account to include based on follower/following ratios
  session.set_relationship_bounds(enabled=True,
                                  potency_ratio=None,
                                  delimit_by_numbers=True,
                                  max_followers=None,
                                  max_following=None,
                                  min_followers=0,
                                  min_following=200,
                                  min_posts=None,
                                  max_posts=None)
  
  #This is supposed to keep you from getting flagged by the algorithm for using a bot
  session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                               peak_likes=(57, 585),
                               peak_comments=(21, 182),
                               peak_follows=(48, None),
                               peak_unfollows=(35, 402),
                               peak_server_calls=(None, 4700))
  
  #List of imported banned tags used to 
  session.set_dont_like(bad_tags)
  # ignore previous friends in commenting and unfollowing (still liked)	
  session.set_dont_include(["friend1", "friend2", "friend3"])
  # Prevents unfollow followers who have liked one of your latest 5 posts
  session.set_dont_unfollow_active_users(enabled=True, posts=5)
  #this sets seconds of sleep between each action by number 
  session.set_action_delays(enabled=True,
                            like=3,
                            comment=5,
                            follow=4.17,
                            unfollow=28)
  #to allow private users
  session.set_skip_users(skip_private=False)
  
  #ACTUAL ACTIVITY#
  #accept your follow requests
  session.accept_follow_requests(amount=100, sleep_delay=2)

  #This likes 75 random posts on your own feed without commenting or following
  ###session.like_by_feed(amount=5, randomize=True, unfollow=False, interact=False)
  #likes the likers of your friends 5 photos
  #session.set_do_follow(enabled=True, percentage=50)
  session.set_ignore_users(['USERS-TO-IGNORE'])
  session.set_do_comment(enabled=False, percentage=10)
  session.set_do_like(enabled=True, percentage=70)
  session.follow_likers(['friend1' , 'friend2'], photos_grab_amount = 5, follow_likers_per_photo = 4, randomize=True, sleep_delay=600, interact=True)
  
  #Unfollows people who do not follow you
  session.unfollow_users(amount=10, InstapyFollowed=(True, "nonfollowers"),
                               style="FIFO",
                               unfollow_after=12 * 60 * 60, sleep_delay=601)
  
  #Clean all followed user - Unfollow all users followed by InstaPy...
  session.unfollow_users(amount=100, InstapyFollowed=(True, "all"),
                               style="FIF      O", unfollow_after=24 * 60 * 60,
                               sleep_delay=601)
  #follow user followers
  session.follow_user_followers(['user1', 'user2', 'user3'], amount=100,
                                  randomize=False, interact=False)
  
  session.set_user_interact(amount=3, percentage=70, randomize=False, media="Photo")
  # also configure [at least] liking to be used while interacting with the commenters ...
  session.set_do_like(enabled=True, percentage=80)
  
  # start the feature
  session.interact_by_comments(['friend1' , 'friend2'], posts_amount=5, comments_per_post=0, reply=False, interact=True, randomize=True, media="Photo")
  
  #session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
  #session.like_by_tags(['natgeo', 'world'], amount=10, interact=True)
  
  #joins an engagement pod, posts your recent picture and interacts with other recent pics of users
  session.set_do_comment(enabled = True, percentage = 60)
  session.set_do_like(enabled=True, percentage=94)
  session.set_do_follow(enabled=True, percentage=70)
  #This sets it to not comment on posts with less than 5 comments
  session.set_delimit_commenting(enabled=True, min=5)
  session.set_comments(comments, media = 'Photo')
  session.join_pods()
