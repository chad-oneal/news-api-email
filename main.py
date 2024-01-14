import requests

api_key = '3e64369c93c24b128a06292c96e128b6'
url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&category=sports&apiKey="
       "3e64369c93c24b128a06292c96e128b6")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and descriptions
for article in content['articles']:
    print(article['title'])
    print(article['description'])