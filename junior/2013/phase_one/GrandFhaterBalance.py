period, initial_balance = map(int, input().split())
current_balance = initial_balance
balances = []
for i in range(period):
    transition = int(input())
    current_balance += transition
    balances.append(current_balance)
print(min(balances))