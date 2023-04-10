import requests


# define the endpoint of url of my API
url = 'https://lang-detect-app-89.herokuapp.com/predict'

# define the data for posting
data = {'text': 'hello, how are you'}

# send the post request to the API
response = requests.post(url, json = data)

# print the response from the API
print(response.json())