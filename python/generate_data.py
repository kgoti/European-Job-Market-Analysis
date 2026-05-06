"""
European Job Market Trend Analysis - Dataset Generator
Simulates job postings data across Germany, Austria, Switzerland
for Data & Analytics roles (2022–2024)
"""

import csv, random
from datetime import datetime, timedelta

random.seed(33)

CITIES = {
    "Germany":     ["Berlin","Munich","Hamburg","Frankfurt","Cologne","Stuttgart","Düsseldorf","Leipzig","Dresden","Nuremberg"],
    "Austria":     ["Vienna","Graz","Linz","Salzburg","Innsbruck"],
    "Switzerland": ["Zurich","Geneva","Basel","Bern","Lausanne"]
}
INDUSTRIES = ["Technology","Finance & Banking","Manufacturing","Healthcare","E-Commerce","Consulting","Automotive","Logistics","Media","Energy"]
JOB_TITLES = {
    "Data Analyst":          ["Data Analyst","Junior Data Analyst","Business Analyst","Reporting Analyst","BI Analyst"],
    "Data Engineer":         ["Data Engineer","ETL Developer","Data Platform Engineer","Pipeline Engineer","Big Data Engineer"],
    "BI Developer":          ["BI Developer","Power BI Developer","Tableau Developer","Reporting Developer","BI Consultant"],
    "Data Scientist":        ["Data Scientist","ML Engineer","AI Analyst","Research Analyst","Quantitative Analyst"],
    "Data Manager":          ["Head of Data","Data Manager","Analytics Manager","BI Manager","Chief Data Officer"]
}
SKILLS_BY_ROLE = {
    "Data Analyst":    ["SQL","Excel","Power BI","Python","Tableau","SAP","Jira","Confluence"],
    "Data Engineer":   ["Python","SQL","Azure","Spark","Databricks","Kafka","Airflow","Docker","dbt"],
    "BI Developer":    ["Power BI","DAX","SQL","Tableau","Excel","SAP BI","SSRS","Looker"],
    "Data Scientist":  ["Python","R","Machine Learning","SQL","TensorFlow","Scikit-Learn","Statistics","Azure ML"],
    "Data Manager":    ["SQL","Power BI","Leadership","Strategy","Agile","Stakeholder Management","Excel"]
}
EXPERIENCE_LEVELS = ["Junior (0-2yr)","Mid (2-5yr)","Senior (5+yr)"]
WORK_MODES = ["On-site","Hybrid","Hybrid","Remote","Hybrid"]
CONTRACT   = ["Permanent","Permanent","Permanent","Fixed-term","Freelance"]
LANGUAGES  = ["German Required","German Required","German Required","English OK","German Required"]
SALARY_RANGES = {
    "Junior (0-2yr)": (32000, 50000),
    "Mid (2-5yr)":    (50000, 75000),
    "Senior (5+yr)":  (75000, 120000)
}

start_date = datetime(2022, 1, 1)
postings = []
posting_id = 1

for day_offset in range(730):  # 2 years
    date = start_date + timedelta(days=day_offset)
    # More postings on weekdays
    if date.weekday() >= 5:
        n = random.randint(3, 15)
    else:
        n = random.randint(15, 60)

    for _ in range(n):
        country  = random.choices(list(CITIES.keys()), weights=[70, 15, 15])[0]
        city     = random.choice(CITIES[country])
        role_cat = random.choice(list(JOB_TITLES.keys()))
        title    = random.choice(JOB_TITLES[role_cat])
        exp      = random.choice(EXPERIENCE_LEVELS)
        skills   = random.sample(SKILLS_BY_ROLE[role_cat], k=random.randint(3, min(6, len(SKILLS_BY_ROLE[role_cat]))))
        sal_min, sal_max = SALARY_RANGES[exp]
        salary_from = random.randint(sal_min, int((sal_min+sal_max)/2))
        salary_to   = random.randint(salary_from, sal_max)
        days_open   = random.randint(7, 90)
        industry    = random.choice(INDUSTRIES)

        postings.append([
            f"JP{posting_id:06d}",
            date.strftime("%Y-%m-%d"),
            country, city, industry,
            role_cat, title, exp,
            random.choice(WORK_MODES),
            random.choice(CONTRACT),
            random.choice(LANGUAGES),
            salary_from, salary_to,
            "|".join(skills),
            days_open
        ])
        posting_id += 1

with open("/home/claude/projects/5_job_market_trends/data/job_postings.csv", "w", newline="") as f:
    csv.writer(f).writerows([[
        "posting_id","date","country","city","industry","role_category","job_title",
        "experience_level","work_mode","contract_type","language_requirement",
        "salary_from","salary_to","skills_required","days_open"
    ]] + postings)
print(f"job_postings.csv → {len(postings)} rows")

# ── 2. skills_demand.csv (exploded skills for analysis) ─────────────────────
skill_rows = []
for p in postings:
    for skill in p[13].split("|"):
        skill_rows.append([p[0], p[1], p[5], p[7], p[2], p[4], skill.strip()])

with open("/home/claude/projects/5_job_market_trends/data/skills_demand.csv", "w", newline="") as f:
    csv.writer(f).writerows([["posting_id","date","role_category","experience_level","country","industry","skill"]] + skill_rows)
print(f"skills_demand.csv → {len(skill_rows)} rows")
print("All datasets generated.")
