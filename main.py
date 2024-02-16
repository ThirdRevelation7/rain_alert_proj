import requests
import smtplib
import keys


api_key = keys.api_key
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

my_email = keys.my_email
temp_pass = keys.password


NEW_YORK_LAT = 40.71
NEW_YORK_LON = -74.01


def send_email():
    # recipients = ["romero7777777@yahoo.com", "christian7.crunch@gmail.com"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=temp_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=[my_email],#pops phone
            msg="Make sure to pack an umbrella today, it's going to rain!",
        )


parameters = {
    "lat": NEW_YORK_LAT,
    "lon": NEW_YORK_LON,
    "appid": api_key,
    "units": "imperial",
    "cnt": 4,

}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

# weather_next_12hrs = [weather_data["list"][n]["weather"][0]['id'] for n in range(4)]
for hour_data in weather_data["list"]:
    conditions = hour_data["weather"][0]["id"]
    if conditions < 700:
        will_rain = True

if will_rain:
    send_email()

    # Test code
    print("there be rain")
