number_of_peoples = int(input())
list_time = []
for i in range(number_of_peoples):
    time = int(input())
    list_time.append(time)
print(abs(list_time[0] - list_time[number_of_peoples - 1]) + 10)