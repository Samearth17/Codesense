def time_in_words(hours, mins):
    # Create phrase string corresponding to time
    phrase = ""
    if hours == 0:
        phrase += "twelve"
    elif hours == 1:
        phrase += "one"
    elif hours == 2:
        phrase += "two"
    elif hours == 3:
        phrase += "three"
    elif hours == 4:
        phrase += "four"
    elif hours == 5:
        phrase += "five"
    elif hours == 6:
        phrase += "six"
    elif hours == 7:
        phrase += "seven"
    elif hours == 8:
        phrase += "eight"
    elif hours == 9:
        phrase += "nine"
    elif hours == 10:
        phrase += "ten"
    elif hours == 11:
        phrase += "eleven"
    elif hours == 12:
        phrase += "twelve"
        
    if mins == 0:
        phrase += " o'clock"
    elif mins == 1:
        phrase += " o'one"
    elif mins == 2:
        phrase += " o'two"
    elif mins == 3:
        phrase += " o'three"
    elif mins == 4:
        phrase += " o'four"
    elif mins == 5:
        phrase += " o'five"
    elif mins == 6:
        phrase += " o'six"
    elif mins == 7:
        phrase += " o'seven"
    elif mins == 8:
        phrase += " o'eight"
    elif mins == 9:
        phrase += " o'nine"
    elif mins == 10:
        phrase += " ten"
    elif mins == 11:
        phrase += " eleven"
    elif mins == 12:
        phrase += " twelve"
    elif mins == 13:
        phrase += " thirteen"
    elif mins == 14:
        phrase += " fourteen"
    elif mins == 15:
        phrase += " fifteen"
    elif mins == 16:
        phrase += " sixteen"
    elif mins == 17:
        phrase += " seventeen"
    elif mins == 18:
        phrase += " eighteen"
    elif mins == 19:
        phrase += " nineteen"
    elif mins == 20:
        phrase += " twenty"
    elif mins == 30:
        phrase += " thirty"
    else:
        tens = int(mins/10)
        ones = mins - tens * 10
        phrase += " " + str(tens) + "ty"
        phrase += " " + str(ones)
        
    return phrase