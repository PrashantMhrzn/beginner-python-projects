def palindrome(num):
    num = str(num)
    return 'palindrome' if (num[::-1]) == num else 'not palindrome'


print(palindrome(121))
