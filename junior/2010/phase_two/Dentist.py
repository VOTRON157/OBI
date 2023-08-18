number_of_appointments = int(input())
start_time, end_time = map(int, input().split())
aux = end_time
count = 1
for i in range(number_of_appointments - 1):
    start_time, end_time = map(int, input().split())
    if aux <= start_time:
        count += 1
        aux = end_time
print(count)