number_of_operations = int(input())
result = 1
for i in range(number_of_operations):
    operation = input().split(" ")
    if operation[1] == "*":
        result *= int(operation[0])
    else:
        result /= int(operation[0])
print(result)