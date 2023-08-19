container_width, container_length, container_height = map(int, input().split())
ship_width, ship_length, ship_height = map(int, input().split())
containers_amount = (ship_width // container_width) * (ship_length // container_length) * (ship_height // container_height)
if container_width > ship_width or container_length > ship_length or container_height > ship_height:
    print(0)
else:
    print(containers_amount)