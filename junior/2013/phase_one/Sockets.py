socket_strip_one, socket_strip_two, socket_strip_three, socket_strip_four = map(int, input().split())
total_sockets = (socket_strip_one + socket_strip_two + socket_strip_three + socket_strip_four) - 3
print(total_sockets)