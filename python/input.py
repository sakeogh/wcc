#name = raw_input('What is your name? ')
#print('Hi ' + name)
#name = raw_input('What is your name?')
#age = raw_input('How old are you?')
#print(name + ' is ' + age + ' years old.')
#age = raw_input('How old are you?')
#dog_years = int(age) * 7
#print('You are ' + str(dog_years) + ' old in dog years.')
#total = float(raw_input("How much was your meal?"))
#tip = total * 20 / 100
#new_total = total + tip
#print("You should tip " + str(tip) + ".")
#print("Your total cost would be " + str(new_total))
#total = raw_input("How much was your meal?")
#tip = float(total) * 20 / 100
#new_total = float(total) + float(tip)
#print("You should tip " + str(tip) + ".")
#print("Your total cost would be " + str(new_total) + ".")
#total = float(raw_input("How much was your meal?"))
#tip = total * 20 / 100
#new_total = total + tip
#print("You should tip $" + str(tip) + ".")
#print("Your total cost would be $" + str(new_total) + ".")
#total = float(raw_input("How much was your meal?"))
#tip = total * .2
#new_total = total + tip
#print("You should tip $" + str(tip) + ".")
#print("Your total cost would be $" + str(new_total) + ".")
total = raw_input("How much was your meal?")
tip = float(total) * 20 / 100
rtip = round(tip, 2)
new_total = float(total) + float(tip)
print("You should tip " + str(rtip) + ".")
print("Your total cost would be " + str(new_total) + ".")
