## Break & Continue Statements in Python

### Break Statement
> Used to exit a while loop immediately (even if there are lines of code still left to run in the loop)

```python
prompt = "\nPlease enter the name of a city you have visited:\n"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit': # Note use of equality operator (==)
        break
    else:
        print(f"I'd love to go to {city.title()}!)
```  

### Continue Statement
> You can use a **continue statement** to return to the beginning of a loop (rather than breaking out the loop entirely without executing the rest of the code)
```python
counter = 0
while counter < 10:
    counter += 1 # Increase counter value by 1 each time the loop runs
    if counter % 2 == 0: # If the counter value is an even number...
        continue

    print(counter)
```
```python
# The output for the Continue Statement example would be:
```
```python
1
3
5
7
9
```
