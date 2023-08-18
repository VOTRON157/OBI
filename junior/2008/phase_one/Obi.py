number_of_participants, minimum_points = map(int, input().split())
count = 0
for i in range(number_of_participants):
        first_phase_points, second_phase_points = map(int, input().split())
        if first_phase_points + second_phase_points >= minimum_points:
            count += 1
print(count)