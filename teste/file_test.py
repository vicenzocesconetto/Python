string = '23,455 ,54545, 454445, 6,65566,65'

array = string.split(',')

print(array)

for i in array:
    print(int(i))
