
def set_searchQuery(job_title, page_number):
    """return a well-constructed search query for wuzzuf.net

    Args:
        job_title (String): the desired job title
        page_number (Int): the number of the current page, starting with 0

    Returns:
        String: well-constructed search query URL for the desired job
    """
    # replace spacing (" ") with special search character ("%20"):
    job_title = job_title.split(" ")    
    job_title = "%20".join(job_title)
    
    # build the search query:
    url_searchQuery = "https://wuzzuf.net/search/jobs/?a=hpb&q={}&start={}".format(job_title, page_number)
    
    return url_searchQuery