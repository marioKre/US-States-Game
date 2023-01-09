from turtle import Screen, Turtle
import pandas

# Create turtle and screen objects
turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")

# Add a map of the USA as background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV file using pandas and convert it to list
states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()

# Create a turtle to write the names of states on the screen
state_write = Turtle()


# Defining a function to write state names on the USA map
# Function will take in text from input as parameter
def pos_write_turtle(input_state):

    # Finding coordinates of state from CSV file
    state_row = states[states.state == input_state]
    x_position = int(state_row["x"])
    y_position = int(state_row["y"])

    # Position turtle, write state name, and go to default coordinates
    state_write.hideturtle()
    state_write.penup()
    state_write.goto(x_position - 15, y_position)
    state_write.write(f"{input_state}", align="left")
    state_write.goto(0, 0)


# Initialize the score and create an empty list to store the guessed states
score = 0
guessed_states = []

# Set the game active flag to True
game_active = True

# Create a list which will be used to generate CSV containing states which are not guessed
states_to_learn = []

# Start the main game loop
while game_active:

    # Prompt the user for the name of a state, use .title() to match format of states in CSV
    answer_state = screen.textinput(
        title=f"{score}/50 States Correct!",
        prompt="Type in a state's name!\n Or type 'Exit' to close the game!",
    ).title()

    # If the user inputs "Exit", write the list of states, which are not yet guessed, to a CSV file and end loop
    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    # If the user's input is the name of a state that is not already in the list of guessed states,
    # increment the score, add the state to the list of guessed states, and write the state name on the screen
    elif answer_state in states_list and answer_state not in guessed_states:
        print("The answer is correct")
        score += 1
        guessed_states.append(answer_state)
        # If the user guesses all the states, print statement and finish the game
        if score == 50:
            print("Congrats, you typed in every state in the U.S.")
            game_active = False
        pos_write_turtle(answer_state)
