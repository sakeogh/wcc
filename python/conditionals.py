#meal_price = float(raw_input('How much was your meal? '))
#print('How would you rate the service? ')
#print('a. Not so good')
#print('b. Good')
#print('c. Excellent!')
#chosen_option = raw_input('Choose an option: ')

# Here's where conditionals come in...
#if chosen_option == 'a':
#    percentage = .15;
#elif chosen_option == 'b':
#    percentage = .18;
#else:
#    percentage = .20;

#tip = meal_price * percentage
#total_price = meal_price + tip
#print('You should tip $' + str(tip))
#print('Your total cost would be $' + str(total_price))

temp = int(raw_input('What is the temperature?'))

print('You should bring the following items:')
if temp <= 40: #If the temp is less than 40 degrees:
    print('Coat') #Bring a light coat
    print('Hat') #Bring a hat
    print('Gloves') #Bring gloves
elif temp <= 70: #Otherwise, if the temp is greater than 40 degrees but less than 70 degrees:
    print('Coat') #Bring a light coat
    print('Hat') #Bring a hat
else: #Otherwise:
    print('Nothing!') #Bring just the clothes you're wearing