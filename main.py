import requests


api_key = "4224d33c07df4f80bc495528bff66e70"
url = "https://newsapi.org/v2/everything?q=apple&from=2025-04-"\
      "30&to=2025-04-30&sortBy=popularity&apiKey=4224d33c07df4f80bc495528bff66e70"

request = requests.get(url)

content = request.text

print(content)