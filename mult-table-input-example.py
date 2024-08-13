factor = int(input('What number do you want to generate a times table for? (Example: 6)\n'))

for counter in range(5, 11, 2):
    result = counter * factor
    print(f'{counter} times {factor} = {result}')
