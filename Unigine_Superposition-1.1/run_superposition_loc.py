
import time
import pyautogui
pyautogui.PAUSE = 0.5 
import subprocess
import os
import signal
import sys
from render_apps_constants import *



os.system(KILL_SUPERPOSITION_CMD)
process = subprocess.Popen([UNIGINE_SUPERPOSITION_PATH])

time.sleep(5)

if len(sys.argv) != 2:
    print("Usage: python script.py <sleep_time_in_seconds>")
    sys.exit(1)
    
sleep_time = int(sys.argv[1])
run_button_location = pyautogui.locateCenterOnScreen(SUPERPOSITION_RUN_BUTTON_PATH, confidence=0.7, grayscale=True)

if run_button_location:
    print(f"Found Run button at {run_button_location}. Clicking...")
    pyautogui.click(run_button_location)
else:
    print("Run button not found! Ensure you have a proper screenshot.")

time.sleep(sleep_time)

print("Closing Unigine Heaven...")
process.terminate()  
time.sleep(2)

os.system(KILL_SUPERPOSITION_CMD)
print("Unigine SUPERPOSITION  benchmark closed.")