def fill_missing_data(data):
    # Get the shape of the data
    num_rows, num_columns = data.shape
    
    # Get the index for the missing row
    missing_row_index = 6
    
    # Iterate through the columns and fill in the missing data
    for col_index in range(num_columns):
        # Calculate the mean of the two values before and after the missing row
        mean_val = (data[missing_row_index -1, col_index] + data[missing_row_index + 1, col_index]) /2
        # Fill in the missing value
        data[missing_row_index, col_index] = mean_val
        
    # Return the data with the missing row filled in
    return data