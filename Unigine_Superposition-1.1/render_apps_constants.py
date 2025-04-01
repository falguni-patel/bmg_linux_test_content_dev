import os

VENV_PATH = "/home/gta/Rendering_apps/render_apps"
VENV_ACTIVATE = os.path.join(VENV_PATH, "bin", "activate")
REQUIREMENTS = ["pyautogui", "opencv-python", "psutil", "pillow"]

HEAVEN_LOG_FILEPATH = "/home/gta/Rendering_apps/Unigine_Heaven-4.0/logs"
HEAVEN_EXECUTION_SCRIPT = "/home/gta/Rendering_apps/Unigine_Heaven-4.0/run_heaven_loc.py"
HEAVEN_DIR = "/home/gta/Rendering_apps/Unigine_Heaven-4.0"
UNIGINE_PATH = "/home/gta/Rendering_apps/Unigine_Heaven-4.0/heaven" 
HEAVEN_RUN_BUTTON_PATH="/home/gta/Rendering_apps/Unigine_Heaven-4.0/run_button.png"
KILL_HEAVEN_CMD ="sudo pkill browser_x64; sudo pkill heaven_x64"


SUPERPOSITION_LOG_FILEPATH = "/home/gta/Rendering_apps/Unigine_Superposition-1.1/logs"
SUPERPOSITION_EXECUTION_SCRIPT = "/home/gta/Rendering_apps/Unigine_Superposition-1.1/run_superposition_loc.py"
SUPERPOSITION_DIR = "/home/gta/Rendering_apps/Unigine_Superposition-1.1"
UNIGINE_SUPERPOSITION_PATH = "/home/gta/Rendering_apps/Unigine_Superposition-1.1/Superposition" 
SUPERPOSITION_RUN_BUTTON_PATH="/home/gta/Rendering_apps/Unigine_Superposition-1.1/superposition_run_button.png"
KILL_SUPERPOSITION_CMD ="sudo pkill superposition"

GPUTOP_DIR = "/home/gta/" 
GPUTOP_CMD = "./gputop" 
SLEEP_INTERVAL = 900  
RUN_DURATION = 10  
GPUTOP_RUN_TIME = 10  # Run gputop for 10 seconds
GPUTOP_INTERVAL = 15 * 60  # Run gputop every 15 minutes (converted to seconds)
