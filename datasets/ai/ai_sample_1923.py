def classify_strings(strings):
    # initialize lists for each classification
    short = []
    long = []
    # classify each string
    for s in strings:
        if len(s) <= 6:
            short.append(s)
        else:
            long.append(s)
    # return classified lists
    return [short, long]

if __name__ == '__main__':
    strings = ['short', 'longer_string', 'medium_length', 'very_long_string']
    print(classify_strings(strings))