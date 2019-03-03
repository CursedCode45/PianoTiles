import time
import pyautogui
from PIL import ImageGrab


def imageGrab():
    first = (1110, 275, 1111, 865)

    image1 = ImageGrab.grab(bbox=first)

    width, height = image1.size
    for x in range(width):
        for y in reversed(range(height)):
            if image1.getpixel((x, y)) == (17, 17, 17):

                actual_x = x + 1109
                actual_y = y + 274

                if actual_y != None:
                    return actual_x, actual_y
                else:
                    break


start = time.time()
while (time.time() - start) < 100:

    firsty = imageGrab()
    val1 = 0
    if firsty != None:
        val1 = firsty
        pyautogui.click(val1)
        print(val1)