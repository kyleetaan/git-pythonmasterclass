#! python 3
# def center_text(*args, sep = " ", end = "\n", flush = False):
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, end=end, flush=flush)

# center_text("hatdog", "footlong", 2, 3, 4, "spam", sep = ", ")
# center_text("spam", "bacon", 2, 3, 4, "spam", sep = ", ")
# center_text("hatdog", "footlong", 2, 3, 4, "spam", sep = ", ")

import tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion = (-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill = "black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill = "black")


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill = "red")


main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width = 640, height = 480)
canvas.grid(row = 0, column = 0)

draw_axes(canvas)

for i in range(-1000, 1000):
    x = parabola(i)
    print(i,x)
    plot(canvas, i, -x )

main_window.mainloop()