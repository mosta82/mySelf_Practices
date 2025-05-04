# def get_digits(number):
#     digits = []
#     while number > 0:
#         digits.insert(0, number % 10)
#         number = number // 10
#     return digits

def get_digits_reverse(number):
    digits = []
    while number > 0:
        digits.append(number % 10)  # add last digit
        number = number // 10
    return digits

n = int(input("Enter a number: "))
# print("Digits:", get_digits(n))
print("Digits:", get_digits_reverse(n))