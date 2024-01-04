import requests
import send_email
topic = "apple"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      f"from=" \
      "2024-01-03&to=2024-01-03&sortBy=popularity&" \
      "apiKey=4f65aa8eb71a4e41addacb98972b55db&" \
      "language=en"
api_key = "4f65aa8eb71a4e41addacb98972b55db"

#Make Request
print("requestisng url. Wait!!")
request = requests.get(url)
print("requestisng url. Done!!")

#Get Json
content = request.json()
message =""
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = "Subject: TodaysNew" + "\n" \
                      +message + "TITLE" + '\n'+ article["title"] + '\n' \
                      + "DESCRIPTION" + '\n'+ article["description"] + '\n'\
                      + "" + '\n' + '\n'

print("Sending Mail !!")

send_email.send_email(message)
print("Sending  Mail  Done!!")


print(type(content))
