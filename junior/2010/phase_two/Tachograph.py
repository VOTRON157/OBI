number_of_breaks = int(input())
traveled_distance = 0
for i in range(number_of_breaks):
    time, velocity = map(int, input().split())
    traveled_distance += time * velocity
print(traveled_distance)