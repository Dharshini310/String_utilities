def reverse_String(n):
    return n[::-1]
def check_palidrome(n):
    k = n
    reverse_n = n[::-1]
    return k == reverse_n
def count_vowels(n):
    s = {'a','e','i','o','u'}
    c = 0
    for i in n :
        if i in s:
            c = c + 1
    return c
