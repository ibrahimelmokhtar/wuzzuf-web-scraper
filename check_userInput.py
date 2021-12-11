from time import sleep      # used for causing a delay

# displayed message while quitting:
QUITTING_MESSAGE = "Invalid job title ... Quitting the program !"

# delay time before quitting the program:
VALIDATION_TIMEOUT = 1


def check_jobTitle(job_title):
    """validate the length of the job title to check the user input.

    Args:
        job_title (String): desired job title entered by the user.
    """
    
    # user input is valid:
    if len(job_title) > 1:
        return
    
    # user input is NOT valid:
    print(QUITTING_MESSAGE)
    sleep(VALIDATION_TIMEOUT)
    quit()