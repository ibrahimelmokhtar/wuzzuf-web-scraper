
def calculate_execution_time(start_time, end_time):
    """calculate the runtime of the program

    Args:
        start_time (datetime object): program start time
        end_time (datetime object): program end time

    Returns:
        Int: program runtime (a.k.a., execution time)
    """
    
    # calculate the difference between (start time) and (end time):
    execution_time = end_time - start_time
    
    return execution_time