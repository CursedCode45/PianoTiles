import time
import pyautogui
from PIL import ImageGrab


def imageGrab2():
    second = (1013, 275, 1014, 865)
    image2 = ImageGrab.grab(bbox=second)

    width, height = image2.size
    for x in range(width):
        for y in reversed(range(height)):
            if image2.getpixel((x, y)) == (17, 17, 17):

                actual_x = x + 1012
                actual_y = y + 274

                if actual_y != None:
                    return actual_x, actual_y
                else:
                    break


start = time.time()
while (time.time() - start) < 100:

    firsty = imageGrab2()
    val2 = 0
    if firsty != None:
        val2 = firsty
        pyautogui.click(val2)
        print(val2)
