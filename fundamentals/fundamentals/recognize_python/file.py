num1 = 42  # variable declaration, number
num2 = 2.3  # variable declaration, number
boolean = True  # variable declaration, Boolean
string = 'Hello World'  # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False} #initialize dictionary, IndentationError: unexpected indent
fruit = ('blueberry', 'strawberry', 'banana') #initialize tuples
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access the pizza topping with index of 1 and print value
pizza_toppings.append('Mushrooms') #add list value
print(person['name']) #log statement
person['name'] = 'George' #change dictionary value
person['eye_color'] = 'blue' #add dictionary value
print(fruit[2]) #log statement, access the fruit with index of 2 and print value
#conditional
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
