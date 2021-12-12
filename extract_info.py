
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
        
    print(company_locations)
    return company_locations
    