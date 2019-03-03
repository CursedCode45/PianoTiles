import time
import pyautogui
from PIL import ImageGrab


def imageGrab4():
    fourth = (803, 275, 804, 865)
    image4 = ImageGrab.grab(bbox=fourth)

    width, height = image4.size
    for x in range(width):
        for y in reversed(range(height)):
            if image4.getpixel((x, y)) == (17, 17, 17):

                actual_x = x + 802
                actual_y = y + 274

                if actual_y != None:
                    return actual_x, actual_y
                else:
                    break


start = time.time()
while (time.time() - start) < 100:

    firsty = imageGrab4()
    val4 = 0

    if firsty != None:
        val4 = firsty
        pyautogui.click(val4)
        print(val4)
