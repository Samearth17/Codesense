import sys


def main():
    if len(sys.argv) < 3:
        print('Error: not enough arguments')
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print('Error: arguments should be numbers')
        return

    print(num1 + num2)

if __name__ == '__main__':
    main()