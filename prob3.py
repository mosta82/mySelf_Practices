n = int(input("what's ur number: "))
sum_digit = 0
while n>0:
    digit=n%10
    sum_digit +=digit
    n = n//10


print(sum_digit)        