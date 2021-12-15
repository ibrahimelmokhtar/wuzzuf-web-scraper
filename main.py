from checkUserInput import *
from saveIntoFile import *
from wuzzufAPI import *
from calculateExecutionTime import *

def main():
    # get disired hob title from the user:
    desired_job = input("Enter job title: ")
    check_jobTitle(desired_job)
    
    # program's execution start time: 
    start_time = datetime.now()
    
    # extract specific data from wuzzuf.net:
    data_found = wuzzuf_api(desired_job)

    # save found data into .csv file:
    save_into_csv(desired_job, data_found)
    
    # program's execution end time:
    end_time = datetime.now()
    
    # calculate total execution time:
    execution_time = calculate_execution_time(start_time, end_time)
    
    # display a message for the user:
    print("The program took:\n\t{}\t\t... formated as (hr : min : sec)".format(execution_time))
    print("to obtain ({}) job results".format(count_found_jobs(data_found, False)))


# entry point:
if __name__ == "__main__":
    try:
        main()
    except:
        print("Exception in main() function ...")
