import json
import requests
import datetime as datetime
import os

token = os.getenv("OPEN_WEATHER_APIKEY", '').lower()
lat = os.getenv("LATITUDE", "19.6069")
lon = os.getenv("LONGITUDE", "-155.5056")

api_request_url_onecall = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={token}&units=metric"


def get_weather_forecast():

    data = requests.get(api_request_url_onecall)
    readable_json = json.loads(data.content)
    print(data.text)

    def print_time(timestamp):
        print(datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S'))
        return

    # https://openweathermap.org/weather-conditions
    # you can use this mapping table to tailor the weather conditions
    # for example, you may consider 10% clouds to be "Clear" and 25% clouds or more to be "Cloudy"...

    def weather_lookup(id):
        if id in range(800, 803):  # we consider below 50% clouds to be "Clear"...
            return "Clear"
        elif id in range(803, 805):
            return "Clouds"
        elif id in range(700, 800):
            return "Mist"
        elif id in range(600, 700):
            return "Snow"
        elif id in range(500, 600):
            return "Rain"
        elif id in range(300, 400):
            return "Rain"
        elif id in range(200, 300):
            return "Thunderstorm"
        else:
            return "Mist"

    #  current time
    print_time(readable_json["current"]["dt"])
    print(readable_json["current"]["weather"][0]["main"])
    print(readable_json["current"]["weather"][0]["id"])
    current_weather = (weather_lookup(readable_json["current"]["weather"][0]["id"]))
    print(current_weather)

    #  3rd hour from now
    print_time(readable_json["hourly"][3]["dt"])
    print(readable_json["hourly"][3]["weather"][0]["main"])
    print(readable_json["hourly"][3]["weather"][0]["id"])
    threehr_weather = weather_lookup(readable_json["hourly"][3]["weather"][0]["id"])
    print(threehr_weather)


    #  6th hour from now
    print_time(readable_json["hourly"][6]["dt"])
    print(readable_json["hourly"][6]["weather"][0]["main"])
    print(readable_json["hourly"][6]["weather"][0]["id"])
    sixhr_weather = weather_lookup(readable_json["hourly"][6]["weather"][0]["id"])
    print(sixhr_weather)

    #  12th hour from now
    print_time(readable_json["hourly"][12]["dt"])
    print(readable_json["hourly"][12]["weather"][0]["main"])
    print(readable_json["hourly"][12]["weather"][0]["id"])
    twelvehr_weather = weather_lookup(readable_json["hourly"][12]["weather"][0]["id"])
    print(twelvehr_weather)

    #  tomorrow at midday
    print_time(readable_json["daily"][1]["dt"])
    print(readable_json["daily"][1]["weather"][0]["main"])
    print(readable_json["daily"][1]["weather"][0]["id"])
    tomorrow_weather = weather_lookup(readable_json["daily"][1]["weather"][0]["id"])
    print(tomorrow_weather)

    #  two days at midday
    print_time(readable_json["daily"][2]["dt"])
    print(readable_json["daily"][2]["weather"][0]["main"])
    print(readable_json["daily"][2]["weather"][0]["id"])
    twodays_weather = weather_lookup(readable_json["daily"][2]["weather"][0]["id"])
    print(twodays_weather)

    weather_list = [current_weather, threehr_weather, sixhr_weather, twelvehr_weather, tomorrow_weather, twodays_weather]
    return weather_list
