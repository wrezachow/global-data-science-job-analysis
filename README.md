## Problem Statement

Comprehensive analytics dashboards analyzing the global data science job market using thousands of job postings collected from multiple job boards. By aggregating and enriching job listings from sources such as datasciencejobs.com and remoteok.com, the project provides insights into hiring trends, required skills, experience expectations, and salary distributions across different roles.

The dashboards provide a wide range of visualizations and metrics, including:

Bar charts showing the top companies hiring data professionals and the distribution of jobs across different roles.

Heatmaps comparing skill demand across roles such as Data Scientist, ML Engineer, Data Engineer, and AI Engineer.

Geographic visualizations displaying the global distribution of data science job postings.

Charts analyzing the distribution of experience levels required by employers.

Salary comparisons highlighting average compensation differences between data-related roles.

Visualizations exploring the demand for major technologies including Python, SQL, AWS, PyTorch, and cloud platforms.

Programming language and cloud platform demand charts identifying the most frequently requested technologies in job postings.

Here are the links to the Tableau public dashboards:

Global Data Science Job Market Analysis

Tech Stack Demand

Hiring Landscape

## Dashboards

This project includes three interactive Tableau dashboards exploring different aspects of the data science job market.


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

View the live dashboard:

https://public.tableau.com/app/profile/wasef.chowdhury/viz/GlobalDataScienceJobMarketAnalysis/GlobalDataScienceJobMarketAnalysis



### Hiring Landscape

![Hiring Landscape](dashboard/Hiring_Landscape.png)

This dashboard focuses on company hiring behavior and job distribution.

Key views include:

- Global distribution of jobs by country
- Remote vs onsite job ratio
- Top hiring companies
- Distribution of jobs by role


View the live dashboard:

https://public.tableau.com/app/profile/wasef.chowdhury/viz/GlobalDataScienceJobMarketAnalysis/HiringLandscape



### Tech Stack Demand

![Tech Stack Demand](dashboard/Tech_Stack_Demand.png)

This dashboard analyzes the technologies and tools most requested in data science job postings.

Key views include:

- Skill demand by role
- Top 15 most requested technologies
- Cloud platform demand (AWS, Azure, GCP)
- Programming language demand


View the live dashboard:

https://public.tableau.com/app/profile/wasef.chowdhury/viz/GlobalDataScienceJobMarketAnalysis/TechStackDemand

## Installation

Clone the repository:

git clone https://github.com/yourusername/Job_Analytics.git

cd Job_Analytics


Create a virtual environment:

`python -m venv venv`


Activate the virtual environment.

Windows:

`venv\Scripts\activate`

Mac / Linux:

`source venv/bin/activate`


Install dependencies:

`pip install -r requirements.txt`

## Running the Project

Run the scraper to collect job postings:

`python main.py`


This will create the raw dataset containing job listings.


Process and clean the data using the notebooks:

`data_transform.ipynb`


Run the LLM parsing notebook to extract additional fields such as experience level and education requirements:

`llm_parse.ipynb`

This step requires an OpenAI API key.

Create a `.env` file in the project root and add:

`OPENAI_API_KEY=your_api_key_here`

The notebook will load the API key from the `.env` file using `python-dotenv`.


The final dataset used for analytics will be generated:

`data/tableau_jobs.csv`