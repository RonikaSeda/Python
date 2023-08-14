from game_data import data
import random
import os
number_of_data = len(data)
correct_answer = " "
score = 0
A_data_to_display = ""
B_data_to_display = ""

def clear_screen():
  os.system('cls')

def A():
  global A_data_to_display
  print("Compare A: ")
  A_data_to_display = random.choice(data)
  print(A_data_to_display["name"]+", ", 
 A_data_to_display["description"]+", ", "from " + A_data_to_display["country"])
  return A_data_to_display

def B():
  global B_data_to_display
  print("Against B: ")
  B_data_to_display = random.choice(data)
  print(B_data_to_display["name"]+", ", 
 B_data_to_display["description"]+", ", "from " + B_data_to_display["country"])
  return B_data_to_display

def comparism():
  global A_data_to_display
  global B_data_to_display
  global correct_answer
  first_data = A_data_to_display["follower_count"]
  second_data = B_data_to_display["follower_count"]
  if first_data > second_data:
    correct_answer = "a"
  elif first_data < second_data:
    correct_answer = "b"


def evaluation():
  global user_answer
  global correct_answer
  global number_of_data
  global score
  if user_answer == correct_answer:
    score += 1
    clear_screen()
    print(f"You're right! Current score: {score}.\n")
    return True
  else:
    final_message = "\n\nSorry, that's wrong. Final score: "
    print(final_message + str(score))
    return False
 #_________________________________________________________ 
should_continue = True
while should_continue:
  A()
  B()
  user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  comparism()
  should_continue = evaluation()
