a='radar'
b='janu'

print(type(a),type(b))

#Check - Palindrome

if a==a[::-1]:
    print(a+ ' is a palindrome')
else:
    print(a+ ' is not a polindrome')

if b==b[::-1]:
    print(b + ' is a polindrome')
else:
    print(b + ' is not a palindrome')