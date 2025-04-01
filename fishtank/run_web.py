import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sys



def install_chrome():
    # Install Google Chrome (assuming Ubuntu/Debian)
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "google-chrome-stable"], check=True)
        print("Google Chrome installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing Google Chrome.")
        
def render_website_for_time(url, duration_seconds):
    # Set up Chrome options (no headless mode for GUI)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize the window
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the URL
    driver.get(url)
    
    # Wait for the user-specified time
    print(f"Rendering website for {duration_seconds} seconds...")
    time.sleep(duration_seconds)
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    website_url = "https://webglsamples.org/aquarium/aquarium.html"
    if len(sys.argv) != 2:
      print("Usage: python script.py <execution_time_in_seconds>")
      sys.exit(1)

    duration = int(sys.argv[1])
    
    # Install Chrome if not already installed
    try:
        subprocess.run(["google-chrome-stable", "--version"], check=True)
        print("Google Chrome is already installed.")
    except subprocess.CalledProcessError:
        install_chrome()
    
    # Render the website for the specified duration
    render_website_for_time(website_url, duration)
