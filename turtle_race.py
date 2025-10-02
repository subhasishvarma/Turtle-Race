import turtle as t
import random
t.colormode(255)

def speed_gen():
    speeds = [10,15,5]
    return random.choice(speeds)

def color_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return [r,g,b]

def turt_defn(i):
    turts = []
    for _ in range(1,i+1):
        turtle = t.Turtle()
        turtle.color(color_rgb())
        turtle.shape("turtle")
        turts.append(turtle)
    return turts

def turt_ini(turts,i):
    j=0
    for turt in turts:
        turt.penup()
        turt.goto(-380,250-j*(500/(i-1)))
        j=j+1
        turt.pendown()

def race(turts):
    cond=True 
    while cond:
        for turt in turts:
            if turt.xcor() == 380:
                won_turt = turt
                cond=False
                break
            turt.forward(speed_gen())
    return turts.index(won_turt)+1
    


user_number = int(t.numinput("No of Turt's", "Please enter number of turtles in the race:", default = 5, minval=2, maxval=10))


turtles = turt_defn(user_number)
turt_ini(turtles,user_number)

bet_turt = int(t.textinput("Bet", f"Which one u wanna bet on? Choose number between 1 and {user_number}"))

screen = t.Screen()
screen.setup(width=800, height=600)

won = race(turtles)

if won == bet_turt:
    t.write(f"Your bet on {bet_turt} was Sucessfull", font=("Arial", 16, "normal"))

else:
    t.write(f"Your bet on {bet_turt} was Unsucessfull", font=("Arial", 16, "normal"))




screen.mainloop()
screen.exitonclick()