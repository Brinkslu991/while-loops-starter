### Counting up to a user-specified number
```python
end_number = int(input("Enter the end number:\n"))
counter = 0

while counter < end_number:
  print(counter)
  counter += 1
```

### Counting down from a a user-specified number
```python
start_number = int(input("Enter the starting number:\n"))
counter = start_number # Assign the start number to the variable named counter

while counter > 0:
  print(counter)
  counter -= 1
```

### Letting the user choose when to quit the loop
```python
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to exit the script."

message = "" # Create an empty string to start with
while message != "quit": # Loop keeps looping until the user enters the word quit
    message = input(prompt)
    print(message)