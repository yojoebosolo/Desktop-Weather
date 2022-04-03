import json
import requests
import datetime as datetime

token = ""
lat = ""
lon = ""

api_request_url_onecall = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={token}&units=metric"
#  api_request_url_current = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token}&units=metric" #  not used

def get_weather_forecast():

    data = requests.get(api_request_url_onecall)
    readable_json = json.loads(data.content)
    print(data.text)


    def print_time(timestamp):
        print(datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S'))
        return


    #  current time
    print_time(readable_json["current"]["dt"])
    print(readable_json["current"]["weather"][0]["main"])
    current_weather = readable_json["current"]["weather"][0]["main"]

    #  3rd hour from now
    print_time(readable_json["hourly"][3]["dt"])
    print(readable_json["hourly"][2]["weather"][0]["main"])
    threehr_weather = readable_json["hourly"][2]["weather"][0]["main"]

    #  6th hour from now
    print_time(readable_json["hourly"][6]["dt"])
    print(readable_json["hourly"][5]["weather"][0]["main"])
    sixhr_weather = readable_json["hourly"][5]["weather"][0]["main"]

    #  12th hour from now
    print_time(readable_json["hourly"][12]["dt"])
    print(readable_json["hourly"][11]["weather"][0]["main"])
    twelvehr_weather = readable_json["hourly"][11]["weather"][0]["main"]

    #  tomorrow at midday
    print_time(readable_json["daily"][1]["dt"])
    print(readable_json["daily"][1]["weather"][0]["main"])
    tomorrow_weather = readable_json["daily"][1]["weather"][0]["main"]

    #  two days at midday
    print_time(readable_json["daily"][2]["dt"])
    print(readable_json["daily"][2]["weather"][0]["main"])
    twodays_weather = readable_json["daily"][2]["weather"][0]["main"]

    weather_list = [current_weather, threehr_weather, sixhr_weather, twelvehr_weather, tomorrow_weather, twodays_weather]
    return weather_list
