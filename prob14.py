import sys

def collatz(start):
	curr = start
	size = 1
	while curr != 1:
		if curr % 2 == 0:
			curr /= 2
		else:
			curr = 3*curr + 1
		size += 1
	return size

def main():
	max = 0
	starting = 0
	for i in range(1, 1000000):
		#print(i)
		num = collatz(i)
		if num > max:
			max = num
			starting = i

	print (starting) 
	


if __name__ == '__main__':
    sys.exit(main())
