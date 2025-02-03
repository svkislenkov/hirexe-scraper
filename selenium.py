from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening a browser
options.add_argument("--disable-blink-features=AutomationControlled")

# Open the LinkedIn jobs page
driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/")

# Wait for page to load
time.sleep(3)

# Search for remote jobs with a specific title
search_box = driver.find_element(By.CSS_SELECTOR, "input.jobs-search-box__text-input")
search_box.send_keys("Data Scientist")  # Change this to your preferred job title
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# Extract job listings
jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")

job_list = []

for job in jobs:
    try:
        title = job.find_element(By.CLASS_NAME, "job-card-list__title").text
        company = job.find_element(By.CLASS_NAME, "job-card-container__company-name").text
        location = job.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
        salary = "Not listed"  # LinkedIn doesn't always show salary, so it might not be available
        
        job_list.append({
            "title": title,
            "company": company,
            "location": location,
            "salary": salary
        })
    except Exception as e:
        print(f"Skipping job due to error: {e}")

# Save results as JSON
with open("linkedin_jobs.json", "w") as f:
    json.dump(job_list, f, indent=4)

driver.quit()
