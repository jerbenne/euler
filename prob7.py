import sys

def isPrime(num):
	for i in range(2, int(num**0.5 + 1)):
		if num % i == 0:
			return False
	return True 


def main():
	primeCount = 0
	i = 2 
	while primeCount != 10001:
		if isPrime(i):
			primeCount = primeCount + 1
		i = i + 1
	print(i - 1)
				


if __name__ == '__main__':
    sys.exit(main())
