import requests

url = "https://cataas.com/cat/says/hello%20world!"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

response = requests.get(url,headers=headers)

print(response)