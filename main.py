import requests
from send_email import send_email

api_key = '3e64369c93c24b128a06292c96e128b6'
url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&category=sports&apiKey="
       "3e64369c93c24b128a06292c96e128b6")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and descriptions
body = ''
for article in content['articles'][:10]:
    title = article.get('title', 'No Title')
    description = article.get('description', 'No Description')

    if title is None or description is None:
        print("Found an article with None in title or description")
        print("Title:", title)
        print("Description:", description)

    # Skip articles with None in title or description
    if title is not None and description is not None:
        body += title + '\n' + description + '\n' \
                + article['url'] + 2*'\n'

subject = "Today's Sports News"
send_email(subject, body)