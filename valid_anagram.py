# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

def valid_anagram(string, test):
    string_list = list(string)
    test_list = list(test)
    if sorted(string_list) == sorted(test_list):
        return True
    else:
        return False

print(valid_anagram('one', 'eno'))