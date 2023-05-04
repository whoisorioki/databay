import requests
from github import Github

# Create a dictionary of headers containing our Authorization header.
headers = {'Authorization': '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'}

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about whoisorioki.
response = requests.get('https://api.github.com/users/whoisorioki', headers=headers)

# Print the content of the response.  As you can see, this token corresponds to the account of whoisorioki.
print(response.json())

response = requests.get('https://api.github.com/users/whoisorioki/followers', headers=headers)
print(response.json())

response = requests.get('https://api.github.com/users/HarunMbaabu', headers=headers)
print(response.json())

response = requests.get('https://api.github.com/repos/whoisorioki/databay', headers=headers)
print(response.json())

parameters = {'per_page': 10, 'page': 1}
response = requests.get('https://api.github.com/users/whoisorioki/starred', headers=headers, params=parameters)
print(response.json()[2])

response = requests.get('https://api.github.com/user', headers=headers)
user = response.json()
print(user)

# Access token
access_token = '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'

# Create a GitHub instance with your access token
g = Github(access_token)

# Retrieve information about the authenticated user
user = g.get_user()
print(user.name)

