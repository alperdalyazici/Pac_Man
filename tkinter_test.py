import time
import turtle
from tkinter import *
import random

global score, lifes
score = 0
lifes = 3
global read_score, read_life
#Instructions of the Game
def game_describtion():
    description = Tk()
    description.title("Game Describtion")
    description.geometry("800x600")
    description.configure(bg = "black")
    a = Label(description, text = "Here is how the game is played: ", font = "italic, 20", fg = "red", bg = "black").grid(row = 0, column = 0)
    space1 = Label(description, text = "                     ", bg = "black", anchor = "nw").grid(row = 1, column = 0)
    game_exp1 = Label(description, text = "The purpose of this game is to collect the foods using your pacman. ", font = "italic, 15", fg = "white", bg = "black", anchor = "nw").grid(row = 2, column = 0)
    game_exp2 = Label(description, text = "Everytime you collect a food, your score increases by 1 point. ", font = "italic, 15", fg = "white", bg = "black", anchor = "nw").grid(row = 3, column = 0)
    game_exp3 = Label(description, text = "When you hit a ghost or go out of bounds, your life decreases by 1. ", font = "italic, 15", fg = "white", bg = "black", anchor = "nw").grid(row = 4, column = 0)
    space2 = Label(description, text = "                     ", bg = "black", anchor = "nw").grid(row = 5, column = 0)
    game_exp4 = Label(description, text = "   Once your score is 140, you beat the game but if your life runs out, you lose!!!! ", font = "italic, 15", fg = "white", bg = "black", anchor = "nw").grid(row = 6, column = 0)
    game_exp5 = Label(description, text = "      Click the button below to view the controls. ", font = "italic, 15", fg = "white", bg = "black", anchor = "nw").grid(row = 7, column = 0)
    space3 = Label(description, text = "                     ", bg = "black", anchor = "nw").grid(row = 8, column = 0)
    control_button = Button(description, text = "Controls", command = controls).grid(row = 9, column = 0)

#Exit button
def exit():
    main_window.quit()

#Control Keys of the Game
def controls():
    controls = Tk()
    controls.title("Game Controls")
    controls.geometry("800x300")
    controls.configure(bg="black")
    explanation = Label(controls, text="Here are the control settings of the game: ", font="italic, 20", fg="red", bg="black").grid(row=0,column=0)
    cont_exp1 = Label(controls, text="You control the pacman movement with your up, down , left and right arrow keys.", font="italic, 15", fg="white", bg="black").grid(row=1,column=0)
    cont_exp2 = Label(controls, text="The pause button is the letter \"a\" . ", font="italic, 15", fg="white", bg="black").grid(row=2,column=0)
    cont_exp3 = Label(controls, text="The cheat button is the letter \"c\" but I don't recommend it since we have cheaters!! ", font="italic, 15", fg="white", bg="black").grid(row=3,column=0)

#The PacMan Game
def game_initialize():
    global score, lifes

    score = 0
    lifes = 3

    main_window.destroy()
    game_window = turtle.Screen()
    game_window.bgcolor("black")
    game_window.setup(width=1280, height=720)
    game_window.title("Pac-Man Game")
    game_window.tracer(0)

    pacman = turtle.Turtle()
    turtle.register_shape('pacmanfigure.gif')
    pacman.shape('pacmanfigure.gif')
    pacman.speed(0.7)
    pacman.goto(0,0)
    pacman.penup()
    pacman.direction = "stop"

    status_pen = turtle.Turtle()
    status_pen.color("blue")
    status_pen.speed(0)
    status_pen.penup()
    status_pen.goto(0, 280)
    status_pen.pendown()
    status_pen.write("Score: " + str(score) + "   " + "Lifes: " + str(lifes), align="center", font="Ariel, 38")
    status_pen.hideturtle()

#Pam Man directions
    def pac_up():
        pacman.direction = "up"
    def pac_down():
        pacman.direction = "down"
    def pac_left():
        pacman.direction = "left"
    def pac_right():
        pacman.direction = "right"

#Pacman movement
    def pac_movement():
        if pacman.direction == "up":
            y = pacman.ycor()
            y +=1.5
            pacman.sety(y)

        elif pacman.direction == "down":
            y = pacman.ycor()
            y -=1.5
            pacman.sety(y)
        elif pacman.direction == "right":
            x = pacman.xcor()
            x +=1.5
            pacman.setx(x)
        elif pacman.direction == "left":
            x = pacman.xcor()
            x -=1.5
            pacman.setx(x)

#Key Buttons
    game_window.listen()
    game_window.onkeypress(pac_up, "Up")
    game_window.onkeypress(pac_down, "Down")
    game_window.onkeypress(pac_left, "Left")
    game_window.onkeypress(pac_right, "Right")

#Creating the foods

    pac_foods = []
    for i in range(35):
        food = turtle.Turtle()
        food.shape("circle")
        food.shapesize(stretch_wid=0.5, stretch_len=0.5)
        food.color("orange")
        food.penup()
        food.speed(0)
        y = random.randint(-350, 350)
        x = random.randint(-620, 620)
        food.setposition(x, y)
        pac_foods.append(food)

#Creating the ghosts

    ghosts = []
    for y in range(6):
        ghost = turtle.Turtle()
        turtle.register_shape("ghost.gif")
        ghost.shape("ghost.gif")
        ghost.speed(0.7)
        ghost.penup()
        y = random.randint(-350, 350)
        x = random.randint(-620, 620)
        ghost.setposition(x, y)
        ghosts.append(ghost)

#Spawning more ghost function

    def create_ghosts():
        for y in range(4):
            ghost = turtle.Turtle()
            turtle.register_shape("ghost.gif")
            ghost.shape("ghost.gif")
            ghost.speed(0.7)
            ghost.penup()
            y = random.randint(-350, 350)
            x = random.randint(-620, 620)
            ghost.setposition(x, y)
            ghosts.append(ghost)

#Created the cheat button

    def cheat_button():
          for ghost in ghosts:
              ghost.hideturtle()

    initial_speed = 0.4

#Created the pause button

    def pause_button():
        pacman.direction = "stop"
        for ghost in ghosts:
            ghost.speed(0)
            initial_speed = 0

#Pause function for loop
    def pause():
          if pacman.direction == "stop":
              pacman.direction = "stop"

#The Boss Key
    def boss_key():
        game_window.bye()
        boss_window = Tk()
        boss_window.title("You are currently working!!!!")
        boss_window.geometry("1280x720")
        boss_image = PhotoImage(file="bosskey.png")
        boss_canvas = Canvas(boss_window, width=1280, height=720)
        boss_canvas.pack(fill="both", expand=True)
        boss_canvas.create_image(0, 0, image=boss_image, anchor="nw")
        boss_window.mainloop()

#Save Function
    def save():
        save_file = open("saveload.txt", "w")
        save_file.write(str(pacman.xcor()))
        save_file.write("\n" +str(pacman.ycor()))
        save_file.write("\n"+ str(score))
        save_file.write("\n" + str(lifes))
        for ghost in ghosts:
            save_file.write("\n" +str(ghost.xcor()))
            save_file.write("\n" +str(ghost.ycor()))

#Load Function
    def load():
        global score, lifes
        load_file = open("saveload.txt", "r")
        x = float(load_file.readline())
        y = float(load_file.readline())
        read_score = int(load_file.readline())
        read_life = int(load_file.readline())
        for ghost in ghosts:
            a = float(load_file.readline())
            b = float(load_file.readline())
            ghost.goto(a,b)
        status_pen.clear()
        score = int(read_score)
        lifes = int(read_life)

        status_pen.write("Score: " + str(score) + "   " + "Lifes: " + str(lifes), align="center",
                             font="Ariel, 38")

        pacman.goto(x,y)


#More key presses
    game_window.listen()
    game_window.onkeypress(cheat_button, "c")
    game_window.onkeypress(pause_button, "p")
    game_window.onkeypress(boss_key, "b")
    game_window.onkeypress(save, "s")
    game_window.onkeypress(load, "l")

#Ghost Movement
    def ghost_movement():
        for ghost in ghosts:
            x = ghost.xcor()
            y = ghost.ycor()
            x += initial_speed
            y += initial_speed
            ghost.setx(x)
            ghost.sety(y)

#Creating more food on next levels
    def create_food():
        for i in range(35):
            food = turtle.Turtle()
            food.shape("circle")
            food.shapesize(stretch_wid=0.5, stretch_len=0.5)
            food.color("orange")
            food.penup()
            food.speed(0)
            y = random.randint(-350, 350)
            x = random.randint(-620, 620)
            food.setposition(x, y)
            pac_foods.append(food)

#the main loop of the game
    while True:
        game_window.update()
        pac_movement()

        if pacman.direction == "stop":
            pause()
        else:
            ghost_movement()

#Ghost-Border Collision
        for ghost in ghosts:
            if ghost.ycor()> 405:
                y = random.randint(-350, 350)
                x = random.randint(-620, 620)
                ghost.goto(x, y)

            if ghost.ycor()< -405:
                y = random.randint(-350, 350)
                x = random.randint(-620, 620)
                ghost.goto(x, y)

            if ghost.xcor()> 685:
                y = random.randint(-350, 350)
                x = random.randint(-620, 620)
                ghost.goto(x, y)

            if ghost.xcor()< -685:
                y = random.randint(-350, 350)
                x = random.randint(-620, 620)
                ghost.goto(x, y)

#Ghost-Pacman collision
        for ghost in ghosts:
            if pacman.distance(ghost)<50:
                lifes -=1
                status_pen.clear()
                status_pen.write("Score: " + str(score) + "   " + "Lifes: " + str(lifes), align="center", font="Ariel, 38")
                time.sleep(1)
                pacman.goto(0,0)
                for ghost in ghosts:
                    y = random.randint(-350, 350)
                    x = random.randint(-620, 620)
                    ghost.goto(x, y)

#Game over function
        if lifes == 0:
            game_window.bye()
            gameover_window = Tk()
            gameover_window.title("Game Over!!!!")
            gameover_window.geometry("400x200")
            gameover_window.configure(bg="black")
            gameover_text = Label(gameover_window, text="The game is now over you ran out of lifes!!!", font="italic, 10", fg="white", bg="black").grid(row=0, column=0)
            score_text = Label(gameover_window, text="Your score was: " + str(score), font="italic, 10", fg="white", bg="black").grid(row=1, column= 0)
            username = Entry(gameover_text, width = 20).grid(row = 2, column = 0)
            def user_save():
                user_text = username.get()
                file = open("leaderboard.txt", "a")
                file.write(username_text)
                print(username_text)
            username_save = Button(gameover_window, text = "Save",command = user_save).grid(row = 3, column = 0)

#Completed the game function
        if score >= 105:
            time.sleep(1)
            game_window.bye()
            win_window = Tk()
            win_window.title("Game Completed!!!!")
            win_window.geometry("400x200")
            win_window.configure(bg="black")
            win_text = Label(win_window, text="Congrats!! You beat the Pac Man Game.",font="italic, 10", fg="white", bg="black").grid(row=0, column=0)
            click_text = Label(win_window, text="Click below to return to the main window", font="italic, 10",fg="white", bg="black").grid(row=1, column=0)
            gotomainwindow_button = Button(win_window, text="Click").grid(row=3, column=0)

#Pacman-Border Collision
        if pacman.xcor()<-695 or pacman.xcor()>695 or pacman.ycor()<-415 or pacman.ycor()>415:
            lifes -=1
            status_pen.clear()
            status_pen.write("Score: " + str(score) + "   " + "Lifes: " + str(lifes), align="center", font="Ariel, 38")
            time.sleep(0.5)
            pacman.goto(0,0)

#Pacman-food collision
        for food in pac_foods:
            if pacman.distance(food) < 40:
                food.goto(1500,1500)
                score +=1
                status_pen.clear()
                status_pen.write("Score: " + str(score) + "   " + "Lifes: " + str(lifes), align="center",
                                 font="Ariel, 38")

                if (score % 35) ==0 and score != 0:
                    create_food()
                    create_ghosts()


#The Main Screen
main_window = Tk()
main_window.title("Pac-Man Main Screen")
main_window.geometry("1280x720")
background = PhotoImage(file="pacman.png")

bg_canvas = Canvas(main_window, width=1280, height=720)

bg_canvas.pack(fill="both", expand=True)

bg_canvas.create_image(0, 0, image=background, anchor="nw")

bg_canvas.create_text(670, 38, text="Welcome to the Pac Man Game !", font=("Ariel", 30), fill="white")

start_button = Button(main_window, text="Start", padx=25, command=game_initialize)
exit_button = Button(main_window, text="Exit", padx=20, command=exit)
settings_button = Button(main_window, text="Settings", padx=20, command=game_describtion)

start_button_window = bg_canvas.create_window(515, 305, window=start_button)
exit_button_window = bg_canvas.create_window(650, 305, window=exit_button)
settings_button_window = bg_canvas.create_window(780, 305, window=settings_button)

main_window.mainloop()


