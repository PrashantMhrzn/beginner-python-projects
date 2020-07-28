def palindrome(num):
    num = str(num)
    if (num[::-1]) == num:
        print("palindrome")
    else:
        print("not palindrome")
    return ''


print(palindrome(231))
