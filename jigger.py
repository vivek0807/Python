import pyautogui, sys
import time, random
from pynput.keyboard import Key, Controller
import os
keyboard = Controller()
class WindowsInhibitor:
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    pyautogui.FAILSAFE=False

    def __init__(self):
        pass

    def inhibit(self):
        import ctypes
        print("Preventing Windows from going to sleep")
        ctypes.windll.kernel32.SetThreadExecutionState(
            WindowsInhibitor.ES_CONTINUOUS | \
            WindowsInhibitor.ES_SYSTEM_REQUIRED)

    def uninhibit(self):
        import ctypes
        print("Allowing Windows to go to sleep")
        ctypes.windll.kernel32.SetThreadExecutionState(
            WindowsInhibitor.ES_CONTINUOUS)

print('Determine how many seconds to wait before moving the cursor')
v = input()
print('Press Ctrl-C to quit.')

try:
    if os.name == 'nt':
            osSleep = WindowsInhibitor()
            osSleep.inhibit()
    while True:
        x, y = pyautogui.position()
        time.sleep(int(v))
        a = random.randint(0,1366) # assuming 1920px width
        b = random.randint(0, 768) # assuming 1080px height
        pyautogui.moveTo(a, b, 4)        # 2 is the time in seconds the cursor moves from x,y to a,b
        pyautogui.click(button='right')
        keyboard.press(Key.cmd)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.cmd)
        time.sleep(5)
        keyboard.press(Key.cmd)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.cmd)
        
except KeyboardInterrupt:
    if osSleep:
        osSleep.uninhibit()
    print('\n')
