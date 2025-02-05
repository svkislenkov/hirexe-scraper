from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.common.by import Keys

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/")


title = driver.title

print(driver.title)

driver.implicitly_wait(0.5)

username_box = driver.find_element(by=By.NAME, value="session_key")
password_box = driver.find_element(by=By.NAME, value="session_password")

username_box.send_keys("johnhirexe@gmail.com")
password_box.send_keys("=P_9aGiP7St5Ce3H*T$+")

# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button = driver.find_element(By.CSS_SELECTOR, "button[data-id='sign-in-form__submit-btn']")
submit_button.click()

time.sleep(180)

driver.quit()