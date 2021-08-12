# Write for loops to accomplish each of the following tasks:

# a. Print the numbers 0 - 20, one number per line.
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

for char in range(0,len(giberish),5):
    print(giberish[char])

print('''\n\n\n''')
# Repeat this process, but replace range(start, stop, step) with range(len(gibberish)).
for num in range(len(giberish)):
    if num % 5 == 0:
        print(giberish[num])
# Use an if statement and the modulus (%) operator to check if the index is divisible by 5. If True, print the character. If False, do not print the character.
# The output should be the same as before.   