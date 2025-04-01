import os
import subprocess
import time
import sys
from render_apps_constants import *
from datetime import datetime

# Set the HOME environment variable
os.environ['HOME'] = "/home/gta"

if len(sys.argv) != 3:
    print("Usage: python script.py <execution_time_in_seconds> <video_type>")
    sys.exit(1)

execution_time = int(sys.argv[1])
video_type = sys.argv[2]

os.makedirs(os.path.dirname(FISHTANK_LOG_FILEPATH), exist_ok=True)

# Create venv if not exists
if not os.path.exists(VENV_PATH):
    print("Creating virtual environment...")
    subprocess.run(f"python3 -m venv {MEDIA_VENV_PATH}", shell=True, executable="/bin/bash")

#  Activate venv
print("Activating virtual environment and installing dependencies...")
for pkg in MEDIA_REQUIREMENTS:
    subprocess.run(f"source {MEDIA_VENV_ACTIVATE} && pip install {pkg}", shell=True, executable="/bin/bash")

print("Running Unigine YOUTUBE benchmark...")

YOUTUBE_command = f"export DISPLAY=:0 && cd {YOUTUBE_DIR} && source {MEDIA_VENV_ACTIVATE} && python3 {YOUTUBE_EXECUTION_SCRIPT} {execution_time} {video_type}"
YOUTUBE_process = subprocess.Popen(YOUTUBE_command, shell=True, executable="/bin/bash")


start_time= time.time()
print("start time", start_time)
while time.time() - start_time < execution_time:
    elapsed_time = time.time() - start_time
  
   
    if elapsed_time % GPUTOP_INTERVAL < 1:  # Every 15 minutes
        print("Running gputop for 10 seconds...")

       
        gputop_log_filename = datetime.now().strftime("gputop_log_%Y%m%d_%H%M%S_"+str(execution_time)+"_sec.txt")
        gputop_log_filepath = os.path.join(YOUTUBE_LOG_FILEPATH, gputop_log_filename)

        with open(gputop_log_filepath, "w") as log_file:
            gputop_full_command = f"cd {GPUTOP_DIR} && {GPUTOP_CMD}"
            gputop_process = subprocess.Popen(gputop_full_command, shell=True, executable="/bin/bash", stdout=log_file, stderr=log_file)

            time.sleep(GPUTOP_RUN_TIME)  
            gputop_process.terminate()

            try:
                gputop_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                gputop_process.kill()

        print(f"gputop execution completed. Log saved to {gputop_log_filepath}")

    time.sleep(1)  


YOUTUBE_process.wait()
print("Setup and execution complete!")