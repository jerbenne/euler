import sys

#prob 2
def evenFib():
    """By considering the terms in the Fibonacci sequence whose 
    values do not exceed four million, find the sum of the even-valued terms."""
    fib = [1,2]

    while fib[len(fib)-1] < 4000000:
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    fib.pop() #remove element greater than 400000

    evenFibs = filter((lambda x : x % 2 == 0), fib)
    return reduce( lambda x, y: x+y, evenFibs)

#prob 3
def largestPrimeFactor():
    num = 600851475143
    factors = []

    factor = 2
    while num != 1:
        if num % factor == 0:
            factors.append(factor)
            num = num / factor

        else:
            factor = factor + 1

    return max(factors)



#prob 4

def main():
    print(largestPrimeFactor())




if __name__ == '__main__':
    sys.exit(main())