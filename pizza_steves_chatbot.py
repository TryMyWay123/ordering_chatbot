import menu
import datetime as dt
print('Welcome to pizza Steve\'s!')
order_date = dt.datetime.now()
state = 'Tennessee'
city = 'Clinton'
zipcode = '37716'
first = input('Enter your first name.\n')
while(len(first) == 0):
    first = input('Please enter your first name.\n')
last = input('Enter your last name.\n')
while(len(last) == 0):
    last = input('Please enter your last name.\n')
full_name = first + last
pitta_greet = 'Hello I am Pitta, it is nice to meet you.\n' 
print(pitta_greet, first)
method = input('Delivery or Carryout\n')
method.upper()
while method.upper() != 'DELIVERY' and method.upper() != 'CARRYOUT':
    method = input('Please select delivery or carryout.\n')
if method.upper() == 'DELIVERY':
    fee = 3.99
    address = input('Enter your address.\n')
    address_full = address + city + state + zipcode
else:
    print('Carryout is 15 minutes faster.\n')
size = ['small', 'medium', 'large', 'xlarge']
size_price = [8.99, 10.99, 12.99, 14.99]
for s in size:
    print(s)
crust = ['garlic', 'cheese stuffed', 'thick', 'thin', 'no garlic']
sauce = ['red', 'white', 'bbq', 'buffalo', 'ranch', 'pesto']
cheese = ['mozzarella', 'parmesan', 'cheddar', 'provolone', 'feta', 'gouda', 'swiss', 'blue cheese']
topping = ['pepperoni', 'mushrooms', 'sausage', 'onions', 'bacon', 'green peppers', 'red peppers', 'banana peppers', 'black olives', 'green olives', 'chicken', 'pineapple', 'spinach', 'ham', 'beef']
unlimited_toppings = 3.99
print(size)
size = input('Enter the size of the pizza.\n')
while size != 'small' and size != 'medium' and size != 'large' and size != 'xlarge':
    size = input('Please select small, medium, large, or xlarge\n')
print(crust)
crust = input('Enter the crust you desire.\n')
print(sauce)
sauce = input('Enter the sauce you desired.\n')
print(cheese)
cheese = input('Enter the cheese you desire.\n')
print(topping)
toppings = input('Enter the toppings you want on your pizza.\n')
num_pizza = 1
add_pizza = input('Would you like to order another pizza? [Y/N]\n')
add_pizza.upper()
while add_pizza.upper() == 'Y':
    num_pizza += 1
    size = input('Enter the size of the pizza.\n')
    crust = input('Enter the crust you desire.\n')
    sauce = input('Enter the sauce you desired.\n')
    cheese = input('Enter the cheese you desire.\n')
    toppings = input('Enter the toppings you want on your pizza.\n')
if add_pizza.upper() == 'N':
    other_items = input('Would you like drinks or dessert? [Y/N]\n')
    other_items.upper() 
    if other_items.upper() == 'Y':
        drinks = ['Pepsi', 'Coke Cola', 'Dr.Pepper', 'Mtn.Dew', 'Fanta Orange', 'Sweet Tea', 'Mello Yello']
        print(drinks)
        add_drinks = input('Enter your drinks here.\n')
        dessert = ['Cinnamon Twist', 'Lava Ckaes', 'Apple Twist']
        add_dessert = input('Enter your dessert here.\n')
        print(dessert)
        drinks = 2.99
        dessert = 3.99
    else:
        print('Hold on...while I get your total.\n')
price_per_pizza = num_pizza * size + unlimited_toppings
sub_total = price_per_pizza + fee + drinks + dessert
tax = 0.975
total = sub_total * tax
print(full_name, 'the total for your order is', total)
print(order_date)




    