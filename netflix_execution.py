./from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Configure Edge options
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")  # Open in maximized mode

# Initialize Edge WebDriver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

# Open Netflix Video
video_url = "https://www.netflix.com/in/title/81227574?trackId=14170286"
driver.get(video_url)
