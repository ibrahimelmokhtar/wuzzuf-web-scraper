
def extract_jobTitles(soup_content):
    """extract job titles from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted job titles
    """
    
    # find all objects of a specific class:
    job_titles_object = soup_content.find_all("h2", {"class":"css-m604qf"})
    
    # create a list to be returned:
    job_titles = list()
    
    # extract job titles:
    for i in range(len(job_titles_object)):
        job_titles.append(job_titles_object[i].text)
                 
    return job_titles


def extract_companyNames(soup_content):
    """extract company names from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted company names
    """
    
    # find all objects of a specific class:
    company_names_object = soup_content.find_all("a", {"class":"css-17s97q8"})
    
    # create a list to be returned:
    company_names = list()
    
    # format company names:
    # by removing (" -") at the end of each company name
    for i in range(len(company_names_object)):
        company_names.append(company_names_object[i].text.split(" "))
        company_names[i].pop(-1)
        company_names[i] = " ".join(company_names[i])
        
    return company_names


def extract_companyLocations(soup_content):
    """extract company locations from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted company locations
    """
    
    # find all objects of a specific class:
    company_locations_object = soup_content.find_all("span", {"class":"css-5wys0k"})
    
    # create a list to be returned:
    company_locations = list()
    
    # format company locations:
    # by removing (" ") at the end of each company name
    for i in range(len(company_locations_object)):
        company_locations.append(company_locations_object[i].text.strip())
        
    return company_locations
    
    
def extract_postingDates(soup_content):
    """extract job posting dates from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted job posting dates
    """
    
    # create a list to be returned:
    posting_dates = list()
    
    # find all objects of a specific class:
    posting_dates_object = soup_content.find_all("div", {"class":"css-d7j1kk"})
    
    # NOTE: ("css-d7j1kk") is the class name for <div> element which contains:
    #       1. <a> :    for company name
    #       2. <span> : for company location
    #       3. <div> :  for posting date
    
    # NOTE: date has two different classes ... so, I'm trying different solution to obtain posting dates.
    #       the two classes are: ("css-4c4ojb"), and ("css-do6t5g")
    #       and there may be many otehrs! who knows!
    
    # extract job posting dates:
    for object in posting_dates_object:
        posting_dates.append(object.findChildren("div")[0].text)
        
    return posting_dates
    

def extract_jobTypes(soup_content):
    """extract job types from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted job types
    """
    
    # create a list to be returned:
    job_types = list()
    
    # find all objects of a specific class:
    job_types_object = soup_content.find_all("div", {"class":"css-1lh32fc"})
    
    # NOTE: ("css-1lh32fc") is the class name for <div> element which contains:
    #       1. <a> :    for job type ... which in turn contains:
    #           a. <span> : for job type text
    
    # NOTE: each job may have more than one job type.
        
    # extract job types:
    for object in job_types_object:
        # construct single job types list:
        single_job = list()
        for i in range(len(object.findChildren("a"))):
            single_job.append(object.findChildren("a")[i].find("span").text)
        # add single job types list into main job types list:
        job_types.append(single_job)
        
    print(job_types)
    return job_types
