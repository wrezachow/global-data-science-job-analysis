from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from seleniumbase import Driver

# Function to handle Infinite Scroll
def scroll(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:  # nothing new loaded — stop
            break

        last_height = new_height

def scrape():
    driver = Driver(uc=True, headless=True)

    driver.get("https://remoteok.com/remote-data-science-jobs")
    time.sleep(6)
    jobs = []

    # Wait for jobs to load
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, "tr[data-company]"))
    scroll(driver)

    
    rows = driver.find_elements(By.CSS_SELECTOR, "tr[data-company]")

    for row in rows:
        job = {
        "title":            row.find_element(By.CSS_SELECTOR, "h2").text if row.find_elements(By.CSS_SELECTOR, "h2") else None,
        "company":          row.get_attribute("data-company"),
        "location":         row.find_element(By.CLASS_NAME, "location").text if row.find_elements(By.CLASS_NAME, "location") else None,
        "work_mode":        "remote",  # remote/hybrid/onsite
        "job_type":         None,  # full-time/internship
        "skills":           [t.text.strip() for t in row.find_elements(By.CSS_SELECTOR, "td.tags a") if t.text.strip()],
        "salary":           None, # Paywalled on RemoteOK
        "date_posted":      row.find_element(By.CSS_SELECTOR, "td.time time").get_attribute("datetime") if row.find_elements(By.CSS_SELECTOR, "td.time time") else None,
        "experience_level": None,  # LLM
        "education":        None,  # LLM
        "source":           "remoteok",  # which site
        "job_url":          "https://remoteok.com" + row.get_attribute("data-href") if row.get_attribute("data-href") else None,
        }
        
        jobs.append(job)

    driver.quit()
    return jobs