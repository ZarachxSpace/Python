# def is_palindrome(s):
#     pure_text = "".join(char for char in s if char.isalnum())
#     reverse = pure_text[::-1]
#     return pure_text.lower() == reverse.lower()

def is_palindrome(s):
    reverse = ""
    pure_text = "".join(char for char in s if char.isalnum())
    for char in pure_text:
        reverse = char + reverse
    return (reverse.lower() == pure_text.lower())


s = "ttytt"
print(is_palindrome(s))

