import sys


def main():
	for a in range(0, 1000):
		for b in range(a, 1000):
			for c in range(b, 1000):
				if a + b + c == 1000:
					if a**2 + b**2 == c**2:
						print (a * b * c)

if __name__ == '__main__':
    sys.exit(main())
