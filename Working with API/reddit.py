import requests

# Authenticating with the API
headers = {'User-Agent': 'Data', 'Authorization': 'Bearer 1077873665170-TuiSLzcO_levnBLabe282wNf49NvvQ'}
response = requests.get('https://oauth.reddit.com/r/kenya/top', headers=headers)

python_top = response.json()

# Getting the Most Upvoted Post
python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes = 0
for article in python_top_articles:
    ar = article["data"]
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]

print(most_upvoted, most_upvotes)

# Getting Post Comments
response = requests.get('https://oauth.reddit.com/r/kenya/comments/137ax7t', headers=headers)
comments = response.json()

# Getting the Most Upvoted Comment
comments_list = comments[1]["data"]["children"]
most_upvoted_comment = ""
most_upvotes_comment = 0
for comment in comments_list:
    co = comment["data"]
    if co["ups"] >= most_upvotes_comment:
        most_upvoted_comment = co["id"]
        most_upvotes_comment = co["ups"]

print(most_upvoted_comment, most_upvotes_comment)

# Upvoting a Comment
payload = {'dir': 0, 'id': '137ax7t'}
response = requests.post('https://oauth.reddit.com/api/vote', headers=headers, json=payload)
print(response.status_code)
