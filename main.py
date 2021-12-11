from check_userInput import *
from searchQuery import *

# get disired hob title from the user:
desired_job = input("Enter job title: ")
check_jobTitle(desired_job)

# set a search query on "wuzzuf.net":
job_url = set_searchQuery(desired_job)
print(job_url)

print("Done!")