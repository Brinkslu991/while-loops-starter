### Input ( ) Function Examples

> The `input( )` function by itself will always return a string.

#### Returning a String
```python
first_name = input('Please enter your first name: (Example: Carl)\n')  

print('You said your first name was {first_name.title()}, right?')
```

#### Returning an Integer using int ( ) and input ( )
- An **integer** is a number without a decimal point  

```python
age = int(input('How old are you?\n'))
print(f'You are {age} years old today.')
```



#### Returning a Float using float ( ) and input ( )
- A **float** (or **floating-point number**) is a number WITH a decimal point  

```python
length = float(input('Enter the length of your living room (in feet): (Example: 20.50)\n'))

width = float(input('Enter the width of your living room (in feet):\n'))

print(f'Living room length (in ft.) {length}')
print(f'Living room width (in ft.) {width}')
```


