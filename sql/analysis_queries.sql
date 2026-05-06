-- ============================================================
-- Project 5: European Job Market Trend Analysis
-- SQL Analysis Queries
-- ============================================================

-- 1. Job Postings by Role Category (Overall Demand)
SELECT
    role_category,
    COUNT(*)                                               AS total_postings,
    ROUND(COUNT(*)*100.0 / SUM(COUNT(*)) OVER(), 1)       AS market_share_pct,
    ROUND(AVG(salary_from + salary_to) / 2, 0)            AS avg_midpoint_salary,
    ROUND(AVG(days_open), 1)                               AS avg_days_to_fill
FROM job_postings
GROUP BY role_category
ORDER BY total_postings DESC;

-- 2. Monthly Demand Trend by Role
SELECT
    DATE_FORMAT(date, '%Y-%m') AS month,
    role_category,
    COUNT(*)                   AS postings
FROM job_postings
GROUP BY DATE_FORMAT(date, '%Y-%m'), role_category
ORDER BY month, postings DESC;

-- 3. Top In-Demand Skills (Overall)
SELECT
    skill,
    COUNT(*)                                              AS demand_count,
    ROUND(COUNT(*)*100.0 / (SELECT COUNT(*) FROM skills_demand), 2) AS demand_pct
FROM skills_demand
GROUP BY skill
ORDER BY demand_count DESC
LIMIT 20;

-- 4. Top Skills by Role Category
SELECT
    role_category,
    skill,
    COUNT(*) AS mentions,
    RANK() OVER (PARTITION BY role_category ORDER BY COUNT(*) DESC) AS skill_rank
FROM skills_demand
GROUP BY role_category, skill
HAVING skill_rank <= 5
ORDER BY role_category, skill_rank;

-- 5. Salary Benchmarks by Role and Experience
SELECT
    role_category,
    experience_level,
    COUNT(*)                                             AS postings,
    ROUND(AVG(salary_from), 0)                           AS avg_salary_from,
    ROUND(AVG(salary_to), 0)                             AS avg_salary_to,
    ROUND(AVG(salary_from + salary_to)/2, 0)             AS avg_midpoint,
    ROUND(MIN(salary_from), 0)                           AS min_salary,
    ROUND(MAX(salary_to), 0)                             AS max_salary
FROM job_postings
GROUP BY role_category, experience_level
ORDER BY role_category, avg_midpoint DESC;

-- 6. Work Mode Distribution (Remote vs Hybrid vs On-site)
SELECT
    work_mode,
    COUNT(*)                                              AS postings,
    ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(), 1)        AS pct,
    ROUND(AVG(salary_from + salary_to)/2, 0)             AS avg_salary
FROM job_postings
GROUP BY work_mode
ORDER BY postings DESC;

-- 7. City-Level Demand (Top 10 Hiring Cities)
SELECT
    city,
    country,
    COUNT(*)                         AS total_postings,
    ROUND(AVG((salary_from+salary_to)/2), 0) AS avg_salary,
    COUNT(DISTINCT role_category)    AS role_diversity
FROM job_postings
GROUP BY city, country
ORDER BY total_postings DESC
LIMIT 10;

-- 8. Industry Demand for Data Roles
SELECT
    industry,
    COUNT(*)                         AS postings,
    ROUND(AVG((salary_from+salary_to)/2),0) AS avg_salary,
    SUM(CASE WHEN work_mode='Remote' THEN 1 ELSE 0 END)  AS remote_postings,
    ROUND(SUM(CASE WHEN work_mode='Remote' THEN 1 ELSE 0 END)*100.0/COUNT(*),1) AS remote_pct
FROM job_postings
GROUP BY industry
ORDER BY postings DESC;

-- 9. Language Requirement Analysis
SELECT
    language_requirement,
    COUNT(*)            AS postings,
    ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(), 1) AS pct,
    ROUND(AVG((salary_from+salary_to)/2), 0) AS avg_salary
FROM job_postings
GROUP BY language_requirement;

-- 10. Year-over-Year Growth by Role
SELECT
    role_category,
    SUM(CASE WHEN YEAR(date)=2022 THEN 1 ELSE 0 END) AS postings_2022,
    SUM(CASE WHEN YEAR(date)=2023 THEN 1 ELSE 0 END) AS postings_2023,
    ROUND(
        (SUM(CASE WHEN YEAR(date)=2023 THEN 1 ELSE 0 END) -
         SUM(CASE WHEN YEAR(date)=2022 THEN 1 ELSE 0 END)) * 100.0 /
        NULLIF(SUM(CASE WHEN YEAR(date)=2022 THEN 1 ELSE 0 END), 0)
    , 1) AS yoy_growth_pct
FROM job_postings
GROUP BY role_category
ORDER BY yoy_growth_pct DESC;
