import turtle
import pandas
screen = turtle.Screen()
screen.title("Us state game")
image = "./project 24/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("project 24/50_states.csv")
all_state = data.state.to_list()
guessed_state = []



while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess state name", prompt="Tell another state name?").title()
    
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)

        df = pandas.DataFrame(missing_state)
        df.to_csv("project 24/states_to_learn.csv")
        break  

    if answer_state in all_state:
        guessed_state.append(answer_state)

        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)

        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.pendown()
        new_turtle.write(answer_state)
        # new_turtle.write(state_data.state.item()) ## - Series.item()

# states_to_learn.csv

