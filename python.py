data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    }]

number_of_data = len(data)
correct_answer = " "

def A():
  print("Compare A: ")
  data_to_display = data[index] 
  print(data_to_display["name"] +"\n", 
 data_to_display["description"] +"\n", "From " + data_to_display["country"])

def B():
  print("Against B: ")
  data_to_display = data[index+1]
  print(data_to_display["name"] +"\n", 
 data_to_display["description"] +"\n", "From " + data_to_display["country"])

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
  score = 0
  global user_answer
  global correct_answer
  global index
  global number_of_data
  if user_answer == correct_answer:
    print(f"You're right! Current score: {score}.")
    index += 1
  else:
    final_message = "Sorry, that's wrong. Final score: "
    index = number_of_data
    return final_message
 #_________________________________________________________ 

index = 0
while index < number_of_data:
  A()
  B()
  user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  comparism()
  evaluation()

 
