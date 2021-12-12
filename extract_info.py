

def extract_companyNames(soup_content):
    """extract company names from a soup object

    Args:
        soup_content (BeautifulSoup Object): contains parsed BeautifulSoup information

    Returns:
        list: extracted company names
    """
    
    # 
    company_names_object = soup_content.find_all("a", {"class":"css-17s97q8"})
    
    # create a list to be returned:
    company_names = list()
    
    # format company names:
    # by removing (" -") at the end of each company name
    for i in range(len(company_names_object)):
        company_names.append(company_names_object[i].text.split(" "))
        company_names[i].pop(-1)
        company_names[i] = " ".join(company_names[i])
        print(company_names[i])
        
    return company_names


