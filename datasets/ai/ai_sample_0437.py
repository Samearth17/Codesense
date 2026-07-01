import nltk 
from nltk.metrics import edit_distance 

def levenshtein_similarity(string1, string2):
    edit_dist = edit_distance(string1, string2)
    similarity = 1-(edit_dist/max(len(string1), len(string2)))
    return similarity

def detect_plagiarism(s1, s2):
    similarity_score = levenshtein_similarity(s1, s2)
    if  similarity_score > 0.75: 
        return "The texts have high similarity"
    elif  similarity_score > 0.5:
        return "The texts have moderate similarity"
    else:
        return "The texts have low similarity"