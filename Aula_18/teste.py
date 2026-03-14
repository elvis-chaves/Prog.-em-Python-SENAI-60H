import tkinter as tk

def gradient(canvas, width, height, color1, color2):
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))

        color = "#%04x%04x%04x" % (nr, ng, nb)
        canvas.create_line(0, i, width, i, fill=color)

root = tk.Tk()
root.title("Gradiente no Tkinter")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

gradient(canvas, 400, 300, "#ff7e5f", "#feb47b")

root.mainloop()