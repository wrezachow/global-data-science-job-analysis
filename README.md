## Problem Statement

Comprehensive analytics dashboards analyzing the global data science job market using thousands of job postings collected from multiple job boards. By aggregating and enriching job listings from sources such as datasciencejobs.com and remoteok.com, the project provides insights into hiring trends, required skills, experience expectations, and salary distributions across different roles.

The dashboards provide a wide range of visualizations and metrics, including:

- Bar charts showing the top companies hiring data professionals and the distribution of jobs across different roles.

- Heatmaps comparing skill demand across roles such as Data Scientist, ML Engineer, Data Engineer, and AI Engineer.

- Geographic visualizations displaying the global distribution of data science job postings.

- Charts analyzing the distribution of experience levels required by employers.

- Salary comparisons highlighting average compensation differences between data-related roles.

- Visualizations exploring the demand for major technologies including Python, SQL, AWS, PyTorch, and cloud platforms.

- Programming language and cloud platform demand charts identifying the most frequently requested technologies in job postings.


---
## Dashboards

### Global Data Science Job Market Analysis

![Global Dashboard](dashboard/Global_Dashboard.png)

This dashboard provides a high-level overview of the global data science job market.

Key views include:

- Remote vs onsite job distribution
- Total jobs, companies hiring, and remote job share
- Global job distribution by country
- Experience level demand
- Top hiring companies
- Skill demand by role
- Average salary by role



### Hiring Landscape

![Hiring Landscape](dashboard/Hiring_Landscape.png)

This dashboard focuses on company hiring behavior and job distribution.

Key views include:

- Global distribution of jobs by country
- Remote vs onsite job ratio
- Top hiring companies
- Distribution of jobs by role



### Tech Stack Demand

![Tech Stack Demand](dashboard/Tech_Stack_Demand.png)

This dashboard analyzes the technologies and tools most requested in data science job postings.

Key views include:

- Skill demand by role
- Top 15 most requested technologies
- Cloud platform demand (AWS, Azure, GCP)
- Programming language demand

---
## Live Dashboards
 
| Dashboard | Description |
|-----------|-------------|
| [Global Overview](https://public.tableau.com/app/profile/wasef.chowdhury/viz/GlobalDataScienceJobMarketAnalysis/GlobalDataScienceJobMarketAnalysis) | High-level market overview — remote share, salary by role, experience demand |
| [Hiring Landscape](https://public.tableau.com/app/profile/wasef.chowdhury/viz/GlobalDataScienceJobMarketAnalysis/HiringLandscape) | Company hiring behavior, job distribution by country and role |
| [Tech Stack Demand](https://public.tableau.com/app/profile/wasef.chowdhury/viz/GlobalDataScienceJobMarketAnalysis/TechStackDemand) | Skill demand by role, top technologies, cloud and language trends |
 
 ---
## Tech Stack
 
| Layer | Tools |
|-------|-------|
| Scraping | Python, Selenium, SeleniumBase |
| Data Processing | Pandas, NumPy |
| LLM Enrichment | OpenAI API (gpt-4o-mini) |
| Visualization | Tableau Public, Matplotlib, Seaborn |
| Environment | python-dotenv, tqdm |
 
---
## Getting Started
 
### 1. Clone the repository
 
```bash
git clone https://github.com/wrezachow/global-data-science-job-analysis.git
cd global-data-science-job-analysis
```
 
### 2. Create and activate a virtual environment
 
```bash
python -m venv venv
```
 
**Windows:**
```bash
venv\Scripts\activate
```
 
**Mac / Linux:**
```bash
source venv/bin/activate
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Configure environment variables
 
Create a `.env` file in the project root:
 
```
OPENAI_API_KEY=your_api_key_here
```
 
---
 
## Running the Pipeline
 
### Step 1 — Scrape job postings
 
```bash
python main.py
```
 
Outputs: `data/raw/scraped_jobs_raw.csv`
 
### Step 2 — Clean and transform the data
 
Open and run all cells in:
 
```
data_transform.ipynb
```
 
Handles null values, salary parsing, work mode derivation, deduplication, and skills normalization.

Outputs: `data/clean/clean_jobs.csv`
 
### Step 3 — LLM enrichment
 
Open and run all cells in:
 
```
llm_parse.ipynb
```
 
Uses `gpt-4o-mini` to infer `experience_level` and `education` from job title and skills for all rows.
 
Outputs: `data/clean/filled_jobs.csv`

### Step 4 - EDA

Open and run all cells in:

```
EDA.ipynb
```
 Explores skill frequency, salary distributions, experience level breakdowns, and remote vs onsite trends. Findings feed directly into the Tableau dashboards.

 Outputs: `data/clean/tableau_jobs.csv`

---
 
## Dataset Schema
 
| Field | Description |
|-------|-------------|
| `title` | Job title |
| `company` | Hiring company |
| `location` | Job location |
| `work_mode` | `remote` or `onsite` — derived from location |
| `job_type` | `full-time`, `contract`, etc. |
| `skills` | List of required skills |
| `salary_min` | Minimum salary (USD) |
| `salary_max` | Maximum salary (USD) |
| `salary_avg` | Average of min and max |
| `date_posted` | Posting date |
| `experience_level` | `entry-level`, `mid-level`, `senior`, `lead` — LLM inferred |
| `education` | Degree requirement — LLM inferred |
| `source` | Source job board |
| `job_url` | Direct link to posting |
 
---
 
## Key Findings
 
### Global Overview
- **4,284 jobs** were collected across **1,715 unique companies** the market is highly fragmented with no single employer dominating hiring
- **37% of postings are remote** significantly above the historical pre-pandemic average, reflecting a sustained shift in data science hiring norms
- **Mid-level roles dominate** at 2,500+ postings, followed closely by senior at ~2,400 entry-level and lead roles make up a small minority, signaling a market that rewards prior experience
- **Research Scientists and ML Engineers command the highest salaries**, both averaging above $160K, while Data Engineers and AI Engineers trail slightly behind
 
### Hiring Landscape
- **The United States accounts for the overwhelming majority of postings** the map shows a stark concentration in North America, with Europe a distant second
- **Apple, Amazon, and Microsoft are the top 3 hiring companies** with 118, 111, and 93 postings respectively. Big Tech remains the dominant employer of data professionals
- **Data Scientist is the most posted role by volume**, accounting for the largest share of the jobs-by-role breakdown, ahead of ML Engineer and Data Engineer
- **78.69% of jobs are onsite** despite remote work being common in tech broadly, most data science roles still require physical presence
 
### Tech Stack Demand
- **Python is the undisputed #1 skill** with 230+ mentions across all roles, no other skill comes close, appearing across every role from Data Analyst to Research Scientist
- **AWS leads cloud platforms** with 100+ mentions, nearly 1.5x Azure (65) and over 2x GCP (47) cloud skills are non-negotiable for Data and ML Engineers
- **PyTorch dominates ML frameworks** with 43 mentions in ML Engineer postings alone, outpacing TensorFlow — the industry has converged on PyTorch for deep learning work
- **C++ is uniquely critical for Computer Vision Engineers** (11 mentions), the only role where a systems language ranks in the top skills, reflecting real-time inference requirements
 
---