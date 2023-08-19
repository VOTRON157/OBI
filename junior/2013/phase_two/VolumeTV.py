initial_volume, changes_amount = map(int, input().split())
changes = []
final_volume = initial_volume
for i in range(changes_amount):
    change = input()
    changes.append(change)
for change in changes:
    if final_volume + change > 100:
        final_volume = 100
    elif final_volume + change < 0:
        final_volume = 0
    else:
        final_volume += change
print(final_volume)