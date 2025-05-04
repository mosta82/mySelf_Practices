def digital_root(n):
    print(f"Original Number: {n}")
    while n > 9:
        digits = [int(d) for d in str(n)]
        n = sum(digits)
        print(f"Sum of digits: {n}")
    return n

num = int(input("Enter a number: "))
result = digital_root(num)
print("Digital Root:", result)
