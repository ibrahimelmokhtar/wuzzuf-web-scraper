from datetime import datetime
import csv
import os

def create_directory(file_type):
    """create directory to save created files into it depending on file types (.csv, .txt, ... ect.)

    Args:
        file_type (String): desired file type (for example: csv, txt, ... etc.)
    """
    
    # get the directory of this script:
    base_directory = os.path.dirname(__file__)
    
    # format the name of the path to be created:
    directory_path = r'{}\\{}'.format(base_directory, file_type)
    
    # create directory if it does NOT exist:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
   

def format_file_name(desired_job, file_type):
    """format file name without file extension (for example: ".txt", ".csv", ... etc.)

    Args:
        desired_job (String): the job you searched for
        file_type (String): desired file type (for example: csv, txt, ... etc.)

    Returns:
        String: constructed file path
    """
    
    # format file name using current date and time:
    date_now = str(datetime.now()).split(":")
    date_now = "-".join(date_now)
    
    file_name = str("{} {}".format(date_now, desired_job))
    print("Saving into file: {}".format(file_name))
    
    # get the directory of this script:
    base_directory = os.path.dirname(__file__)
    
    # format the name of the path to be created:
    file_path = r'{}\\{}\\{}'.format(base_directory, file_type, file_name)
    
    return file_path


def count_found_jobs(data_found):
    """count jobs found on wuzzuf.net for specific keyword

    Args:
        data_found (dict): constructed dictionary contains found data on wuzzuf.net
    """
    # get jobs' number:
    count = len(data_found.keys())
    
    # print message:
    print("Number of jobs found: {}".format(count))


def save_into_csv(desired_job, data_found):
    """save given data into .csv file

    Args:
        desired_job (String): the job you searched for
        data_found (Dict): constructed dict contains found data
    """
    
    # create a directory if it does NOT exist:
    file_type = "csv"
    create_directory(file_type)
    
    # construct file name:
    file_path = format_file_name(desired_job, file_type) + ".csv"
        
    with open(file_path, 'w', encoding="utf-8") as csv_file:
        # create csv writer object:
        csv_writer = csv.writer(csv_file)
        
        # write header names:
        csv_writer.writerow(["Job Title", "Company Name", "Company Location", "Posting Date", \
                            "Job Types", "Career Level", "Years of Experience", \
                            "Job Link", "Job Requirements"])
        
        # start writting details for each job:
        for _, job_data in data_found.items():
            csv_writer.writerow([job_data["job_title"], job_data["company_name"], \
                                job_data["company_location"], job_data["posting_date"], \
                                job_data["job_types"], job_data["career_level"], \
                                job_data["years_of_experience"], \
                                job_data["job_link"]])
            # , job_data["job_requirements"]
            