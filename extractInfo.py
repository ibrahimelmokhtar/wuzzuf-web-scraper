from hasNumbers import *    # used with (years of experience) extraction

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
        
    return job_types


def extract_careerLevels(soup_content):
    
    """extract career levels from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted career levels
    """
    
    # create a list to be returned:
    career_levels = list()
    
    # find all objects of a specific class:
    required_years_object = soup_content.find_all("div", {"class":"css-y4udm8"})
    
    # extract career levels:
    for i in range(len(required_years_object)):
        career_levels.append(required_years_object[i].find_all("a", {"class":"css-o171kl"})[0].text)
        
    return career_levels


def extract_yearsOfExperience(soup_content):
    
    """extract years of experience from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted years of experience
    """
    
    # create a list to be returned:
    years_of_experience = list()
    
    # find all objects of a specific class:
    years_of_experience_object = soup_content.find_all("div", {"class":"css-y4udm8"})
    
    # extract years of experience:
    for i in range(len(years_of_experience_object)):
        spanChildren = years_of_experience_object[i].findChildren("span")
        
        # NOTE: years of experience position depends on number of job types:
        #       job types: ("Full Time", "Part Time", "Freelance/Project", ... etc.)
        #       so, loop through its characters to check if there is any digits in it or not
        #       when you find any digit, take that position as years of experience position
        position = 0
        try:
            while not has_numbers(spanChildren[position].text):
                position += 1
            # format years of experience:
            # by removing (". ") at the start, and ("Yrs of Exp") at the end
            # final look (for example): ("0 - 2")
            single_year = spanChildren[position].text.split(" ")
            single_year = " ".join(single_year[1:-3])
        except:
            print("404: (years of experience) NOT FOUND!")
            single_year = ""    # put empty string in its job place
            
        years_of_experience.append(single_year)
        
    return years_of_experience


def extract_jobLinks(soup_content):
    """extract job links from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted job links
    """
    
    # find all objects of a specific class:
    job_links_object = soup_content.find_all("h2", {"class":"css-m604qf"})
    
    # create a list to be returned:
    job_links = list()
    
    # extract job links:
    for i in range(len(job_links_object)):
        # format job link to be re-usable:
        job_link = "https://wuzzuf.net{}".format(job_links_object[i].find("a").attrs["href"])
        job_links.append(job_link)
    
    return job_links

