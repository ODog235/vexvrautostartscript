import pyautogui
import time
import math
import sys
tryagain = True
time.sleep(3)
path = ""
print("Dir of file: " + "sys.path[0]")
path = sys.path[0]
print(type(pyautogui.locateCenterOnScreen(r''+ path 'tryagainimage.png')))
image_num = int(input("Attempt number to start from:"))
print(pyautogui.locateCenterOnScreen(r''+ path 'tryagainimage.png'))
pyautogui.moveTo(pyautogui.locateCenterOnScreen(r''+ path 'restart.png'))
pyautogui.click()
pyautogui.moveTo(pyautogui.locateCenterOnScreen(r''+ path 'start.png'))
pyautogui.click()
while tryagain:
    if None != pyautogui.locateCenterOnScreen(r''+ path 'tryagainimage.png'):
        print('Found try again button')
        pyautogui.screenshot(imageFilename=r''+ path + str(image_num) + ".PNG")
        image_num += 1
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(r''+ path 'tryagainimage.png'))
        pyautogui.click()
        print("Clicked tryagian")
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(r''+ path 'restart.png'))
        pyautogui.click()
        print("Clicked restart")
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(r''+ path 'start.png'))
        pyautogui.click()
        print("Clicked start")
    print("Not found")
