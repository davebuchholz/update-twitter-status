#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This twitter bot was created to help prove beginner API and Python usage. This bot must not be used for abuse.
# Guidelines:
#
# Twitter will not tolerate identical tweets. You must have the bot tweet different tweets each time or it will not work.
# If you want to have the bot tweet at a certain account, you must include the twitter account username in the beginning of your tweet.
# This bot is set up to accept a .txt file. If you do not wish to pass a file, you must comment out that code and uncomment the single
# status update portion of code.

import time
import sys
import os
import webbrowser

from twython import Twython
from twython import TwythonStreamer
from twython import TwythonError

#set up our script to input a .txt file. Reminder that argv[0] is this file and therefore we must use index 1.
argfile = str(sys.argv[1])

#taken from Twitter Application Settings page. You must get this information before doing anything else. 
APP_KEY = 'Insert App Key'
APP_SECRET = 'Insert App Secret'

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

print (auth['auth_url'])
#opens up authorization attempt in webpage
webbrowser.open_new(auth['auth_url'])
#webpage should give you a pin AFTER you've authorized it via button click
oauth_verifier = input('Enter your pin:')

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)

FINAL_OAUTH_TOKEN = final_step['oauth_token']
FINAL_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)

print (twitter.verify_credentials())


# below commented out block is useful for single status update tweets.
# For now, it's commented out because we're using command line file input.
#
#
##try:
##    twitter.update_status(status='This is a test!')
##except TwythonError as e:
##    print (e)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

#for each line in the file, tweet the line, then sleep for 60 seconds. Repeat until the file has been completed.
#WARNING: Empty lines in the file will be tweeted. Do not leave blank lines.
for line in f:
    twitter.update_status(status = line)
    time.sleep(60)