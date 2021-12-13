from checkUserInput import *
from searchQuery import *
from extractInfo import *
import requests
from bs4 import BeautifulSoup

# get disired hob title from the user:
desired_job = input("Enter job title: ")
check_jobTitle(desired_job)

# set a search query on "wuzzuf.net":
job_url = set_searchQuery(desired_job)
print(job_url)

# fetch the obrained URL, then get page content:
page_content = requests.get(job_url).content

# parse markup page content using "lxml" parser:
soup_content = BeautifulSoup(page_content, "lxml")

# extract job titles:
job_titles = extract_jobTitles(soup_content)

# extract company names:
company_names = extract_companyNames(soup_content)

# extract company locations:
company_locations = extract_companyLocations(soup_content)

# extract job posting dates:
posting_dates = extract_postingDates(soup_content)

# extract job types:
job_types = extract_jobTypes(soup_content)

# extract career levels:
career_levels = extract_careerLevels(soup_content)

# extract years of experience:
years_of_experience = extract_yearsOfExperience(soup_content)
