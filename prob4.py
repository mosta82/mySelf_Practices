# def sum_digits_recursive(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digits_recursive(n // 10)

# print(sum_digits_recursive(456))  # Output: 15

n = 234
digits = []
while n > 0:
    digits.insert(0,n % 10)  
    n = n // 10
print(sum(digits))  # Output: [2, 3, 4]
