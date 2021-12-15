from checkUserInput import *
from saveIntoFile import *
from wuzzufAPI import *

# get disired hob title from the user:
desired_job = input("Enter job title: ")
check_jobTitle(desired_job)

# extract specific data from wuzzuf.net:
data_found = wuzzuf_api(desired_job)

# save found data into .csv file:
save_into_csv(desired_job, data_found)

