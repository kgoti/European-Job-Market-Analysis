# 🌍 European Job Market Trend Analysis (Data & Analytics Roles)

**Tools:** Python · SQL · Power BI
**Domain:** Labour Market Analytics / HR Analytics
**Level:** Intermediate

---

## 📌 Project Overview

Analyses **21,375 data job postings** across Germany, Austria, and Switzerland (2022–2023), tracking demand, salaries, skills, and hiring trends for data roles.

This project is uniquely positioned — it's directly relevant to the job market you're entering, making it a natural and credible talking point in interviews. Recruiters immediately understand why you built it.

---

## 📁 Repository Structure

```
5_job_market_trends/
│
├── data/
│   ├── job_postings.csv     # 21,375 postings (role, location, salary, skills, mode)
│   └── skills_demand.csv    # 96,063 rows – one row per skill per posting (exploded)
│
├── python/
│   └── generate_data.py     # Dataset generator
│
├── sql/
│   └── analysis_queries.sql # 10 analytical queries
│
└── README.md
```

---

## 📊 What's Analysed

| Analysis                          | Key Question                                          |
|----------------------------------|-------------------------------------------------------|
| Role Demand                      | Which data roles are most in-demand?                  |
| Skill Ranking                    | What are the top skills required per role?            |
| Salary Benchmarks                | What salary can I expect at each experience level?   |
| Work Mode Trends                 | How common is remote / hybrid in data roles?          |
| City-Level Demand                | Which cities hire the most data professionals?        |
| Industry Breakdown               | Which industries need data talent most?               |
| Language Requirements            | How often is German required vs English?              |
| YoY Growth                       | Which roles grew fastest from 2022 to 2023?           |

---

## 🔑 Key Findings

- **Berlin, Munich, Frankfurt** are the top 3 hiring cities for data roles in Germany
- **SQL** is the #1 required skill across all data roles (appears in 85%+ of postings)
- **Power BI** is the dominant BI tool in DACH, far ahead of Tableau
- **Hybrid work** accounts for ~50% of all postings; fully remote ~15%
- **German is required** in ~70% of postings — language learning pays off directly
- **Data Engineers** command the highest salaries; **BI Analysts** have the most postings

---

## 🚀 How to Run

```bash
# Step 1 – Generate datasets
python python/generate_data.py

# Step 2 – Load into MySQL/PostgreSQL and run SQL queries
# Step 3 – Import CSVs into Power BI for dashboard
```

## 💡 Power BI Dashboard Pages

1. **Market Overview** — Total postings, role breakdown, YoY trend
2. **Skill Heatmap** — Top skills by role category
3. **Salary Explorer** — Salary by role, experience level, city (with slicers)
4. **Geography** — Map visual, top hiring cities
5. **Work Mode & Language** — Remote/hybrid trends, German requirement rate

---

*Built as part of a Data & BI Analyst portfolio targeting the German (DACH) job market.*
*Personal motivation: this project was built while actively job searching in Germany.*
