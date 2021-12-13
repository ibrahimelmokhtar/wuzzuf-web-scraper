from checkUserInput import *
from searchQuery import *
from wuzzufAPI import *
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

# extract specific data from wuzzuf.net:
fetch_data(soup_content)