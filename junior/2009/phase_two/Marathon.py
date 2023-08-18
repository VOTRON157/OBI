water_stations_amount = int(input())
athlete_distance = int(input())
count = 0
for i in range(0, water_stations_amount):
    water_stations_position = int(input())
    if athlete_distance * i >= water_stations_position:
        count += 1
if count == water_stations_amount:
    print("S")
else:
    print("N")