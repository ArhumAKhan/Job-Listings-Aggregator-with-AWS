# scraper/indeed_scraper.py
# THIS IS ONLY FOR LOCAL USE
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

def collect():
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver (MANUALLY CHANGE PATH FOR LOCAL TESTING)
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

    # Visit Indeed
    driver.get("https://www.indeed.com/jobs?q=Software+Engineer&l=United+States")

    # Wait for the page to load
    time.sleep(3)

    # Grab the page source and pass it to BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()  # URL for Indeed search results for 'Software Engineer' in the US
    return soup


def scrape_indeed_jobs():

    data = collect()

    jobs = []

    # Debugging: Print the number of job elements found
    job_elements = data.find_all('div', class_='jobsearch-SerpJobCard')
    print(f"Found {len(job_elements)} job postings")

    # Find all job postings in the search result
    for job_element in job_elements:
        title_element = job_element.find('h2', class_='title')
        title = title_element.text.strip() if title_element else 'N/A'

        company_element = job_element.find('span', class_='company')
        company = company_element.text.strip() if company_element else 'N/A'

        location_element = job_element.find('div', class_='recJobLoc')
        location = location_element['data-rc-loc'] if location_element else 'N/A'

        jobs.append({
            'title': title,
            'company': company,
            'location': location
        })

    return jobs

if __name__ == "__main__":
    # Test scraping the jobs
    job_listings = scrape_indeed_jobs()
    for job in job_listings:
        print(job['title'], job['company'], job['location'])
