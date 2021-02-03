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

# TODO - change so that it only accesses images2?


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def check_answer_singular(user_entry, answer, relx, rely, color, frame, next_function):
    user_entry = user_entry.lower().strip("\n")
    if user_entry == answer:
        correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
        correct_label = Label(frame, image=correct_image)
        correct_label.image = correct_image
        correct_label.place(anchor=CENTER, relx=relx + 0.15, rely=rely)

        next_btn = Button(frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg=color,
                          command=lambda: next_function())
        next_btn.place(anchor=CENTER, relx=0.65, rely=0.9)
    else:
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=relx + 0.15, rely=rely)


def check_answer_next(user_entry, answer, relx, rely, color, frame, next_function):
    user_entry = user_entry.lower()
    if (user_entry != answer) or (user_entry == "") or (user_entry == " "):
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=relx + 0.15, rely=rely)
    else:
        user_list.append(user_entry)
        correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
        correct_label = Label(frame, image=correct_image)
        correct_label.image = correct_image
        correct_label.place(anchor=CENTER, relx=relx + 0.15, rely=rely)

    for answer in answer_list:
        if answer not in user_list:
            return

    next_btn = Button(frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg=color,
                      command=lambda: next_function())
    next_btn.place(anchor=CENTER, relx=0.65, rely=0.9)


def temp():
    # TODO - change the destroy when ready
    intro_frame.destroy()

    global f3
    f3 = Frame(window, bg=teal)
    f3.pack(expand=1, fill=BOTH)

    question_frame = Frame(f3, bg=gray, borderwidth=3, relief='solid')
    question_frame.place(anchor=N, relx=0.5, rely=0.01)

    question_label = Label(question_frame, text="What is Peter's address?", font=(s_font, '25', 'bold'), bg=gray)
    question_label.pack(side=TOP, pady=(10, 5), padx=20)

    entry = Text(question_frame, height=3, font=(s_font, '22'), width=20)
    entry.pack(side=TOP, pady=(5, 10), padx=20)

    clue_font = s_font

    instructions_frame = Frame(f3, bg=teal)
    instructions_frame.place(anchor=CENTER, relx=0.5, rely=0.35)

    instructions_a = Label(instructions_frame, text="V", font=(clue_font, '25', 'bold'), underline=0, bg=teal)
    instructions_a.pack(side=LEFT)

    instructions_b = Label(instructions_frame, text="igenere: You will find your key shift if you seek \"advice "
                                                    "from a caterpillar.\" ", font=(clue_font, '25'), bg=teal)
    instructions_b.pack(side=LEFT)

    cipher_text = Label(f3, bg=teal, font=(clue_font, '25'), text="Vvrirtxlaietoes! Lru lzg hzwbq e jrxet lvp ta "
                                                                  "wfqjzfu flba omxuwz. Virr kobyg. Qhn’yi clfsji "
                                                                  "bsprv. Mvs rntsy ct dhpg gxgxizw iwfe ie yrsw re "
                                                                  "xzgwh dlf burzw gnca faalig gi ov cypvaakma "
                                                                  "ryurgsmvv, uo ivfea ez tyhzm odo kbzoe vx oa "
                                                                  "vued. Gvlcon, xum jntzv pqwao sw lhba qvpsmt arw "
                                                                  "iz bioc yhb xf yv rz Diklbfrv yxq tefl Gnnwk.",
                        wraplength=700)
    cipher_text.place(anchor=CENTER, relx=0.5, rely=0.6)



    # TODO - change next function
    submit_btn = Button(f3, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_singular(entry.get("1.0", END), "address", 0.55, 0.19, 'black', f3,
                                                              temp_next()))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def temp_next():
    pass


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
                      command=lambda: p_frame_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def p_frame_one():
    intro_frame_three.destroy()

    global fp1
    fp1 = Frame(window, bg=teal)
    fp1.pack(expand=1, fill=BOTH)


def frame_two():
    # TODO - change destroy statement
    intro_frame.destroy()

    global f2
    f2 = Frame(window, bg=teal)
    f2.pack(expand=1, fill=BOTH)

    global answer_list
    answer_list = ["sparkling", "square", "brown", "promises", "raven's wing", "sex maniac"]

    global user_list
    user_list = []

    description = Label(f2, text="You find a collection of books with the letter. Flipping through their pages, you "
                                 "notice that there are a number of highlighted sentences, but some words are smudged"
                                 " from what appear to be tear stains. Ghost Lady is embarrassed that you found "
                                 "her \"shrine\" to Peter and doesn't say anything more. You need to find Peter,"
                                 " so you reason that figuring out these missing words will help you to build "
                                 "a better picture of Peter.", wraplength=1100, font=(s_font, '22'), bg=teal)
    description.place(anchor=N, relx=0.5, rely=0.01)

    sentence_frame = Frame(f2, bg=gray, borderwidth=3, relief='solid')
    sentence_frame.place(anchor=CENTER, relx=0.5, rely=0.55)

    puzzle_font = s_font
    puzzle_font_size = '22'
    padding_x = 10
    padding_y = (0, 5)

    row_zero = Label(sentence_frame, text="From your research, you discover that Peter...",
                     font=(puzzle_font, puzzle_font_size, 'bold'), bg=gray)
    row_zero.pack(side=TOP, pady=(5, 0))

    row_half = Frame(sentence_frame, bg=gray)
    row_half.pack(side=TOP, pady=padding_y)

    row_half_a = Label(row_half, text="has the ", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_half_a.pack(side=LEFT)

    row_half_b = Entry(row_half, font=(puzzle_font, puzzle_font_size), width=15)
    row_half_b.pack(side=LEFT)

    row_half_c = Label(row_half, text=" jaw of Watson,", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_half_c.pack(side=LEFT)

    row_one = Frame(sentence_frame, bg=gray)
    row_one.pack(side=TOP, pady=padding_y)

    row_one_a = Label(row_one, text="the ", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_one_a.pack(side=LEFT)

    row_one_b = Entry(row_one, font=(puzzle_font, puzzle_font_size), width=15)
    row_one_b.pack(side=LEFT)

    row_one_c = Label(row_one, text=" skin of Cullen,", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_one_c.pack(side=LEFT)

    row_two = Frame(sentence_frame, bg=gray)
    row_two.pack(side=TOP, pady=padding_y)

    row_two_a = Label(row_two, text="the ", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_two_a.pack(side=LEFT)

    row_two_b = Entry(row_two, font=(puzzle_font, puzzle_font_size), width=15)
    row_two_b.pack(side=LEFT)

    row_two_c = Label(row_two, text=" eyes of Darcy,", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_two_c.pack(side=LEFT)

    row_three = Frame(sentence_frame, bg=gray)
    row_three.pack(side=TOP, pady=padding_y, padx=padding_x)

    row_three_a = Label(row_three, text="a heightened sensitivity for the ",
                        font=(puzzle_font, puzzle_font_size), bg=gray)
    row_three_a.pack(side=LEFT)

    row_three_b = Entry(row_three, font=(puzzle_font, puzzle_font_size), width=15)
    row_three_b.pack(side=LEFT)

    row_three_c = Label(row_three, text=" of life like a young Gatsby,", font=(puzzle_font, puzzle_font_size),
                        bg=gray)
    row_three_c.pack(side=LEFT)

    row_four = Frame(sentence_frame, bg=gray)
    row_four.pack(side=TOP, pady=padding_y)

    row_four_a = Label(row_four, text="hair as dark as a ", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_four_a.pack(side=LEFT)

    row_four_b = Entry(row_four, font=(puzzle_font, puzzle_font_size), width=15)
    row_four_b.pack(side=LEFT)

    row_four_c = Label(row_four, text=" like Dantes,", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_four_c.pack(side=LEFT)

    row_five = Frame(sentence_frame, bg=gray)
    row_five.pack(side=TOP, pady=padding_y)

    row_five_a = Label(row_five, text="and is the biggest ",
                       font=(puzzle_font, puzzle_font_size), bg=gray)
    row_five_a.pack(side=LEFT)

    row_five_b = Entry(row_five, font=(puzzle_font, puzzle_font_size), width=15)
    row_five_b.pack(side=LEFT)

    row_five_c = Label(row_five, text=" you ever saw like Caulfield,", font=(puzzle_font, puzzle_font_size),
                       bg=gray)
    row_five_c.pack(side=LEFT)

    # TODO - change next function
    submit_btn = Button(f2, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_answer_next(row_half_b.get(), "square", 0.75, 0.4,
                                                                        'black', f2, temp_next()),
                                                      check_answer_next(row_one_b.get(), "sparkling", 0.75, 0.47,
                                                                        'black', f2, temp_next()),
                                                      check_answer_next(row_two_b.get(), "brown", 0.75, 0.54,
                                                                        'black', f2, temp_next()),
                                                      check_answer_next(row_three_b.get(), "promises", 0.75, 0.61,
                                                                        'black', f2, temp_next()),
                                                      check_answer_next(row_four_b.get(), "raven's wing", 0.75, 0.68,
                                                                        'black', f2, temp_next()),
                                                      check_answer_next(row_five_b.get(), "sex maniac", 0.75, 0.75,
                                                                        'black', f2, temp_next())))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


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
                          command=lambda: temp())
    start_button.place(anchor=CENTER, relx=0.5, rely=0.9)

    window.mainloop()
