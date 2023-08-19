flour, eggs, milk = map(int, input().split())
count = 0
while flour >= 2 and eggs >= 3 and milk >= 5:
    flour -= 2
    eggs -= 3
    milk -= 5
    count += 1
print(count)