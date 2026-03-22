# def even_integers(num):
#     even = []
#     for n in (num):
#         if n % 2 == 0:
#             even.append(n)

#     return even

def even_integers(num):
    even = [n for n in num if n % 2 == 0]
    return even


integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_integers(num=integer_list))
