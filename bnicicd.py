import requests

print("hello world")
print("hello Pria")

response = requests.get("https://www.google.com")

print(response.text)