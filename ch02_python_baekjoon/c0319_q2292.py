n = int(input())

hex_nums = 0
room_counts = 0

while n > room_counts:
    hex_nums = hex_nums + 1
    if hex_nums == 1:
        room_counts = room_counts + hex_nums
    else:
        room_counts = room_counts + (hex_nums-1)*6
    
print(hex_nums)