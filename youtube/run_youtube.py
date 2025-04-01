import time
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def install_chrome():
    # Install Google Chrome (assuming Ubuntu/Debian)
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "google-chrome-stable"], check=True)
        print("Google Chrome installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing Google Chrome.")
        

def handle_playback(driver):
    # Check and click the Play button if the video isn't playing automatically
    try:
        # Wait for the play button to appear and click it if necessary
        play_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "play-pause-button"))
        )
        play_button.click()
        print("Video started playing.")
    except Exception as e:
        print("Error in playback:", e)
        
    
    try:


        driver.switch_to.frame(iframe)
        play_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ytp-play-button"))
        )
        play_button.click()
        print("Video started playing (ytp-play-button).")
    except Exception as e:
        print("Error in playback (ytp-play-button):", e)
    
    
    try:
            play_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ytp-large-play-button"))
            )
            play_button.click()
            print("Video started playing (ytp-large-play-button).")
    except Exception as e:
            print("Error in playback (ytp-large-play-button):", e)


    # Handle the "Skip Ad" button if it appears
    try:
        skip_ad_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ytp-skip-ad-button"))
        )
        skip_ad_button.click()
        print("Ad skipped.")
    except Exception as e:
        print("No 'Skip Ad' button found.")


def render_youtube_video(url, duration_seconds):
    # Set up Chrome options (no headless mode for GUI)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize the window
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    #  WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    
    driver.get(url)
    
    
    handle_playback(driver)
        
   
    print(f"Rendering YouTube video for {duration_seconds} seconds...")
    time.sleep(duration_seconds)
    
    
    driver.quit()

def get_video_url_based_on_type(video_type):
    # YouTube Music URL
    if video_type == "music":
        return "https://music.youtube.com/watch?v=YALvuUpY_b0&list=RDAMVMYALvuUpY_b0"
    
    # VP9 Chrome URL
    elif video_type == "vp9_chrome":
        return "https://www.youtube.com/embed/WW2DKBGCvEs?rel=0&loop=1&playlist=WW2DKBGCvEs&autoplay=1"
    
    # AV1 Chrome URL
    elif video_type == "av1_chrome":
        return "https://www.youtube.com/watch?v=k2qgadSvNyU&list=PLyqf6gJt7KuHBmeVzZteZUlNUQAVLwrZS"
    
    else:
        print("Invalid video type.")
        return None

def main():
    if len(sys.argv) != 3:
      print("Usage: python script.py <execution_time_in_seconds> <video_type>")
      sys.exit(1)
   
    execution_time = int(sys.argv[1])  # Execution time in seconds
    video_type = sys.argv[2]  # wl name (second argument)
    
    
    url = get_video_url_based_on_type(video_type)
    
    if url:
      render_youtube_video(url, execution_time)

if __name__ == "__main__":
    main()
