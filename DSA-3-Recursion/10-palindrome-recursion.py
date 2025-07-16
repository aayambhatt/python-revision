def palindrome(s, left, right):
    s = s.lower()
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return palindrome(s, left+1, right-1)


s1 = "Naman"
s2 = "Aayam"
print(palindrome(s1, 0, len(s1)-1))
print(palindrome(s2, 0, len(s2)-1))


    
