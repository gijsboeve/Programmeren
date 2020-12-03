import turtle

window = turtle.Screen()

window.bgcolor("pink")
window.title("hoi gijs")

gijs = turtle.Turtle()
gijs.pensize(7)
gijs.speed(5)
gijs.shape("turtle")
size = 10

gijs.left(36)
colors = ("yellow", "red", "green","yellow", "red")
for color in colors:
    gijs.color(color)
    gijs.forward (100)
    gijs.left(180 - 36)

gijs.hideturtle()

window.exitonclick()


