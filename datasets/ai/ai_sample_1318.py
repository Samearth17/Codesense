def is_anagram(str1, str2):
 str1_dict = dict()
 str2_dict = dict()
 
 for char in str1:
 if char in str1_dict:
 str1_dict[char] += 1
 else:
 str1_dict[char] = 1
 
 for char in str2:
 if char in str2_dict:
 str2_dict[char] += 1
 else:
 str2_dict[char] = 1
 
 for key in str1_dict:
 if key not in str2_dict:
 return False
 elif str1_dict[key] != str2_dict[key]:
 return False
 
 return True