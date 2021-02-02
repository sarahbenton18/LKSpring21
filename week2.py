from tkinter import *
from tkinter import font
from PIL import ImageTk
import PIL.Image

teal = "#3C84A4"
fancy_font = 'Pristina'
s_font = 'Bell MT'
type_font = 'Courier'
comp_font = 'Candara'
gray = '#DCDBDB'


def chapter_one():
    intro_frame.destroy()

    global chapter_one_frame
    chapter_one_frame = Frame(window, bg='black')
    chapter_one_frame.pack(expand=1, fill=BOTH)

    lust_image = ImageTk.PhotoImage(PIL.Image.open("images/images2/lust.png").resize((800, 550)))
    lust_label = Label(chapter_one_frame, image=lust_image, borderwidth=5, relief='solid')
    lust_label.image = lust_image
    lust_label.place(anchor=CENTER, relx=0.5, rely=0.4)

    next_btn = Button(chapter_one_frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: intro_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def intro_one():
    chapter_one_frame.destroy()

    global intro_frame_one
    intro_frame_one = Frame(window, bg=teal)
    intro_frame_one.pack(expand=1, fill=BOTH)

    next_btn = Button(intro_frame_one, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: intro_two())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def intro_two():
    intro_frame_one.destroy()

    global intro_frame_two
    intro_frame_two = Frame(window, bg=teal)
    intro_frame_two.pack(expand=1, fill=BOTH)

    next_btn = Button(intro_frame_one, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: intro_three())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def intro_three():
    intro_frame_two.destroy()

    global intro_frame_three
    intro_frame_three = Frame(window, bg=teal)
    intro_frame_three.pack(expand=1, fill=BOTH)

    next_btn = Button(intro_frame_one, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_one():
    intro_frame_three.destroy()

    global f1
    f1 = Frame(window, bg=teal)
    f1.pack(expand=1, fill=BOTH)


if __name__ == "__main__":
    window = Tk()
    window.title("Divine Deviance Week 2")
    window.state('zoomed')

    intro_frame = Frame(window, bg=teal)
    intro_frame.pack(expand=1, fill=BOTH)

    lk_label = Label(intro_frame, text="Lock and Key Club presents...", font=(fancy_font, '50', 'bold'), bg=teal)
    lk_label.place(anchor=CENTER, relx=0.5, rely=.15)

    intro_label = Label(intro_frame, text="Divine Deviance:\nWeek Two", font=(fancy_font, '100', 'bold'),
                        borderwidth=5, relief='solid', padx=10, bg=teal)
    intro_label.place(anchor=CENTER, relx=0.5, rely=0.5)

    start_button = Button(intro_frame, text="Start", font=(fancy_font, '25', 'bold'), fg="white", bg="black",
                          command=lambda: chapter_one())
    start_button.place(anchor=CENTER, relx=0.5, rely=0.9)

    window.mainloop()
