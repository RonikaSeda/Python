import os
import random
should_continue = True
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
list_of_card_points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#-----------------------------------------------------------------------  
def start_game():
  for turn in range(0,2):
    my_cards.append(random.choice(list_of_card_points))
    dealers_cards.append(random.choice(list_of_card_points))
  if 10 in my_cards and 11 in my_cards:
    print(f"You lose! - you had the Black Jack {my_cards}")
    return False
  if 10 in dealers_cards and 11 in dealers_cards:
    print(f"You win! - Dealer has the Black Jack {dealers_cards}")
    return False
  return True
  
def continue_game():
  global my_result
  my_result = 0
  for card in my_cards:
    my_result += int(card)
    
  global dealers_result
  dealers_result = 0
  for card in dealers_cards:
    dealers_result += int(card)
  if dealers_result <= 16:
    new_card = random.choice(list_of_card_points)
    dealers_cards.append(new_card)
    dealers_result += new_card
  # print(f"DEALER'S {dealers_cards} and {dealers_result}")

  if my_result >= 21 and 11 in my_cards:
    my_result -= 10
 
  if dealers_result >= 21 and 11 in dealers_cards:
    dealers_result -= 10
  print(f"Your card points are {my_cards} ({my_result})\nDealer's one card point is {dealers_cards[0]}")
  return my_result, dealers_result
  
def add_cards():
  global my_result
  answer = input("Do you want to get another card? yes/no\n")
  while answer == "yes" and my_result < 21:
    points_to_be_added = random.choice(list_of_card_points)
    my_cards.append(points_to_be_added)
    my_result += points_to_be_added
    print(f"{my_cards} ({my_result})")
    if my_result < 21:
      answer = input("Do you want to get another card? yes/no\n")
    
          
def end_game():
  clear_screen()
  if dealers_result < my_result <= 21:
    print("You win!")
  elif my_result < dealers_result <= 21:
    print("Dealer wins!")
  elif my_result == dealers_result:
    print("Draw")
  elif my_result <= 21 <= dealers_result:
    print("You win")
  elif dealers_result <= 21 <= my_result:
    print("You lose")
  else:
    print("Both lose")
  print(f"your result {my_result}")
  print(f"dealers result {dealers_result}")
  
while should_continue:
  my_cards = []
  dealers_cards = [] 
  if start_game():
    continue_game()
    add_cards()
    end_game()
    want_continue = input("\nDo you want one more game? yes/no\n")
  if want_continue == "no":
    should_continue = False
    clear_screen()
    print("Thank you for the game!")
  else:
    clear_screen()


