import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = []

while len(correct_answers) < 50:
#create a window for user's input
    answer_state = screen.textinput(title=f"Correct states: {len(correct_answers)}/50", prompt="What's another state's name?")
    title_case_answer = answer_state.title()
    print(title_case_answer,"\n_________")

#check if the guess is in the States column
    data = pandas.read_csv("50_states.csv")
    list_of_states = data.state.to_list()

    if title_case_answer == "Exit":
        break
    if title_case_answer in list_of_states:

        #get the state's coordinates
        row = data[data.state == title_case_answer]
        x_coordinate = row["x"].values[0]
        y_coordinate = row["y"].values[0]

        #write the correct guess on the map
        if title_case_answer not in correct_answers:
            state = turtle.Turtle()
            state.up()
            state.hideturtle()
            print(x_coordinate, y_coordinate)
            state.goto(x_coordinate, y_coordinate)
            state.write(title_case_answer)
            correct_answers.append(title_case_answer)

            print(correct_answers)

states_left = data.state
mask = ~data['state'].isin(correct_answers)
states_left = pandas.DataFrame(states_left[mask])
states_left = states_left.reset_index(drop=True)
print(states_left)
states_left.to_csv("states_to_learn.csv")


screen.bye()
