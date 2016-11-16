#def multiply(a, b):
#    result = a * b
#    return result
# Test the function:
#solution = multiply(4, 5) # Invoke multiply giving it the arguments 4 and 5
#print(solution) # Expected: 20
# Test the function
#print(multiply(4,5)) # Expected: 20
# Test the function
#multiply(4, 5) # Expected: ???
# Test the function
#print(multiply(4,5)) # 20
#print(multiply(9,11)) # 99
#print(multiply(0,10)) # 0
#print(multiply(.5,9)) # 4.5
#print(multiply(-1, -55)) # 55
#print(multiply(3, 'Hello')) # 'HelloHelloHello'
#def isPositive(a):
#    if a > 0:
#        return True
#    else:
#        return False
# Test the function
#print(isPositive(-4)) # Expected: False
#print(isPositive(4)) # Expected: True
#print(isPositive(-9.9)) # Expected: False
#print(isPositive(9.9)) # Expected: True
# Import statements should always be at the top of your file, not in the body of functions
#import random

#def draw_random_card():
#    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
#    random.shuffle(cards)
#    return cards.pop()

# Test the function
#print(draw_random_card()) # Expected: Random number b/n 1 & 11
#print(draw_random_card()) # Expected: Random number b/n 1 & 11
#print(draw_random_card()) # Expected: Random number b/n 1 & 11

#def display_winner(winner, msg):
#    if winner == 'Player':
#        outcome = 'You win! '
#    else:
#        outcome = 'Computer wins! '
#
#    print(outcome + '(' + msg + ')')

# Test the function
#display_winner('Player', 'You were closest to 21') # Expected: You win! (You were closest to 21)
#display_winner('Computer', 'It was closest to 21') # Expected: Computer wins! (It was closest to 21)
#display_winner('Computer', 'You busted')  # Expected: Computer wins! (You busted)

#def square(a):
#    return a * a
#print square(4)

def cube(a):
    product = a * a * a
    return product

solution = cube(3) # Invoke multiply giving it the arguments 4 and 5
print(solution)
