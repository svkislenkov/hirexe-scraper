import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run headless (no UI)

# Use Service to pass the executable path
service = Service(ChromeDriverManager().install())

# Initialize the undetected Chrome driver
driver = uc.Chrome(service=service, options=options)

# Example: Open a page
driver.get("https://www.linkedin.com/jobs/")
print(driver.title)

# Close the driver after usage
driver.quit()
