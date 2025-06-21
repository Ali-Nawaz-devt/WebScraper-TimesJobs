# 🕵️‍♂️ TimesJobs Web Scraper – Python Project

This project is a Python-based web scraper that extracts Python-related job listings from the TimesJobs mobile website. It collects job title, company, skills, experience, location, salary, and job link, and saves the results to an Excel file.

---

## 🔧 Technologies Used

- Python
- BeautifulSoup (bs4)
- Requests
- Pandas
- lxml

---

## ✅ Features

- Extracts job listings from TimesJobs mobile site
- Gathers essential job details
- Handles multiple jobs with error checking
- Outputs data to a structured Excel file
- Easy to customize for other roles or sites

---

## 📊 Extracted Fields

- Job Title  
- Company Name  
- Location  
- Experience Required  
- Salary  
- Required Skills  
- Direct Job Link

---

## 📝 Sample Output

| Job Title         | Company    | Location | Experience | Salary | Skills               | Link     |
|------------------|------------|----------|------------|--------|----------------------|----------|
| Python Developer | ABC Corp   | Mumbai   | 2–5 yrs    | ₹ 6LPA | Python, Django, APIs | [Link]   |

---

## ▶️ How to Run

```bash
# Install required packages
pip install requests beautifulsoup4 pandas lxml

# Run the script
python timesjobs_scraper.py
