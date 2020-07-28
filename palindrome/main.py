def palindrome(num):
    num = str(num)
    return 'palindrome' if (num[::-1]) == num else 'not palindrome'


usr_inp = input('enter a number or string to check if palindrome: ')
print(palindrome(usr_inp))
