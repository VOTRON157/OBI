number_of_trays = int(input())
broken_cups = 0
for i in range(number_of_trays):
    can, cups = map(int, input().split())
    if can > cups:
        broken_cups += cups
print(broken_cups)