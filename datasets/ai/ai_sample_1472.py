def generate_report(data):
    # create an empty output dictionary
    output = {}

    # Iterate over the data
    for employee in data:
        # get the employee name
        name = employee['name']

        # get the employee salary
        salary = employee['salary']

        # add the salary info to the output dictionary
        output[name] = salary

    # return the output of the report
    return output