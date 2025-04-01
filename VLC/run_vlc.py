import subprocess
import time
import os
import sys
from datetime import datetime
from multiprocessing import Process
from render_apps_constants import *

VIDEO_PATH = "/home/gta/Media_apps/gats_video/BikeraceSDR_4k60_x264_yuv420_8b_709_27mbps.mkv" 
def play_video_with_vlc(video_path, duration_seconds):
    """Function to run VLC and play a video for the specified duration."""
    vlc_command = [
        "vlc", 
        video_path, 
        "--play-and-exit"  # Play the video and exit after finishing
    ]
    
    try:
       
        vlc_process = subprocess.Popen(vlc_command)
        
        # Wait for the user-defined duration
        print(f"Playing video for {duration_seconds} seconds...")
        time.sleep(duration_seconds)
        
        # Terminate VLC after the specified duration
        vlc_process.terminate()
        print("Video playback finished.")
        
    except Exception as e:
        print(f"Error during video playback: {e}")


if __name__ == "__main__":
    
    if not os.path.exists(VIDEO_PATH):
        print("Error: The video file does not exist. Please check the file path.")
    else:
        if len(sys.argv) != 2:
          print("Usage: python script.py <execution_time_in_seconds>")
          sys.exit(1)
        duration_seconds = int(sys.argv[1])
        
    
        vlc_process = Process(target=play_video_with_vlc, args=(VIDEO_PATH, duration_seconds))
        vlc_process.start()
        vlc_process.join()

        print("VLC  finished.")
