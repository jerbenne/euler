import sys

def numFactors(num):
	factors = 2 #num and itself
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			factors += 2
	return factors

def main():
	triNum = 1
	i = 2
	
	while numFactors(triNum) < 500:
		triNum += i
		i += 1

	print(triNum)
				


if __name__ == '__main__':
    sys.exit(main())
