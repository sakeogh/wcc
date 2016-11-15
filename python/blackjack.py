import random
#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#print(cards) # To see the list before being shuffled

random.shuffle(cards)

#print(cards) # To see the list after being shuffled

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Your card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

#print(cards) # To see the list after two cards have been popped off.
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

# Round 2
if decision == 's':
    player_card2 = 0
    print('Your card: ' + str(player_card1));
    computer_card2 = cards.pop()
    print('Computer cards:  ' + str(computer_card1) + ', ' + str(computer_card2))
elif decision == 'h':
    player_card2 = cards.pop()
    computer_card2 = cards.pop()
    print('Your card: ' + (str(player_card1) + ', ' + str(player_card2)))
    print('Computer card:  ' + (str(computer_card1) + ', ' + str(computer_card2)))

# Round 2 results
player_card_total2 = player_card1 + player_card2
computer_card_total2 = computer_card1 + computer_card2

if computer_card_total2 == 21:
    print('Game over. Computer wins.')
elif player_card_total2 == 21:
    print('Game over. You win.')
elif (player_card_total2 == 21) and (computer_card_total2 == 21):
    print("Game over. It's a draw!")
else:
    decision2 = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

# Round 3
if (decision2 == 's') and (computer_card_total2 <= 16):
    player_card3 = 0
    print('Your cards:  '+ str(player_card1) + ', ' + str(player_card2))
    computer_card3 = cards.pop()
    print('Computer cards:  ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3))
elif (decision2 == 's') and (computer_card_total2 > 16):
    player_card3 = 0
    computer_card3 = 0
    print('Your cards:  '+ str(player_card1) + ', ' + str(player_card2))
    print('Computer cards:  '+ str(computer_card1) + ', ' + str(computer_card2))
elif (decision2 == 'h') and (computer_card_total2 <= 16):
    player_card3 = cards.pop()
    computer_card3 = cards.pop()
    print('Your card: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
    print('Computer card:  ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3))
elif (decision2 == 'h') and (computer_card_total2 > 16):
    player_card3 = cards.pop()
    computer_card3 = 0
    print('Your card: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
    print('Computer cards:  ' + str(computer_card1) + ', ' + str(computer_card2))

player_card_total3 = player_card1 + player_card2 + player_card3
computer_card_total3 = computer_card1 + computer_card2 + computer_card3

if (player_card_total2 > 21) and (computer_card_total2 <= 21):
    print('Game over. Computer wins.');
elif (player_card_total2 <= 21) and (computer_card_total2 > 21):
    print('Game over. You win.');
elif (player_card_total2 == 21) and (computer_card_total2 == 21):
    print("Game over. It's a draw!");
else:
    print('Bye')
