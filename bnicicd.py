import requests
from datetime import datetime

print("hello world")
print("hello Pria")

response = requests.get("https://www.google.com")

# print(response.text)

waktu = datetime.now()
with open("tempResponse/" + str(waktu) + ".txt" , "w") as f:
    f.write(response.txt)