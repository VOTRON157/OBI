coord_x, coord_y = map(int, input().split())

if coord_x >= 0 and coord_x <= 432 and coord_y >= 0 and coord_y <= 468:
    print("dentro")
else:
    print("fora")