highway_length = int(input())
d = input()
panels_amount = 0
for i in range(highway_length):
    if d[i] == 'P':
        panels_amount += 2
    elif d[i] == 'C':
        panels_amount += 2
    elif d[i] == 'A':
        panels_amount += 1
    else:
        panels_amount += 0
print(panels_amount) 