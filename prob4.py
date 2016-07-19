import sys

"""Find the largest palindrome made from the product of two 3-digit numbers."""

def isPalindrome(word):
    return isPalindromeHelper(str(word))


def isPalindromeHelper(word):
    if len(word) <= 1:
        return True
    if word[0] == word[len(word)-1]:
        return isPalindrome(word[1:(len(word)-1)])
    return False


def main():
    assert isPalindrome("abc") is False
    assert isPalindrome("aba") is True
    assert isPalindrome("aa") is True

    multiples = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            multiples.append((i*j))

    print max(filter(isPalindrome, multiples))

if __name__ == '__main__':
    sys.exit(main())

#ans is 580085