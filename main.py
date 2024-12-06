# Lucas Brinks
# 12/6/24
# While loops intro

# Number game
# import random

# name = input('Hello there what is your name?: ')
# number = random.randint(1,100)
# print(f'Hello {name}, I\'m thinking of a number between 1 and 100.')
# guesses_taken = 0

# while guesses_taken < 5:
#     guess = input('Enter a guess: ')
#     guess = int(guess)
#     guesses_taken = guesses_taken + 1
#     if guess < number:
#         print('That was too low.')
#     elif guess > number:
#         print('That was too high.')
#     else:
#         break
    
# if guess == number:
#     print('Good job you waisted your time guessing my number.')
# else:
#     print(f'How did you not guess {number}')

# Temperature averg

temperatures = []
while True:
    temp = int(input('Enter a temperature (Enter -9999 to quit): '))
   
    if temp == -9999:
        break
    else:
        temperatures.append(temp)
    
print(temperatures)
avrg = sum(temperatures)/len(temperatures)
print(f'{avrg}°F')

        


