from tkinter import *

main_window = Tk()
main_window.title("Pac-Man Main Screen")
main_window.geometry("1280x720")
background = PhotoImage(file="pacman.png")

bg_canvas = Canvas(main_window, width=1280, height=720)

bg_canvas.pack(fill="both", expand=True)

bg_canvas.create_image(0, 0, image=background, anchor="nw")

bg_canvas.create_text(670, 38, text="Welcome to the Pac Man Game !", font=("Ariel", 30), fill="white")