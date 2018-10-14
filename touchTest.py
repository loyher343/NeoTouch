import touchio
import time
import board
import neopixel


pixel_pin = board.EXTERNAL_NEOPIXEL
num_pixels = 30
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)




touch_A5 = touchio.TouchIn(board.A5)
touch_A4 = touchio.TouchIn(board.A4)
touch_A3 = touchio.TouchIn(board.A3)
touch_A2 = touchio.TouchIn(board.A2)




white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
clear = (0,0,0)
while True:
    if touch_A5.value: 
        print("touched!")
        pixels.fill(clear)
        pixels.write()
        time.sleep(0.3)
        pixels.fill(blue)
        pixels.write()
    if touch_A4.value: 
        print("touched!")
        pixels.fill(clear)
        pixels.write()
        time.sleep(0.3)
        pixels.fill(green)
        pixels.write()
    if touch_A3.value: 
        print("touched!")
        pixels.fill(clear)
        pixels.write()
        time.sleep(0.3)
        pixels.fill(red)
        pixels.write()
    if touch_A2.value: 
        print("touched!")
        pixels.fill(clear)
        pixels.write()
        time.sleep(0.3)
        pixels.fill(white)
        pixels.write()
    