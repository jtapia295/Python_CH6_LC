string1 = '1234'

other_string = '5678'
key_string = ''

for num in range(len(string1)):
    key_string = key_string + string1[num]
    key_string = key_string + other_string[num]

print(key_string)

