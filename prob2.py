def check_number_properties(number):
    result = {}

    # Even check
    result['is_even'] = (number % 2 == 0)

    # Divisible by 3
    result['div_by_3'] = (number % 3 == 0)

    # Divisible by 5
    result['div_by_5'] = (number % 5 == 0)

    # ✅ Future expansion (example):
    result['div_by_7'] = (number % 7 == 0)

    return result



n = int(input("👉put a number: "))
res = check_number_properties(n)

# Human readable output
print("\n📊 Result Summary:")
print(res)
print("Even Number?" , "yes" if res['is_even'] else "no")
print("Divisible by 3?" , "yes" if res['div_by_3'] else "no")
print("Divisible by 5?" , "yes" if res['div_by_5'] else "no")
print("Divisible by 7?" , "yes" if res['div_by_7'] else "no")
