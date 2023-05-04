# Creating my own Authorization token

import requests

client_id = 'GgXwGCyOSnfd94a1u0GS-A'
client_secret = '8t1Ee73N4U_oEPo2oyxUYTh9RFSXgA'
username = 'whoisorioki'
password = '#D9adrian'
user_agent = 'Data'

auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}
headers = {'User-Agent': user_agent}
response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

if response.status_code == 200:
    # print(response.json())
    access_token = response.json()['access_token']
    headers['Authorization'] = f'Bearer {access_token}'
else:
    print('Authentication failed:', response.json()['message'])

print(headers)

response = requests.get('https://oauth.reddit.com/r/python/about', headers=headers)

if response.status_code == 200:
    subreddit_data = response.json()['data']
    print('Subreddit:', subreddit_data['display_name'])
    print('Subscribers:', subreddit_data['subscribers'])
else:
    print('API request failed:', response.json()['message'])

