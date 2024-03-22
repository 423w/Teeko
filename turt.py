###radius found to be 16###
def turt_time():
    import turtle as t
    import math as m
    """Create a 5*5 board via turtle"""
    # This took 5 hours
    # +1 for this to read files
    r = 16
    ##get markers##
    ##set variables##
    circ = 1
    t.reset()
    t.speed(0)
    t.penup()
    t.backward(r * 5)
    t.left(90)
    t.forward(r * 6)
    t.pendown()

    ##draw circle##

    t.circle(r)
    circ += 1
    t.right(90)
    ##draw rows##
    for i in range(4):
        for i in range(4):
            t.forward(r)
            t.right(90)

            t.circle(r)
            circ += 1
            t.left(90)
            t.penup()
            t.forward(2 * r)
            t.pendown()
        ##draw column##
        t.penup()
        t.back(r)
        t.right(90)
        t.forward(r)
        t.pendown()
        t.forward(r)
        t.right(90)
        t.penup()
        t.forward(3 * r)
        t.pendown()
        t.right(90)
        t.forward(r)
        t.left(90)
        t.penup()
        t.forward(3 * r)
        t.pendown()
        t.left(90)
        t.forward(r)
        t.right(90)
        t.penup()
        t.forward(3 * r)
        t.pendown()
        t.right(90)
        t.forward(r)
        t.left(90)
        t.penup()
        t.forward(3 * r)
        t.pendown()
        t.left(90)
        t.forward(r)
        t.penup()
        t.forward(r)
        t.left(90)
        t.forward(r)
        t.left(90)
        t.pendown()
        t.circle(r)
        circ += 1
        t.right(90)
    ##Last row##
    for i in range(4):
        t.forward(r)
        t.right(90)
        t.circle(r)
        circ += 1
        t.left(90)
        t.penup()
        t.forward(r * 2)
        t.pendown()

    t.penup()
    t.left(135)

    ##Diagonal x's starting at each rx,ry##
    for ry in [7 * r, 4 * r, 1 * r, -2 * r]:
        for rx in [-2 * r, r, 4 * r, 7 * r]:
            t.right(90)
            t.setposition(rx, ry)

            t.backward(m.sqrt((r ** 2) * 2) + r)
            t.pendown()
            t.backward(m.sqrt(2 * ((3 * r) ** 2)) - 2 * r)
            t.penup()
            t.right(135)
            t.backward(r + m.sqrt((r ** 2)) / 2)
            t.right(135)
            t.pendown()
            t.backward(m.sqrt(2 * ((3 * r) ** 2)) - 2 * r)
            t.penup()

    ##set for plop##
    t.left(135)
    t.setposition(400, 0)


def turt_plop(x, y, color, speed=0, hide=True):
    """Plop a color onto a circle"""
    import turtle as t

    t.speed(speed)
    r = 16
    t.setposition(r * 3 * (x - 3) - 16, r * -3 * (y - 3))

    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()

    if hide:
        t.setposition(400, 0)


def write_win(center_x, center_y, text):
    ''' Write text on the Screen '''
    from turtle import Screen, Turtle, clear

    clear()
    board = Turtle()
    FONT = ('Comic Sans', 50, 'normal')
    board.penup()
    board.goto(center_x, center_y)
    if 'Black' in text:
        board.pencolor('black')
    if "Red" in text:
        board.pencolor('red')
    board.write(text, font=FONT, align="center")
    screen = Screen()
    screen.bgpic('explosion_gif.gif')
    board.forward(500)
    screen.exitonclick()


def write_text_keep(ypos, text, size):
    """ Write text on the Screen """
    from turtle import Screen, Turtle
    board = Turtle()
    FONT = ('Times New Roman', size, 'normal',)
    board.penup()
    board.goto(0, ypos)
    board.write(text, font=FONT, align="center")
    board.forward(500)
    screen = Screen()
