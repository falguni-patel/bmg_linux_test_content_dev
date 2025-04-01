import os

VENV_PATH = "/home/gta/Rendering_apps/render_apps"
VENV_ACTIVATE = os.path.join(VENV_PATH, "bin", "activate")
REQUIREMENTS = ["pyautogui", "opencv-python", "psutil", "pillow"]

MEDIA_VENV_PATH = "/home/gta/Rendering_apps/media_apps"
MEDIA_VENV_ACTIVATE = os.path.join(VENV_PATH, "bin", "activate")
MEDIA_REQUIREMENTS = ["pyautogui", "opencv-python", "psutil", "pillow","selenium","webdriver-manager"]

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

VALLEY_LOG_FILEPATH = "/home/gta/Rendering_apps/Unigine_Valley-1.0/logs"
VALLEY_EXECUTION_SCRIPT = "/home/gta/Rendering_apps/Unigine_Valley-1.0/run_valley_loc.py"
VALLEY_DIR = "/home/gta/Rendering_apps/Unigine_Valley-1.0"
UNIGINE_VALLEY_PATH = "/home/gta/Rendering_apps/Unigine_Valley-1.0/valley" 
VALLEY_RUN_BUTTON_PATH="/home/gta/Rendering_apps/Unigine_Valley-1.0/valley_run_button.png"
KILL_VALLEY_CMD ="sudo pkill browser_x64; sudo pkill valley_x64"

FISHTANK_LOG_FILEPATH = "/home/gta/Media_apps/fishtank/logs"
FISHTANK_EXECUTION_SCRIPT = "/home/gta/Media_apps/fishtank/run_web.py"
FISHTANK_DIR = "/home/gta/Media_apps/fishtank"

VLC_LOG_FILEPATH = "/home/gta/Media_apps/VLC/logs"
VLC_EXECUTION_SCRIPT = "/home/gta/Media_apps/VLC/run_vlc.py"
VLC_DIR = "/home/gta/Media_apps/VLC"


GPUTOP_DIR = "/home/gta/" 
GPUTOP_CMD = "./gputop" 
SLEEP_INTERVAL = 900  
RUN_DURATION = 10 
GPUTOP_RUN_TIME = 10  # Run gputop for 10 seconds
GPUTOP_INTERVAL = 15 * 60  # Run gputop every 15 minutes (converted to seconds)
