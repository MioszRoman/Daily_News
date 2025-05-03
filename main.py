import requests
from send_emails import send_email

topic = "apple"
api_key = "4224d33c07df4f80bc495528bff66e70"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-04-"\
      "30&to=2025-04-30&sortBy=popularity&apiKey=4224d33c07df4f80bc495528bff66e70&language=en"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

titles = []
descriptions = []

dicts = {}

body = "Subject: Greetings!" + "\n"

#Access the article titles and description
for article in content['articles'][:15]:
      titles.append(article['title'])
      descriptions.append(article['description'])
      dicts.update({article['title']: article['description']})
      if article['description'] is not None:
            body = body + article['title'] + ':\n' + article['description'] +"\nIf you wanna see, check this link: " + article['url'] + 2 * '\n'

body = body.encode('utf-8')

#Send email with titles, descriptions and links to the article
decision = input("Type if you want to send email: (Y/N) ")
if decision == 'Y' or decision == 'y':
      send_email(message=body)
"""
url_of_image = "https://en.wikipedia.org/wiki/File:Ezio_Auditore_da_Firenze.png"

response = requests.get(url_of_image)

print(response.text)

with open("image.png", "wb") as file:
      file.write(response.content)
      """