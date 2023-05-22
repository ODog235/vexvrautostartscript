import pyautogui
import time
import math
tryagain = True
time.sleep(3)
print(type(pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\tryagainimage.png')))
image_num = int(input("Attempt number to start from:"))
print(pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\tryagainimage.png'))
pyautogui.moveTo(pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\restart.png'))
pyautogui.click()
pyautogui.moveTo(pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\start.png'))
pyautogui.click()
while tryagain:
    if None != pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\tryagainimage.png'):
        print('Found try again button')
        pyautogui.screenshot(imageFilename=r"C:\Users\owenb\Downloads\autostartvexvr\image" + str(image_num) + ".PNG")
        image_num += 1
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\tryagainimage.png'))
        pyautogui.click()
        print("Clicked tryagian")
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\restart.png'))
        pyautogui.click()
        print("Clicked restart")
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(r'C:\Users\owenb\Downloads\autostartvexvr\start.png'))
        pyautogui.click()
        print("Clicked start")
    print("Not found")
