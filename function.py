def palindrome(x):
    b = x[::-1]
    if x==b:
        return "It is a palindrome"
    else:
        return"Not a palindrome"