n = int(input())

line_num = 0
num_counts = 0

while n > num_counts:
    line_num = line_num + 1
    num_counts = num_counts + line_num

difference = num_counts - n

if line_num % 2 == 0:
    a = line_num - difference
else:
    a = difference + 1
b = (line_num + 1) - a

print('{}/{}'.format(a, b))