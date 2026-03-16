from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase import Driver

import time

def scrape():
    driver = Driver(uc=True, headless=True)

    jobs = []

    for page in range(1, 327): #327
        driver.get(f"https://datasciencejobs.com/jobs/page/{page}/")
        try:
            WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, "job-description-container"))
        except:
            print(f"Skipped page: {page}")
            continue

        rows = driver.find_elements(By.CSS_SELECTOR, ".card-grid-2.hover-up")
        
        for idx, row in enumerate(rows):
            job = {
                "title":            row.find_element(By.TAG_NAME, "h4").text,
                "company":          row.find_element(By.CLASS_NAME, "name-job").text,
                "location":         row.find_element(By.CLASS_NAME, "location-small").text,
                "work_mode":        None, # Handle in cleaning
                "job_type":         row.find_element(By.CLASS_NAME, "mt-5").text,
                "skills":           [s.text.strip() for s in row.find_elements(By.CLASS_NAME, "badge-skill-sm") if s.text.strip()],
                "salary":           row.find_element(By.CLASS_NAME, "card-text-price").text.strip() or None if row.find_elements(By.CLASS_NAME, "card-text-price") else None,
                "date_posted":      None,
                "experience_level": None,   # LLM
                "education":        None,   # LLM
                "source":           "datasciencejobs",
                "job_url":          row.find_element(By.CSS_SELECTOR, "h4 a").get_attribute("href"),
            }
            jobs.append(job)
        time.sleep(0.3)
    driver.quit()
    return jobs