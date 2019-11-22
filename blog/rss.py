import feedparser



def pull_feed(url):
    NewsFeed = feedparser.parse(url)
    posts = []
    for i in NewsFeed.entries:
        entry = NewsFeed.entries[i]
        author = entry.author
        title = entry.title
        text = entry.summary
        published_date = entry.published
        link = entry.link
        posts.append({
            'author':author,
            'title':title,
            'text':text,
            'published_date':published_date,
            'link':link
        })
    return {'posts':posts}
