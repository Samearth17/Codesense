import argparse
import sys

def permutation(string):
 if len(string) == 1:
 return [string]
 
 result = []
 
 for i in range(len(string)):
 s = string[i]
 remString = string[:i] + string[i+1:]
 
 for p in permutation(remString):
 result.append(s + p)
 
 return result
 
if __name__ == '__main__':
 parser = argparse.ArgumentParser()
 parser.add_argument('--string', default=None, help='string to permutate')
 args = parser.parse_args()

 if (args.string is None):
 print('Please provide a valid string as command line argument!')
 sys.exit(1)
 
 result = permutation(args.string)
 print(result)