def is_prime(num):
    prime = True
    if num <= 1:
        prime = False
    else: 
        for i in range(2, num):
            if num % i == 0:
                prime = False
    return prime

def main():
    num = 10
    print("All prime numbers up to", num, "are:")
    for i in range(2, num+1):
        if is_prime(i):
            print(i)

main()

# Outputs: 2 3 5 7