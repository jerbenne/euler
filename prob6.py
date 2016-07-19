import sys

def sol():
    pass

def sum_of_squares(n):
    return sum([i**2 for i in range(1, n+1)])

def main():

    print sum(range(1,101))**2 - sum([i**2 for i in range(1, 101)])


if __name__ == '__main__':
    sys.exit(main())

#ans is 25164150