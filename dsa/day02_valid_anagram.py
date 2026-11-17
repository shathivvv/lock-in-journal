def is_anagram(s, t):
    return sorted(s) == sorted(t)


#Time O(n log n)
#Space O(n)

def count_chars(text):
    counts={}

    for char in text:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char]=1
    return counts
def is_anagram_fast(s, t):
    if len(s)!= len(t):
        return False

    return count_chars(s) == count_chars(t)

#Time O(n) average
#Space O(k)
#Brute Force
assert is_anagram("listen", "silent")==True
assert is_anagram("rat", "car") == False
assert is_anagram("hello", "hell")== False
assert is_anagram("", "")== True
assert is_anagram("anagram", "nagaram") == True
assert is_anagram("a", "ab")== False
assert is_anagram("aab", "abb")== False
print("Sorting approach: All tests passed!")

#Optimized
assert is_anagram_fast("listen", "silent")==True
assert is_anagram_fast("rat", "car") == False
assert is_anagram_fast("hello", "hell")== False
assert is_anagram_fast("", "")== True
assert is_anagram_fast("anagram", "nagaram") == True
assert is_anagram_fast("a", "ab")== False
assert is_anagram_fast("aab", "abb") ==False
print("Optimized approach: All tests passed!")