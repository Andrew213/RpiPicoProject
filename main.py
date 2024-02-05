from machine import Pin, PWM, ADC
import random
from neopixel import myNeopixel
import time
from myservo import Servo

passiveBuzzer = PWM(Pin(15))
passiveBuzzer.duty_u16(0)   # Остановить звук
servo=Servo(10)

servo.ServoAngle(int(180))
def play_buss(freq):
    passiveBuzzer.duty_u16(5000)
    passiveBuzzer.freq(freq)

try:
    xValue = ADC(28)
    yValue = ADC(27)
    zValue = Pin(26, Pin.IN, Pin.PULL_UP)

    red = 0
    green = 0
    blue = 0
    np = myNeopixel(8, 16)
    np.brightness(100)

    while True:


        xVal = xValue.read_u16() // 257

        yVal = yValue.read_u16() // 257

        if zValue.value():
            np.clear()
        if xVal < 250 and xVal > 60 and yVal > 250:
            np.set_pixel(6, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(400)
            servo.ServoAngle(20)
        elif xVal < 120 and xVal < 60 and yVal > 220:
            np.set_pixel(7, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(500)
            servo.ServoAngle(40)
        elif xVal < 10 and yVal <= 250 and yVal > 60:
            np.set_pixel(0, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(600)
            servo.ServoAngle(60)
        elif xVal <= 100 and yVal <= 90:
            np.set_pixel(1, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(700)
            servo.ServoAngle(80)
        elif xVal > 60 and xVal < 250 and yVal == 0:
            np.set_pixel(2, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(800)
            servo.ServoAngle(100)
        elif xVal >= 210 and yVal < 90:
            np.set_pixel(3, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(900)
            servo.ServoAngle(120)
        elif xVal >= 220 and yVal >= 90 and yVal < 250:
            np.set_pixel(4, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(1000)
            servo.ServoAngle(140)
        elif xVal >= 250 and yVal >= 220:
            np.set_pixel(5, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            play_buss(160)
        else:
            np.clear()
            passiveBuzzer.duty_u16(0)

        print("x: ", xVal, "y: ", yVal)

        np.show()

        time.sleep(0.1)
        passiveBuzzer.duty_u16(0)  # Остановить звук

    #     play_melody(mario_melody)
    #     time.sleep(1)  # Пауза между мелодиями

except:
    passiveBuzzer.deinit()




