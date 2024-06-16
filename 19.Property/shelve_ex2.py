import shelve

# 1. 피드 데이터를 shelve에 저장하기
feeds = [
    {
        'id': 1,
        'title': 'Introduction to Python',
        'description': 'Learn the basics of Python.',
        'tags': ['python', 'beginner']
    },
    {
        'id': 2,
        'title': 'Advanced Python',
        'description': 'Deep dive into advanced Python topics.',
        'tags': ['python', 'advanced']
    }
]

with shelve.open('oscon_feeds.db') as db:
    for feed in feeds:
        db[str(feed['id'])] = feed

# 2. 피드 데이터 구조 변경하기
with shelve.open('oscon_feeds.db', writeback=True) as db:
    for key in db:
        feed = db[key]
        if 'tags' in feed:
            tags = feed.pop('tags')
            feed['tags_list'] = tags
        feed['updated'] = True
        db[key] = feed

    for key in db:
        print(db[key])
'''
{'id': 1, 'title': 'Introduction to Python', 'description': 'Learn the basics of Python.', 'tags_list': ['python', 'beginner'], 'updated': True}
{'id': 2, 'title': 'Advanced Python', 'description': 'Deep dive into advanced Python topics.', 'tags_list': ['python', 'advanced'], 'updated': True}
'''