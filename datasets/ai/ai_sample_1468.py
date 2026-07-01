import random
 
def MonteCarlo(n):
    inside = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside += 1
 
    return 4*inside/n
 
if __name__ == '__main__':
    n = int(input("Input the number of points: "))
    print("Pi is approximately {}!".format(MonteCarlo(n)))