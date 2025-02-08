from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import utility
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to scrape job details
def scrape_jobs(job_listings):

    job_container = driver.find_element(By.CLASS_NAME, "yKoIdqEjaEMAlNAnskpYewmdzhIJXdCix")
    jobs = job_container.find_elements(By.CSS_SELECTOR, ".ember-view.FumbxwQADHHaZPiZiFZeTShFdCFCNZAaiHLs.occludable-update.p0.relative.scaffold-layout__list-item")
    for job in jobs:
        try:
            lines = job.text.strip().split('\n')
        
            # Extract 1st, 3rd, 4th, and 5th lines if they exist
            job_info = {
                "title": lines[0] if len(lines) > 0 else "",
                "company": lines[2] if len(lines) > 2 else "",
                "location": lines[3] if len(lines) > 3 else "",
                "salary_benefits": lines[4] if len(lines) > 4 else ""
            }
            job_listings.append(job_info)
        except Exception as e:
            print(f"Skipping a job due to error: {e}")
    
    # return job_data

# Setup Driver + Website
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs")
title = driver.title
print(driver.title)

driver.implicitly_wait(0.5)

# Login
username_box = driver.find_element(by=By.NAME, value="session_key")
password_box = driver.find_element(by=By.NAME, value="session_password")
username_box.send_keys("johnhirexe@gmail.com")
password_box.send_keys("=P_9aGiP7St5Ce3H*T$+")
submit_button = driver.find_element(By.CSS_SELECTOR, "button[data-id='sign-in-form__submit-btn']")
submit_button.click()

time.sleep(20)

# Search by role
search_box = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input")
search_box.send_keys("Software Engineer")
search_box.send_keys(Keys.RETURN)

time.sleep(utility.get_stall())

# Specify remote role (version 2)
all_filters = driver.find_element(By.CSS_SELECTOR, ".search-reusables__all-filters-pill-button")
all_filters.click()

# Remote label
time.sleep(utility.get_stall())
remote_label = driver.find_element(By.XPATH, "//label[contains(., 'Remote')]")
driver.execute_script("arguments[0].scrollIntoView(true);", remote_label)
remote_label.click()

# Click apply filters
time.sleep(utility.get_stall())
apply_button = driver.find_element(By.XPATH, "//button[@data-test-reusables-filters-modal-show-results-button='true']")
apply_button.click()


job_listings = []
scrape_jobs(job_listings)

with open('listings.json', 'w') as json_file:
    json.dump(job_listings, json_file, indent=4)

time.sleep(300)

driver.quit()