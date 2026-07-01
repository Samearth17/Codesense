def permute(a, l, r): 
    if l==r: 
        print(''.join(a)) 
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

def main():
    string = input("Enter a string:")
    n = len(string) 
    a = list(string)
    permute(a, 0, n-1)

if __name__ == '__main__': 
    main()