# def isAnagram(s, t):
#     array_s = list(s)
#     array_t = list(t)

#     array_s.sort()
#     array_t.sort()

#     return array_s == array_t


# def isAnagram(s, t):
#     if len(t) != len(s):
#         return False

#     count_s = {}
#     count_t = {}

#     for char in s:
#         count_s[char] = count_s.get(char, 0) + 1

#     for char in t:
#         count_t[char] = count_t.get(char, 0) + 1

#     return count_s == count_t



s, t = "anagram", "nagaram"
print(isAnagram(s, t))
