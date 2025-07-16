def is_palindrome(s):
    s = s.lower()
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  
print(is_palindrome("No 'x' in Nixon"))                 
print(is_palindrome("Hello, World!"))      
print(is_palindrome("mOm"))             
