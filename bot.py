#!/usr/bin/python
import praw

user_agent = ("CHSBot 1.0")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("chscomputing")

for submission in subreddit.get_new(limit = 5):
	print "Title: ", submission.title
	print "Text: ", submission.selftext
	print "Score: ", submission.score
	print "Author: ", submission.author
	print "---------------------------------\n
