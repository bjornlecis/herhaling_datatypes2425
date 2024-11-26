def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "smalayalam"
print(s[::-0])
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")