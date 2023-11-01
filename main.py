import requests

api_key = "4261bdc83cd3428a96604d97727d911c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-01&sortBy=publishedAt&apiKey=4261bdc83cd3428a96604d97727d911c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

#print(content)