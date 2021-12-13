from datetime import datetime
import csv

def format_file_name(desired_job):
    
    """format file name without file extension (for example: ".txt", ".csv", ... etc.)

    Returns:
        String: constructed file name
    """
    # format file name using current date and time:
    date_now = str(datetime.now()).split(":")
    date_now = "-".join(date_now)
    
    file_name = str("{} {}".format(date_now, desired_job))
    
    return file_name
    

def save_into_csv(desired_job, data_found):
    # construct file name:
    file_name = format_file_name(desired_job) + ".csv"

    with open(file_name, 'w') as csv_file:
        # create csv writer object:
        csv_writer = csv.writer(csv_file)
        
        # write header names:
        csv_writer.writerow(["Job Title", "Company Name", "Company Location", "Posting Date", \
                            "Job Types", "Career Level", "Years of Experience"])
        
        # start writting details for each job:
        count = 0
        for _, job_data in data_found.items():
            count += 1
            csv_writer.writerow([job_data["job_title"], job_data["company_name"], \
                                job_data["company_location"], job_data["posting_date"], \
                                job_data["job_types"], job_data["career_level"], \
                                job_data["years_of_experience"]])
            