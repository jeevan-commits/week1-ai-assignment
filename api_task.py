import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("🐱 Random Cat Fact")
    print("-------------------")
    print(data["fact"])

else:
    print("Failed to fetch data")