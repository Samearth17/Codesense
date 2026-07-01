def checkStability(input_string):
    # Initializing variable to 0
    stability_level = 0

    # Counting vowels
    vowels_count = 0 
    vowel_list = ['a','e','i','o','u']
    for i in input_string: 
        if i in vowel_list:
            vowels_count += 1

    # Calculating stability
    stability_level = vowels_count / len(input_string)

    # Printing out the stability
    print("Stability of string '%s' = %.2f" %(input_string,stability_level)) 

input_string = "This is a test sentence!" 
checkStability(input_string)