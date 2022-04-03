import RPi.GPIO as GPIO
import time

GPIO.cleanup()


servo_pin_1 = 18
servo_pin_2 = 23
button_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_1, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo_1 = GPIO.PWM(servo_pin_1, 50) # GPIO 17 for PWM with 50Hz
servo_2 = GPIO.PWM(servo_pin_2, 50) # GPIO 17 for PWM with 50Hz

servo_1.start(0)
servo_2.start(11.9)
time.sleep(2)

"""
"Clear": 12,
"Clouds": 10,
"Rain": 8,
"Drizzle": 8,
"Thunderstorm": 5.7,
"Snow": 3.9,
"Mist": 2.4
"""
"""
servo_1.start(4)
servo_2.start(4)
time.sleep(2)

servo_1.start(6)
servo_2.start(6)
time.sleep(2)

servo_1.start(8)
servo_2.start(8)
time.sleep(2)


servo_1.start(10)
servo_2.start(10)
time.sleep(2)


servo_1.start(12.5)
servo_2.start(12.5)
time.sleep(2)


servo_1.start(2)
servo_2.start(2)
time.sleep(2)

servo_1.ChangeDutyCycle(0)
servo_2.ChangeDutyCycle(0)
time.sleep(.4)"""
