# def is_palindrome(s):
#     pure_text = "".join(char.lower() for char in s if char.isalnum())
#     return pure_text == pure_text[::-1]


def is_palindrome(s):
    pure_text = "".join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(pure_text) - 1
    while left < right:
        if pure_text[left] != pure_text[right]:
            return False
        
        left += 1
        right -= 1

    return True


s = "Racecar"
print(is_palindrome(s))

