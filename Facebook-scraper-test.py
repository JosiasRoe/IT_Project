from facebook_scraper import get_posts

for post in get_posts('ituppsala', pages=100):
    print(post['text'][:50])

