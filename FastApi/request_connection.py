import requests
api_url = "https://pokeapi.co/api/v2/pokemon?limit=100000"
response = requests.get(api_url)
print(response.json())