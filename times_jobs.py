import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_jobs(url, max_jobs=10):
    """
    Scrapes job listings from TimesJobs mobile site.
    Returns a pandas DataFrame.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error if request fails
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

    print(f"Status Code: {response.status_code} ✅")

    soup = BeautifulSoup(response.text, 'lxml')
    job_cards = soup.find_all('div', class_='srp-listing')

    data = []

    for i, job in enumerate(job_cards[:max_jobs]):
        try:
            job_title = job.find('h3').text.strip()
            company_name = job.find('span', class_='srp-comp-name').text.strip()
            location = job.find('div', class_='srp-loc').text.strip()
            experience = job.find('div', class_='srp-exp').text.strip()
            salary = job.find('div', class_='srp-sal').text.strip()

            skills_tags = job.find_all('a', class_='srphglt')
            skills = ", ".join([s.text.strip() for s in skills_tags[:3]])

            link_tag = job.find('a', class_='srp-apply-new')
            job_url = link_tag['href'] if link_tag and link_tag['href'].startswith('http') else 'https://m.timesjobs.com' + link_tag['href']

            data.append({
                'Job Title': job_title,
                'Company': company_name,
                'Location': location,
                'Experience': experience,
                'Salary': salary,
                'Skills': skills,
                'Link': job_url
            })

        except Exception as e:
            print(f"Error parsing job {i+1}: {e}")
            continue

    df = pd.DataFrame(data)
    return df

# -------------------------------
# Run the scraper and export data
# -------------------------------

URL = "https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation="

print("Scraping TimesJobs for Python jobs...\n")
jobs_df = fetch_jobs(URL)

if not jobs_df.empty:
    output_file = "timesjobs_python_jobs.xlsx"
    jobs_df.to_excel(output_file, index=False)
    print(f"\n✅ Successfully saved {len(jobs_df)} jobs to '{output_file}'")
    print(jobs_df.head())  # Show sample output
else:
    print("❌ No data to save.")
