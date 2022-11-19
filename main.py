import turtle
import pandas

# Use turtle.Screen to set up screen for the game
screen = turtle.Screen()
screen.title('African Countries Games')
screen_image = './african_countries.gif'
screen.addshape(screen_image)
turtle.shape(screen_image)

# Read the .csv data for the game with Pandas
data = pandas.read_csv('./african_countries.csv')
countries_data = data.country.to_list()
correct_guesses = []

while len(correct_guesses) < 53:
    answer = screen.textinput(title=f'{len(correct_guesses)}/53 Countries Guessed',
                              prompt='What is another country?').title()

    if answer == 'exit'.title():
        missing_countries = []
        for country in countries_data:
            if country not in correct_guesses:
                missing_countries.append(country)
        countries_missed = pandas.DataFrame(missing_countries)
        countries_missed.to_csv('./missing_countries.csv')
        break

    if answer in countries_data:
        correct_guesses.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        xy_cord = data[data.country == answer]
        t.goto(int(xy_cord.x), int(xy_cord.y))
        t.write(answer)
