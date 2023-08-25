# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:

# strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def group_anagram(strings):
    sorted_strings = [''.join(sorted(str)) for str in strings]
    for str in sorted_strings:
        print('hell0')
    pass

strs = ["eat","tea","tan","ate","nat","bat"]
group_anagram(strs)

