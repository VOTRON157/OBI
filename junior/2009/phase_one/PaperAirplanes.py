number_of_participants, paper_purchased_amount, paper_needed_amount = map(int, input().split())
if number_of_participants * paper_needed_amount <= paper_purchased_amount:
    print("S")
else:
    print("N")