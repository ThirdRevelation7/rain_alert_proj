import requests
import smtplib



api_key = "api_key"
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

my_email = "myemail@email.com"
temp_pass = "mypass"


SEATTLE_LAT = 47.61
SEATTLE_LON = -122.322069

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=temp_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=["someonesemail@email.com"],
            msg="Subject: Weather Update\n\nMake sure to pack an umbrella today, it's going to rain!",
        )


parameters = {
    "lat": SEATTLE_LAT,
    "lon": SEATTLE_LON,
    "appid": api_key,
    "units": "imperial",
    "cnt": 4,

}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for hour_data in weather_data["list"]:
    conditions = hour_data["weather"][0]["id"]
    if conditions < 700:
        will_rain = True

if will_rain:
    send_email()
