import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def install_chrome():
    # Install Google Chrome (assuming Ubuntu/Debian)
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "google-chrome-stable"], check=True)
        print("Google Chrome installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing Google Chrome.")
        
def read_credentials():
    # Read Netflix credentials from a txt file
    credentials = {}
    try:
        with open('credentials.txt', 'r') as f:
            for line in f:
                if line.strip():
                    key, value = line.strip().split('=')
                    credentials[key] = value
        return credentials
    except FileNotFoundError:
        print("Credentials file not found!")
        return None

def login_to_netflix(driver, credentials):
    # Open Netflix login page
    driver.get("https://www.netflix.com/login")
    
    # Wait for the username field to be visible before interacting with it
    try:
        user_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id_userLoginId"))
        )
        password_field = driver.find_element(By.ID, "id_password")
        login_button = driver.find_element(By.CLASS_NAME, "btn.login-button")

        # Enter credentials and log in
        user_field.send_keys(credentials['username'])
        password_field.send_keys(credentials['password'])
        login_button.click()

        # Wait for login to complete
        WebDriverWait(driver, 10).until(
            EC.url_changes("https://www.netflix.com/login")
        )
        print("Logged in successfully.")
        
    except Exception as e:
        print("Error during login:", e)

def render_netflix_for_time(url, duration_seconds):
    # Set up Chrome options (no headless mode for GUI)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize the window
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Read credentials from file
    credentials = read_credentials()
    if credentials:
        # Log in to Netflix
        login_to_netflix(driver, credentials)
        
        # Wait for login to complete and navigate to the content
        driver.get(url)
        
        try:
            play_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'button-nfplayerPlay'))
            )
            play_button.click()  # Click to play the video if not auto-playing
            print("Video started playing.")
        except Exception as e:
            print("Could not start video automatically:", e)
        
        # Wait for the user-specified time
        print(f"Rendering Netflix content for {duration_seconds} seconds...")
        time.sleep(duration_seconds)
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    #netflix_url = "https://www.netflix.com/in/title/81227574?trackId=14170286"
    netflix_url= "https://www.netflix.com/watch/81246479?trackId=268410292&tctx=-97%2C-97%2C%2C%2C%2C%2C%2C%2C81227574%2CVideo%3A81246479%2CdetailsPageEpisodePlayButton"
    duration = int(input("Enter duration (in seconds) to render the Netflix content: "))
    
    # Install Chrome if not already installed
    try:
        subprocess.run(["google-chrome-stable", "--version"], check=True)
        print("Google Chrome is already installed.")
    except subprocess.CalledProcessError:
        install_chrome()
    
    # Render the Netflix content for the specified duration
    render_netflix_for_time(netflix_url, duration)
