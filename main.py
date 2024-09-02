import requests
from twilio.rest import Client

my_api_key = "my_api_key"
account_sid = "my_sid"
auth_token = "my_auth"


parameters = {
    "lat": 59.913868,
    "lon": 10.752245,
    "appid": my_api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

bring_umbrella = False

for item in weather_data["list"]:
    weather_id = item["weather"][0]["id"]
    if weather_id < 600:
        bring_umbrella = True
if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='sender_number',
        body="It's going to rain today! Bring an umbrella🫡",
        to='phone_number'
    )

    print(message.status)


