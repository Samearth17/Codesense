def compare_strings(str1, str2):
 # compare string length
 if len(str1) > len(str2):
 print('String 1 is longer than String 2')
 elif len(str2) > len(str1):
 print('String 2 is longer than String 1')
 else:
 print('Strings are of equal length')

 # compare characters
 common_chars = set(str1).intersection(set(str2))
 if len(common_chars) == min(len(str1), len(str2)):
 print('Strings have same characters')

 # compare case sensitivity
 if str1.lower() == str2.lower():
 print('Strings are equal in terms of case sensitivity')

str1 = 'Hello World'
str2 = 'hello world!'

compare_strings(str1, str2);