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


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion = (-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill = "black")
    page.create_line(0, -y_origin, 0, y_origin, fill = "black")


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill = "red")


main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width = 640, height = 480)
canvas.grid(row = 0, column = 0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

main_window.mainloop()