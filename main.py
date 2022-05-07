from weather_api import get_weather_forecast

import time
import RPi.GPIO as GPIO
import datetime as datetime
import os

GPIO.cleanup()


servo_pin_1 = os.getenv("SERVO_PIN_1", 18)
servo_pin_2 = os.getenv("SERVO_PIN_2", 23)
button_pin = os.getenv("BUTTON_PIN", 17)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_1, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo_1 = GPIO.PWM(servo_pin_1, 50) # GPIO 17 for PWM with 50Hz
servo_2 = GPIO.PWM(servo_pin_2, 50) # GPIO 17 for PWM with 50Hz

servo_1.start(2)
servo_2.start(12)
time.sleep(0.8)

servo_1.start(12)
servo_2.start(2)
time.sleep(0.8)

servo_1.start(2)
servo_2.start(12)
time.sleep(0.8)

servo_1.start(6)
servo_2.start(6)
time.sleep(0.8)

servo_1.ChangeDutyCycle(0)
servo_2.ChangeDutyCycle(0)
time.sleep(.4)


positions = {"Clear": 11.9,
               "Clouds": 10.1,
               "Rain": 8,
               "Thunderstorm": 5.9,
               "Snow": 3.9,
               "Mist": 2.1,

               "Now": 12,
               "3hr": 10.2,
               "6hr": 8.5,
               "12hr": 6,
               "24hr": 4,
               "48hr": 2.5}

def move_servo(servo_1_position, servo_2_position):
    servo_1_new_position = positions[servo_1_position]
    servo_2_new_position = positions[servo_2_position]
    
    servo_1.ChangeDutyCycle(servo_1_new_position)
    servo_2.ChangeDutyCycle(servo_2_new_position)
    time.sleep(0.5)
    servo_1.ChangeDutyCycle(0)
    servo_2.ChangeDutyCycle(0)
    time.sleep(0.5)

def print_servo(servo, position): #  used for testing only
    new_position = positions[position]
    print(f"Servo: {servo} Position: {new_position}")


class Timer:
    value = 0
    max_value = (10 * 60) * 5

    def __init__(self):
        pass

    def reset(self):
        self.value = 0

    def tick(self):
        refresh = False

        if self.value >= Timer.max_value:
            self.reset()
            refresh = True

        self.value += 1
        time.sleep(0.09)
        return refresh


def weather_toggle(current_weather_displayed):
    if current_weather_displayed >= max_weather_displayable:
        current_weather_displayed = 0
    else:
        current_weather_displayed += 1
    return current_weather_displayed

global last_refreshed_weather
last_refreshed_weather = datetime.datetime.now()
weather_list = get_weather_forecast() 

def refresh_weather_data(current_weather_displayed, weather_list):
    global last_refreshed_weather
    the_time = datetime.datetime.now()
    print(f"last refresh: {last_refreshed_weather} - time now: {the_time}")
    if the_time >= last_refreshed_weather + datetime.timedelta(minutes=20):
        print("getting new weather from API")
        weather_list = get_weather_forecast()
        last_refreshed_weather = the_time
    else:
        print("using old data, no refresh needed")
    weathers = [
        {"time": "Now", "weather": weather_list[0]},
        {"time": "3hr", "weather": weather_list[1]},
        {"time": "6hr", "weather": weather_list[2]},
        {"time": "12hr", "weather": weather_list[3]},
        {"time": "24hr", "weather": weather_list[4]},
        {"time": "48hr", "weather": weather_list[5]}
    ]
    weather_to_display = weathers[current_weather_displayed]
    return weather_to_display, weather_list


def get_input():
    if GPIO.input(button_pin) == GPIO.LOW:
        return True
    else:
        return False


def update_display(weather_to_display):
    print(f"{current_weather_displayed} - {weather_to_display['time']}: {weather_to_display['weather']}")
    print_servo(servo_1, weather_to_display["time"])
    print_servo(servo_2, (weather_to_display["weather"]))
    move_servo((weather_to_display["time"]), (weather_to_display["weather"]))


if __name__ == '__main__':

    current_weather_displayed = 0  # make weather display the current weather the first time
    weather_to_display, weather_list = refresh_weather_data(current_weather_displayed, weather_list)
    update_display(weather_to_display)
    max_weather_displayable = 5
    

    timer = Timer()
    print("Ready")
    while True:

        if get_input() is True:
            timer.reset()
            current_weather_displayed = weather_toggle(current_weather_displayed)
            weather_to_display, weather_list = refresh_weather_data(current_weather_displayed, weather_list)
            update_display(weather_to_display)

        refresh = timer.tick()

        #print(timer.value)
        if refresh is True:
            current_weather_displayed = weather_toggle(current_weather_displayed)
            weather_to_display, weather_list = refresh_weather_data(current_weather_displayed, weather_list)
            update_display(weather_to_display)
