import sys


"""What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
def sol():
    i = 0
    while True:
   		i = i + 1
   		if isDiv(i):
   			return i


def isDiv(num):
	for i in range(1,21):
		if num % i != 0:
			return False
	return True

def main():
    print(sol())


if __name__ == '__main__':
    sys.exit(main())


#ans is 232792560
