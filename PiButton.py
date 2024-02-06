import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED_PIN = 8
BUTTON_PIN = 10

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    button_status = GPIO.input(BUTTON_PIN)
    if button_status == GPIO.LOW:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED when button is pressed
        while GPIO.input(BUTTON_PIN) == GPIO.LOW:
            time.sleep(0.1)  # Wait for button to be released
    else:
        GPIO.output(LED_PIN, GPIO.LOW)