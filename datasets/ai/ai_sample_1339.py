def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    for c in s1:
        if c not in s2:
            return False
    for c in s2:
        if c not in s1:
            return False
    return True

def get_anagrams(string):
    anagrams = []
    for i in range(len(string)):
        for j in range(len(string)):
            if i == j:
                continue
            s1 = string[i:j+1]
            s2 = string[:i] + string[j+1:]
            if is_anagram(s1, s2):
                anagrams.append(s2)
    return anagrams