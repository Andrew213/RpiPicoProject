import random

from machine import Pin, ADC
from neopixel import myNeopixel
import time


xValue = ADC(28)
yValue = ADC(27)
zValue = Pin(26, Pin.IN, Pin.PULL_UP)


red = 0
green = 0
blue = 0
np = myNeopixel(8,15)
np.brightness(100)

while True:
    xVal = xValue.read_u16()//257

    yVal = yValue.read_u16() // 257
    if zValue.value():
        np.clear()
    if xVal < 250 and xVal > 60 and yVal > 250:
        np.set_pixel(6, random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif  xVal < 120 and xVal < 60 and yVal > 220:
        np.set_pixel(7,  random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif xVal < 10 and yVal <= 250 and yVal > 60:
        np.set_pixel(0,  random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif xVal <= 100 and yVal <= 90:
        np.set_pixel(1,  random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif xVal > 60 and xVal < 250 and yVal == 0:
        np.set_pixel(2,  random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif xVal >= 210 and yVal < 90:
        np.set_pixel(3,  random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif xVal >= 220 and yVal >= 90 and yVal < 250:
        np.set_pixel(4,  random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif xVal >= 250 and yVal >= 220:
        np.set_pixel(5,  random.randint(0,255), random.randint(0,255), random.randint(0,255))
    else:
        np.clear()
    print("x: ", xVal, "y: ", yVal)

    np.show()

    # print("Xva: ", xVal * 255 // 4)
    time.sleep(0.1)
    # xVal = xValue.read_u16()
    # yVal = yValue.read_u16()
    # print("xVal: ", xVal, "yVal: ", yVal)
    #
    # # fooX = xVal // 257
    # # fooY = yVal // 257
    # # if(xVal % 2 == 0):
    # #     print((xVal * 8 + yVal) + 1)
    # # # print('fooX: ', xVal % 2, ", ", "fooY: ", fooY)
    # # # wheel(xVal, yVal)
    # time.sleep(0.1)

# red = 0  # red
# green = 0  # green
# blue = 0  # blue
# np = myNeopixel(8, 15)
# adc0 = ADC(26)
#
#
# def wheel(pos):
#     global red, green, blue
#     WheelPos = pos % 255
#     print("pos ", pos)
#     print("WheelPos", WheelPos)
#     if WheelPos < 85:
#         red = (255 - WheelPos * 3)
#         green = (WheelPos * 3)
#         blue = 0
#     elif WheelPos >= 85 and WheelPos < 170:
#         WheelPos -= 85
#         red = 0
#         green = (255 - WheelPos * 3)
#         blue = (WheelPos * 3)
#     else:
#         WheelPos -= 170
#         red = (WheelPos * 3)
#         green = 0
#         blue = (255 - WheelPos * 3)
#
#
# np.brightness(20)
# while True:
#     adcValue = adc0.read_u16() // 257
#     for j in range(0, 8):
#         wheel(adcValue + j * 255 // 8)
#         np.set_pixel(j, red, green, blue)
#         np.show()
#         time.sleep(0.1)
#     time.sleep_ms(100)