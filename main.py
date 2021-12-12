from check_userInput import *
from searchQuery import *
from extract_info import *
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