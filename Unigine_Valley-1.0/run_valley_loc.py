
import time
import pyautogui
pyautogui.PAUSE = 0.5 
pyautogui.FAILSAFE = False
import subprocess
import os
import signal
import sys
from render_apps_constants import *



os.system(KILL_VALLEY_CMD)
process = subprocess.Popen([UNIGINE_VALLEY_PATH])

time.sleep(5)

if len(sys.argv) != 2:
    print("Usage: python script.py <sleep_time_in_seconds>")
    sys.exit(1)
    
sleep_time = int(sys.argv[1])
run_button_location = pyautogui.locateCenterOnScreen(VALLEY_RUN_BUTTON_PATH, confidence=0.6, grayscale=True)

if run_button_location:
    print(f"Found Run button at {run_button_location}. Clicking...")
    time.sleep(1)
    #pyautogui.moveTo(run_button_location, duration=0.5)
    #pyautogui.click()
    pyautogui.click(run_button_location)
else:
    print("Run button not found! Ensure you have a proper screenshot.")

time.sleep(sleep_time)

print("Closing Unigine valley...")
process.terminate()  
time.sleep(2)

os.system(KILL_VALLEY_CMD)
print("Unigine VALLEY  benchmark closed.")