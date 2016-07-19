import sys

def isPrime(num):
	for i in range(2, int(num**0.5 + 1)):
		if num % i == 0:
			return False
	return True 


def main():
	primeSum = 0
	for i in range(2, 2000000):
		if isPrime(i):
			primeSum += i
	print(primeSum)
				


if __name__ == '__main__':
    sys.exit(main())
