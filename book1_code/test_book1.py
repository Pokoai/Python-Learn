import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
r.raise_for_status()
response_dict = r.json()

