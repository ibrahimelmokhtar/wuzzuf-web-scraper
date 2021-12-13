from extractInfo import *

def fetch_data(soup_content):
    """extract specific data from a given soup object

    Args:
        soup_content (BeautifulSoup object): contains parsed BeautifulSoup information

    Returns:
        tuple: extracted information
    """
    
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
    
    # extract job links:
    job_links = extract_jobLinks(soup_content)
    
    
    return  job_titles, company_names, company_locations, \
            posting_dates, job_types, career_levels, years_of_experience, job_links
            

def wuzzuf_api(soup_content):
    """construct a dictionary with the collected data

    Args:
        soup_content (BeautifulSoup object): contains parsed BeautifulSoup information

    Returns:
        dict: organized, well-formed data
    """
    
    # empty dictionary for the final collected data:
    data = dict()
    
     # desired data to be collected:
    job_titles, company_names, company_locations, \
        posting_dates, job_types, career_levels, years_of_experience, job_links = fetch_data(soup_content)
    
    # construct a dictionary for each job:
    for i in range(len(job_titles)):
        data[i] = dict()
        data[i]["job_title"] = job_titles[i]
        data[i]["company_name"] = company_names[i]
        data[i]["company_location"] = company_locations[i]
        data[i]["posting_date"] = posting_dates[i]
        data[i]["job_types"] = job_types[i]
        data[i]["career_level"] = career_levels[i]
        data[i]["years_of_experience"] = years_of_experience[i]
        data[i]["job_link"] = job_links[i]
        
    return data