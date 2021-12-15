from checkUserInput import *
from saveIntoFile import *
from searchQuery import *
from wuzzufAPI import *
import requests
from bs4 import BeautifulSoup

# get disired hob title from the user:
desired_job = input("Enter job title: ")
check_jobTitle(desired_job)

# set a search query on "wuzzuf.net":
page_number = 0
job_url = set_searchQuery(desired_job, page_number)
print(job_url)

# fetch the obrained URL, then get page content:
page_content = requests.get(job_url).content

# parse markup page content using "lxml" parser:
soup_content = BeautifulSoup(page_content, "lxml")

# extract total number of jobs found:
total_jobs = extract_totalJobNumber(soup_content)

# extract specific data from wuzzuf.net:
data_found = wuzzuf_api(soup_content)

# save found data into .csv file:
save_into_csv(desired_job, data_found)

# print number of jobs found:
count_found_jobs(data_found)
