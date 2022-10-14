from facebook_scraper import get_posts
from facebook_scraper import *

#Två olika user agent, båda funkar, vet inte om en är bättre än den andra
set_user_agent("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
#set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0")

n=0
for post in get_posts('itklubbv/events', pages=3, credentials=("lukasspam10@gmail.com","d%6D9J^ZqTbG&1op")):
    print(post['post_url'])
#for post in get_posts('itklubbv', pages=3, credentials=("lukasspam10@gmail.com","d%6D9J^ZqTbG&1op")):
#    n += 1
 #   print(f"Post: {n}")
  #  print(post['text'])
   # print(post['post_url'])
    #print()

