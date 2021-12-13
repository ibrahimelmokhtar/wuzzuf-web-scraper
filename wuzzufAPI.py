from extractInfo import *

def fetch_data(soup_content):
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

