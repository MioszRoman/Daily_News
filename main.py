import requests
from send_emails import send_email

api_key = "4224d33c07df4f80bc495528bff66e70"
url = "https://newsapi.org/v2/everything?q=apple&from=2025-04-"\
      "30&to=2025-04-30&sortBy=popularity&apiKey=4224d33c07df4f80bc495528bff66e70"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

titles = []
descriptions = []

dict = {}


#Access the article titles and description
for article in content['articles']:
      titles.append(article['title'])
      descriptions.append(article['description'])
      dict.update({article['title']: article['description']})


raw_message = f"""
Subject: 5 news from apis

Title: {titles[0]}

Description: {descriptions[0]}

"""
"""
decision = input("Type if you want to send email: (Y/N) ")
if decision == 'Y':
      send_email(raw_message)
"""