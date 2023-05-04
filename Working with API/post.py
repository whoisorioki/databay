import requests

# Create a dictionary of headers containing our Authorization header.
headers = {'Authorization': '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'}

# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key,
# there are other optional keys.
payload = {"name": "test"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)

payload = {"name": "learning-about-apis"}
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
status = response.status_code
print(status)
