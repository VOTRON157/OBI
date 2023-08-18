bigger_number_represented = int(input())
number_one, operation_signal, number_two = map(str, input().split(" "))
result = 0
if operation_signal == '+':
    result = int(number_one) + int(number_two)
else:
    result = int(number_one) * int(number_two)
if result > bigger_number_represented:
    print("OVERFLOW")
else:
    print("OK")
