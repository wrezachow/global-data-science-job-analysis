import pandas as pd
from scraper.datasciencejobs import scrape as scrape_dsj
from scraper.remoteok import scrape as scrape_remoteok

print("Scraping datasciencejobs...")
dsj_jobs = scrape_dsj()
print(f"{len(dsj_jobs)} jobs collected")

print("Scraping remoteok...")
rok_jobs = scrape_remoteok()
print(f"{len(rok_jobs)} jobs collected")

all_jobs = dsj_jobs + rok_jobs
print(f"\nTotal: {len(all_jobs)} jobs")

df = pd.DataFrame(all_jobs)
df.to_csv("data/raw/scraped_jobs_raw.csv", index=False)
print("Saved")