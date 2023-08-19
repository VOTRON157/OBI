wins_c, ties_c, goals_c, wins_f, ties_f, goals_f = map(int, input().split())
points_c = (wins_c * 3) + ties_c
points_f = (wins_f * 3) + ties_f

if points_c > points_f:
    print("C")
elif points_c < points_f:
    print("F")
else:
    if goals_c > goals_f:
        print("C")
    elif goals_c < goals_f:
        print("F")
    else:
        print("=")