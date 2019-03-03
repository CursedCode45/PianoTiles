import time
import pyautogui
from PIL import ImageGrab

def imageGrab3():
    third = (908, 275, 909, 865)
    image3 = ImageGrab.grab(bbox=third)

    width, height = image3.size
    for x in range(width):
        for y in reversed(range(height)):
            if image3.getpixel((x, y)) == (17, 17, 17):

                actual_x = x + 907
                actual_y = y + 274

                if actual_y != None:
                    return actual_x, actual_y
                else:
                    break


start = time.time()
while (time.time() - start) < 100:

    firsty = imageGrab3()
    val3 = 0

    if firsty != None:
        val3 = firsty
        pyautogui.click(val3)
        print(val3)
