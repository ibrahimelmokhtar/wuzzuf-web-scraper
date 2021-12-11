
def set_searchQuery(job_title):
    """return a well-constructed search query for wuzzuf.net

    Args:
        job_title (String): the desired job title

    Returns:
        String: well-constructed search query URL for the desired job
    """
    # replace spacing (" ") with special search character ("%20"):
    job_title = job_title.split(" ")    
    job_title = "%20".join(job_title)
    
    # build the search query:
    url_searchQuery = "https://wuzzuf.net/search/jobs/?q={}&a=hpb".format(job_title)
    
    return url_searchQuery