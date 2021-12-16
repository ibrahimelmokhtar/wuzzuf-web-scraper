from extractInfo import *
from searchQuery import *
from math import ceil


def get_single_page(desired_job, page_number):
    """get soup content from specific url

    Args:
        desired_job (String): the desired job title
        page_number (Int): the number of the current page, starting with 0

    Returns:
        BeautifulSoup Object: contains parsed BeautifulSoup information
    """
    
    # set a search query on "wuzzuf.net":
    job_url = set_searchQuery(desired_job, page_number)
    print(job_url)

    # fetch the obrained URL, then get page content:
    page_content = requests.get(job_url).content

    # parse markup page content using "lxml" parser:
    soup_content = BeautifulSoup(page_content, "lxml")
    
    return soup_content


def fetch_data(desired_job, page_number=0):
    """extract specific data from a soup object created within function

    Args:
        desired_job (String): the desired job title
        page_number (Int): the number of the current page, starting with 0

    Returns:
        tuple: extracted information
    """
    # create empty lists for required data:
    job_titles = list()
    company_names = list()
    company_locations = list()
    posting_dates = list()
    job_types = list()
    career_levels = list()
    years_of_experience = list()
    job_links = list()
    job_requirements = list()
    
    # extract total number of jobs found:
    soup_content = get_single_page(desired_job, page_number)
    total_jobs = extract_totalJobNumber(soup_content)

    # print number of jobs found:
    print("Number of jobs found: {}".format(total_jobs))
    
    # calculate stopping condition and get rounded up integer part:
    total_pages = ceil(total_jobs / 15)
    print("Total number of pages: {}\n".format(total_pages))
    
    # print message for the user:
    print("Start collecting data ...")
    
    # loop through all pages:
    while page_number < total_pages:
        # get soup content for specific page:
        soup_content = get_single_page(desired_job, page_number)
        
        # extract job titles:
        single_page_titles = extract_jobTitles(soup_content)
        for job_title in single_page_titles:
            job_titles.append(job_title)

        # extract company names:
        single_page_companies = extract_companyNames(soup_content)
        for company_name in single_page_companies:
            company_names.append(company_name)


        # extract company locations:
        single_page_locations = extract_companyLocations(soup_content)
        for company_location in single_page_locations:
            company_locations.append(company_location)

        # extract job posting dates:
        single_page_dates = extract_postingDates(soup_content)
        for posting_date in single_page_dates:
            posting_dates.append(posting_date)

        # extract job types:
        single_page_job_types = extract_jobTypes(soup_content)
        for job_type in single_page_job_types:
            job_types.append(job_type)

        # extract career levels:
        single_page_career_levels = extract_careerLevels(soup_content)
        for career_level in single_page_career_levels:
            career_levels.append(career_level)

        # extract years of experience:
        single_page_experiences = extract_yearsOfExperience(soup_content)
        for year in single_page_experiences:
            years_of_experience.append(year)
        
        # extract job links:
        single_page_links = extract_jobLinks(soup_content)
        for job_link in single_page_links:
            job_links.append(job_link)
        
        # extract job requirements:
        # job_requirements.append(extract_jobRequirements(job_links))
        single_page_requirements = extract_jobRequirements(single_page_links)
        for job_requirement in single_page_requirements:
            job_requirements.append(job_requirement)
        
        page_number += 1
    
    return  job_titles, company_names, company_locations, \
            posting_dates, job_types, career_levels, \
                years_of_experience, job_links, job_requirements
            

def wuzzuf_api(desired_job, page_number=0):
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
        posting_dates, job_types, career_levels, \
            years_of_experience, job_links, job_requirements = fetch_data(desired_job, page_number)

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
        data[i]["job_requirements"] = job_requirements[i]
        
    return data