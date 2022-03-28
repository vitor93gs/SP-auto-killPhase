#SP KILL PHASE BOT
import pyautogui
import time
pyautogui.click(800,100)
counter = 0
while counter < 200:
    with pyautogui.hold('s'):
        pyautogui.moveTo(348,470,duration = 0.03)
    pyautogui.press('0')
    time.sleep(0.01)
    pyautogui.press(',')
    pyautogui.click(348,470) 
    pyautogui.press('5')
    pyautogui.click(348,470)
    pyautogui.press('4')
    pyautogui.click(348,470)
    time.sleep(4)
    pyautogui.press('.') 
    # pyautogui.press('1')
    # pyautogui.moveTo(282,448,duration=0.1)
    # pyautogui.click(282,448)
    # time.sleep(3.1)
    with pyautogui.hold('w'):
        pyautogui.moveTo(348,470,duration=0.03)
    # pyautogui.press('4')
    # pyautogui.click(348,470)
    # pyautogui.moveTo(414,493,duration=0.1)
    # time.sleep(3)
    pyautogui.press('1')
    pyautogui.click(414,493)
    time.sleep(5.1)
    counter += 1
        