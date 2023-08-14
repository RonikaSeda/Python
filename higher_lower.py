from game_data import data
import os
number_of_data = len(data)
correct_answer = " "
score = 0
def clear_screen():
  os.system('cls')
def A():
  print("Compare A: ")
  data_to_display = data[index] 
  print(data_to_display["name"]+", ", 
 data_to_display["description"]+", ", "From " + data_to_display["country"])

def B():
  print("Against B: ")
  data_to_display = data[index+1]
  print(data_to_display["name"], 
 data_to_display["description"], "From " + data_to_display["country"])

def comparism():
  global correct_answer
  data_to_display = data[index]
  first_data = int(data_to_display["follower_count"])
  data_to_display = data[index+1]
  second_data = int(data_to_display["follower_count"])
  if first_data > second_data:
    correct_answer = "a"
  elif first_data < second_data:
    correct_answer = "b"


def evaluation():
  global user_answer
  global correct_answer
  global index
  global number_of_data
  global score
  if user_answer == correct_answer:
    score += 1
    clear_screen()
    print(f"You're right! Current score: {score}.\n")
    index += 1
  else:
    final_message = "\n\nSorry, that's wrong. Final score: "
    index = number_of_data
    print(final_message + str(score))
 #_________________________________________________________ 
print(logo)
index = 0
while index < number_of_data:
  A()
  print(vs)
  B()
  user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  comparism()
  evaluation()

