# Write for loops to accomplish each of the following tasks:

# a. Print the numbers 0 - 20, one number per line.
from typing_extensions import IntVar


for num in range(21):
    print(num) 
# b. Print only the ODD values from 3 - 29, one number per line.
for num in range(3,30, 2):
    print(num)
# c. Print the EVEN numbers 12 down to -14 in descending order, one number per line.
for num in range(12,-14, -2):
    if num != 0:
        print(num)
# d. Print the numbers 50 down to 20 in descending order, but only if the numbers are multiples of 3.
for num in range(50,20, -1):
    if (num / 3) % 1 == 0:
        print(num)

 
word = 'LaunchCode'

# Given the string in 'word' code for loops to do the following:

# a) Print out each character of the string, one letter per line. Do this WITHOUT using index values.
for char in word:
    print(char)
print("<-------------------------->")

# b) Use index values to print each character of the string—in reverse order—to a new line. 
# To access a single character from a string, 
# use the syntax word[index], where index is an integer value.
for num in range(len(word),0,-1):
    print(word[num-1])

 # Code a for loop to print the every 5th character from 'gibberish', including the first character. Use index values and range(start, stop, step).

# Hint: Instead of figuring out the stop value by counting all of the characters in gibberish yourself, make Python do it for you! 
# len(gibberish) returns the length of the string stored in the variable.
#giberish = 'Vna#hewzB*rQhT%yq^lvg xiPwgOexWo &C^oUoGSdtJLj'
gibberish = 'Vna#hewzB*rQhT%yq^lv %iPwgOexWo &C^oUoGSdtJLj'

for char in range(0,len(gibberish),5):
    print(gibberish[char])
print('''\n\n\n''')

# Repeat this process, but replace range(start, stop, step) with range(len(gibberish)).
# Use an if statement and the modulus (%) operator to check if the index is divisible by 5. If True, print the character. If False, do not print the character.
# The output should be the same as before.
# for num in range(len(gibberish)):
if num % 5 == 0:
    print(gibberish[num])   




# Define three variables for a spacecraft - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the spacecraft reaches.
space_craft_altitude = 0
astronauts_onboard = None
fuel_level = None

# Code a while loop to ask the user for the starting fuel level. The loop should continue until the user enters a value between 5000 and 30000. If the user submits a number outside of the range, print "Invalid entry."
fuel_level = int(input('Please enter an amount of fuel to enter. 5000-30000'))

while fuel_level < 5000 or fuel_level > 30000:
    print('Invalid Entry')
    fuel_level = input('Please enter a valid range(5000 - 30000)')


# Code a second loop to prompt the user for the number of astronauts. Have the loop continue until the user enters an integer from 1 - 7.
astronauts_onboard = int(input('How many astronauts will be onboard? Range (1-7)'))

while astronauts_onboard < 1 or astronauts_onboard > 7:
    print('Invalid Entry.')
    astronauts_onboard = int(input('Please enter amount of passengers within range 1-7'))


# Use a third while loop to update the fuel and the altitude of the spacecraft. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers. 
# The loop should end when there is not enough fuel to boost the crew another 50 km, so the fuel level might not reach 0.

while fuel_level - (100 * astronauts_onboard) >= 0 :
    fuel_level = fuel_level - (100 * astronauts_onboard)
    space_craft_altitude = space_craft_altitude + 50
    print('Fuel Level at ', fuel_level)
    print('Altitude Covered ', space_craft_altitude, ' km')

print('<-------------------------------->')
        


# After the loops finish, print the result using the phrase, "The spacecraft gained an altitude of ___ km and has ___ kg of fuel left." Fill in the blanks with the current altitude and fuel level values.
print('Spacecraft gained an altitude of ', space_craft_altitude, ' km and has ', fuel_level, ' kg of fuel left.')

# If the altitude is 2000 km or higher, add "Orbit achieved!" to the output. Otherwise add, "Failed to reach orbit."
if space_craft_altitude >= 2000:
    print('Orbit Acheived!')
else:
    print('Failed to reach orbit!')



# Use two input statements to prompt the user for a start_value and an end_value. Both inputs should be integers.
start_value = int(input('Please enter a starting value'))
end_value = int(input('Please enter a ending value'))
total = 0

# Use a loop to add up all of the numbers from start_value to end_value. Use the variable 'total' as the accumulator. Print "The sum of the numbers from ___ to ___ is ___." Fill in the blanks with the values for start_value, end_value, and total.
for num in range(start_value,end_value):
    total = total + num

print('The sum of the numbers from ',start_value, ' to ', end_value, ' is ', total, '.')




# Use the accumulator pattern to build a new string. It should contain all of the characters from the string stored in 'sentence', but without any vowels. For this task, y does NOT count as a vowel. Print the new string.
sentence = 'It was a bright cold day in April, and the clocks were striking thirteen.'
no_vowels = ''

for char in sentence:
    if char not in 'aeiou':
        no_vowels = no_vowels + char

print(no_vowels)