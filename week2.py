from tkinter import *
from tkinter import font
from PIL import ImageTk
import PIL.Image

pink = '#FCAEE5'
fancy_font = 'Edwardian Script ITC'
s_font = 'Bell MT'
type_font = 'Courier'
comp_font = 'Candara'
gray = '#DCDBDB'

# possible fonts
# 'Bookman Old Style'
# 'Edwardian Script ITC Regular'
# 'Kunstler Script Regular'
# 'Lucida Handwriting Italic'

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
    pass


def temp_next():
    pass


def intro_one():
    intro_frame.destroy()

    global intro_frame_one
    intro_frame_one = Frame(window, bg='black')
    intro_frame_one.pack(expand=1, fill=BOTH)

    description = Label(intro_frame_one, text="\tA week or so has passed since you watched Howard Sullivan's ghost"
                                              " disappear before your eyes. Having heard nothing from the Society of"
                                              " Divine Deviance since then, you begin to think that you are never "
                                              "going to get any answers. Then, one day, as you’re taking a "
                                              "mid-afternoon stroll through the park, you notice a rather gaunt female"
                                              " figure approaching you. You are initially startled, but something about"
                                              " the longing on her face makes you want to ask her if she’s okay.\n\t"
                                              "\"I heard you know how to help people like me,\" she says. "
                                              "You can only assume this woman has been presented to you as your "
                                              "next assignment. Intrigued, you ask her what she needs.\n\t\"My name is "
                                              "Elaine. I was a "
                                              "librarian for 30 years, and I gave my entire life to my work. I never"
                                              " had time for a real relationship, except maybe with the narratives "
                                              "of my favorite authors. Yes, I’d been with my fair share of suitors, "
                                              "but I told myself it was all just lust. It was all just for kicks."
                                              " I never let myself connect on a deeper level. That was, until I met"
                                              " Peter.\n\t\"Having familiarized myself with nearly every literary "
                                              "leading man there is, I know a catch when I see one, and I can tell"
                                              " you that Peter was a prize. Not just a catch, but I realize now that"
                                              " Peter was the one. I never had the guts to admit my true feelings for"
                                              " him in my lifetime. I never knew what to say, so that’s why I wrote "
                                              "him a letter. Please, find my letter and deliver it to Peter so I can"
                                              " finally be at peace.\"", wraplength=1000, font=(s_font, '19'),
                        justify=LEFT, bg='black', fg='white')
    description.place(anchor=CENTER, relx=0.5, rely=0.45)

    next_btn = Button(intro_frame_one, text="Next", font=(fancy_font, '25', 'bold'), fg='black', bg='white',
                      command=lambda: chapter_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def chapter_one():
    intro_frame_one.destroy()

    global chapter_one_frame
    chapter_one_frame = Frame(window, bg='black')
    chapter_one_frame.pack(expand=1, fill=BOTH)

    lust = ImageTk.PhotoImage(PIL.Image.open("images/images2/rose_background1.jpg"))
    chapter_one_frame.lust = lust
    w = lust.width()
    h = lust.height()

    lust_canvas = Canvas(chapter_one_frame, width=w, height=h, highlightthickness=0)
    lust_canvas.place(anchor=CENTER, relx=0.5, rely=0.5)

    lust_canvas.create_image(0, 0, anchor=NW, image=lust)

    lust_canvas.create_text(w / 2 - 47, h / 2 + 228, anchor=S, text="Lust", font=(fancy_font, '250', 'bold'), fill='black',
                            justify=CENTER)
    lust_canvas.create_text(w / 2 - 50, h / 2 + 225, anchor=S, text="Lust", font=(fancy_font, '250', 'bold'), fill='white',
                            justify=CENTER)
    lust_canvas.create_text(w / 2 + 3, h / 2 - 197, anchor=CENTER, text="Chapter 2", font=(fancy_font, '100', 'bold'),
                            fill='black', justify=CENTER)
    lust_canvas.create_text(w / 2, h / 2 - 200, anchor=CENTER, text="Chapter 2", font=(fancy_font, '100', 'bold'),
                            fill='white', justify=CENTER)

    next_btn = Button(chapter_one_frame, text="Start", font=(fancy_font, '40', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.85)


def p_frame_one():
    chapter_one_frame.destroy()

    global fp
    if fp.winfo_exists():
        fp.destroy()
    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.425)

    picture_label = Label(picture_frame, text="You hop in the car with Elaine so she can lead you to the spot where "
                                              "she left the letter before she died.",
                          font=(s_font, '22', 'bold'), wraplength=1100, bg=pink)
    picture_label.pack(side=TOP)

    picture_label2 = Label(picture_frame, text="Follow her directions:", font=(fancy_font, '35', 'bold'),
                           wraplength=1100, bg=pink)
    picture_label2.pack(side=TOP)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/start.png").resize((450, 400)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=TOP)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_two())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def p_frame_two():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p1.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p2.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_one(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_three())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_three():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p3.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p4.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_two(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_four())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_four():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p5.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p6.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_three(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_five())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_five():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p7.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p8.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_four(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_six())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_six():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p9.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p10.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_five(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_seven())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_seven():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p11.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p12.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_six(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_eight())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_eight():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p13.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p14.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_seven(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_nine())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_nine():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p15.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p16.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_eight(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_ten())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_ten():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p17.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p18.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_nine(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_eleven())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_eleven():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p19.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p20.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_ten(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_twelve())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_twelve():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p21.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p22.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_eleven(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_thirteen())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_thirteen():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p23.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p24.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_twelve(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_fourteen())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_fourteen():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p25.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p26.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_thirteen(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_sixteen())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_fifteen():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p25.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p26.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_fourteen(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_sixteen())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_sixteen():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p27.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p28.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_fifteen(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_seventeen())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_seventeen():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p29.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p30.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_sixteen(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_eighteen())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_eighteen():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p31.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p32.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_seventeen(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_nineteen())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_nineteen():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p33.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p34.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_eighteen(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_twenty())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def p_frame_twenty():
    global fp
    fp.destroy()

    fp = Frame(window, bg=pink)
    fp.pack(expand=1, fill=BOTH)

    picture_frame = Frame(fp, bg=pink)
    picture_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    picture_img = ImageTk.PhotoImage(PIL.Image.open("images/images2/p35.png").resize((500, 300)))
    img = Label(picture_frame, image=picture_img, bg='black', borderwidth=3)
    img.image = picture_img
    img.pack(side=LEFT, padx=20)

    picture_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images2/p36.png").resize((500, 300)))
    img2 = Label(picture_frame, image=picture_img2, bg='black', borderwidth=3)
    img2.image = picture_img2
    img2.pack(side=LEFT, padx=20)

    instructions = Label(fp, text="You finally make it to the letter.", font=(fancy_font, '35', 'bold'), bg=pink)
    instructions.place(anchor=CENTER, relx=0.5, rely=0.75)

    prev_btn = Button(fp, text="Previous", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: p_frame_nineteen(), padx=5)
    prev_btn.place(anchor=CENTER, relx=0.45, rely=0.9)

    next_btn = Button(fp, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_two())
    next_btn.place(anchor=CENTER, relx=0.55, rely=0.9)


def frame_two():
    fp.destroy()

    global f2
    f2 = Frame(window, bg=pink)
    f2.pack(expand=1, fill=BOTH)

    global answer_list
    answer_list = ["skin", "square", "brown", "promises", "raven's wing", "sex maniac"]

    global user_list
    user_list = []

    description = Label(f2, text="You find a collection of books with the letter. Flipping through their pages, you "
                                 "notice that there are a number of highlighted sentences, but some words are smudged"
                                 " from what appear to be tear stains. Elaine is embarrassed that you found "
                                 "her \"shrine\" to Peter and doesn't say anything more. You need to find Peter,"
                                 " so you reason that figuring out these missing words will help you to build "
                                 "a better picture of Peter.", wraplength=1100, font=(s_font, '22'), bg=pink)
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

    row_one_a = Label(row_one, text="the sparkling ", font=(puzzle_font, puzzle_font_size), bg=gray)
    row_one_a.pack(side=LEFT)

    row_one_b = Entry(row_one, font=(puzzle_font, puzzle_font_size), width=15)
    row_one_b.pack(side=LEFT)

    row_one_c = Label(row_one, text=" of Cullen,", font=(puzzle_font, puzzle_font_size), bg=gray)
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

    row_five_c = Label(row_five, text=" you ever saw like Caulfield.", font=(puzzle_font, puzzle_font_size),
                       bg=gray)
    row_five_c.pack(side=LEFT)

    submit_btn = Button(f2, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_answer_next(row_half_b.get(), "square", 0.75, 0.4,
                                                                        'black', f2, frame_three),
                                                      check_answer_next(row_one_b.get(), "skin", 0.75, 0.47,
                                                                        'black', f2, frame_three),
                                                      check_answer_next(row_two_b.get(), "brown", 0.75, 0.54,
                                                                        'black', f2, frame_three),
                                                      check_answer_next(row_three_b.get(), "promises", 0.75, 0.61,
                                                                        'black', f2, frame_three),
                                                      check_answer_next(row_four_b.get(), "raven's wing", 0.75, 0.68,
                                                                        'black', f2, frame_three),
                                                      check_answer_next(row_five_b.get(), "sex maniac", 0.75, 0.75,
                                                                        'black', f2, frame_three)))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_three():
    f2.destroy()

    global f3
    f3 = Frame(window, bg=pink)
    f3.pack(expand=1, fill=BOTH)

    question_frame = Frame(f3, bg=gray, borderwidth=3, relief='solid')
    question_frame.place(anchor=N, relx=0.5, rely=0.01)

    question_label = Label(question_frame, text="What is Peter's email address?", font=(s_font, '25', 'bold'), bg=gray)
    question_label.pack(side=TOP, pady=(10, 5), padx=20)

    entry = Text(question_frame, height=3, font=(s_font, '22'), width=23)
    entry.pack(side=TOP, pady=(5, 10), padx=20)

    clue_font = s_font

    instructions_frame = Frame(f3, bg=pink)
    instructions_frame.place(anchor=CENTER, relx=0.5, rely=0.35)

    instructions_a = Label(instructions_frame, text="V", font=(clue_font, '25', 'bold'), underline=0, bg=pink)
    instructions_a.pack(side=LEFT)

    instructions_b = Label(instructions_frame, text="igenere: You will find your key shift if you seek \"advice "
                                                    "from a caterpillar.\" ", font=(clue_font, '25'), bg=pink)
    instructions_b.pack(side=LEFT)

    cipher_text = Label(f3, bg=pink, font=(clue_font, '25'), text="Vvrirtxlaietoes! Lru lzg hzwbq e jrxet lvp ta "
                                                                  "wfqjzfu flba omxuwz. Virr kobyg. Qhn’yi clfsji "
                                                                  "bsprv. Mvs rntsy ct dhpg gxgxizw iwfe ie yrsw re "
                                                                  "xzgwh dlf burzw gnca faalig gi ov cypvaakma "
                                                                  "ryurgsmvv, uo ivfea ez tyhzm odo kbzoe vx oa "
                                                                  "vued. Gvlcon, xum jntzv pqwao sw lhba qvpsmt arw "
                                                                  "iz bioc yhb xf yv rz Diklbfrv yxq tefl Gnnwk.",
                        wraplength=700)
    cipher_text.place(anchor=CENTER, relx=0.5, rely=0.6)

    submit_btn = Button(f3, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_singular(entry.get("1.0", END), "collettpeter91@gmail.com", 0.6,
                                                              0.19, 'black', f3, frame_four))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_four():
    f3.destroy()

    global f4
    f4 = Frame(window, bg=pink)
    f4.pack(expand=1, fill=BOTH)

    msg_frame = Frame(f4, bg=pink)
    msg_frame.place(anchor=CENTER, relx=0.5, rely=0.3)

    description = Label(msg_frame, text="Now with a means to contact Peter, you decide to send him the following "
                                        "message (actually do it):", bg=pink, wraplength=1000,
                        font=(s_font, '25', 'bold'))
    description.pack(side=TOP)

    message = Label(msg_frame, text="\"Hi Peter, I know Elaine and she asked me to get in touch with you. I have"
                                    " something to give to you from her - I don’t know her very well but it seems"
                                    " very important to her that you receive this letter. I was wondering if we could"
                                    " arrange a place to meet up so that I can deliver it. I hope to hear from you "
                                    "soon.\"", font=(s_font, '25'), wraplength=800, justify=CENTER, bg=pink)
    message.pack(side=TOP, pady=(30, 0))

    question_frame = Frame(f4, bg=gray, borderwidth=3, relief='solid')
    question_frame.place(anchor=CENTER, relx=0.5, rely=0.7)

    question = Label(question_frame, text="What is in the signature line of Peter's reply?", bg=gray,
                     font=(s_font, '25'))
    question.pack(side=TOP, padx=10, pady=(10, 5))

    entry = Entry(question_frame, font=(s_font, '25'), width=20)
    entry.pack(side=TOP, pady=(5, 10))

    submit_btn = Button(f4, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_singular(entry.get(), "\"go ahead, make my day.\"", 0.65, 0.75,
                                                              'black', f4, frame_five))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_five():
    f4.destroy()

    global f5
    f5 = Frame(window, bg=pink)
    f5.pack(expand=1, fill=BOTH)

    description = Label(f5, text="Elaine smiles, knowing exactly what Peter is talking about. She explains that their "
                                 "favorite movie to watch together was \"Singin’ in the Rain\" and that it never "
                                 "failed to cheer them up. Elaine tells you that she always thought it was funny how "
                                 "Don kept taking his hat off in the pouring rain. What a fool! Peter loved the way she"
                                 " laughed during that scene.", bg=pink, wraplength=1000, font=(s_font, '25', 'bold'))
    description.place(anchor=CENTER, relx=0.5, rely=0.2)

    question_frame = Frame(f5, bg=gray, borderwidth=3, relief='solid')
    question_frame.place(anchor=CENTER, relx=0.5, rely=0.55)

    question = Label(question_frame, text="How many times does Don take off his hat?", bg=gray, font=(s_font, '25'))
    question.pack(side=TOP, padx=10, pady=(10, 5))

    entry = Entry(question_frame, font=(s_font, '25'), width=20)
    entry.pack(side=TOP, pady=(5, 10))

    instructions = Label(f5, text="Once you have the right answer, email it to Peter and tell him about this scene.",
                         bg=pink, font=(s_font, '25', 'bold'))
    instructions.place(anchor=CENTER, relx=0.5, rely=0.75)

    submit_btn = Button(f5, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_singular(entry.get(), "3", 0.65, 0.57, 'black', f5,
                                                              frame_six))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_six():
    f5.destroy()

    global f6
    f6 = Frame(window, bg=pink)
    f6.pack(expand=1, fill=BOTH)

    description = Label(f6, text="Go to where Peter wants to meet. Take a picture with your team and the letter at"
                                 " this location and email it to sarah.benton.18@cnu.edu.", font=(s_font, '40', 'bold'),
                        wraplength=800, justify=CENTER, bg=pink)
    description.place(anchor=CENTER, relx=0.5, rely=0.5)


if __name__ == "__main__":
    window = Tk()
    global fp
    fp = Frame(window, bg=pink)

    window.title("Divine Deviance Week 2")
    window.geometry("1440x900")

    intro_frame = Frame(window, bg='black')
    intro_frame.pack(expand=1, fill=BOTH)

    fire_image = ImageTk.PhotoImage(PIL.Image.open("images/images2/pink_sparks.png"))
    w = fire_image.width()
    h = fire_image.height()

    background_canvas = Canvas(intro_frame, width=w, height=h, highlightthickness=0)
    background_canvas.place(anchor=CENTER, relx=0.5, rely=0.5)

    background_canvas.create_image(0, 0, anchor=NW, image=fire_image)

    background_canvas.create_text(w / 2, h / 2 + 25, anchor=S, text="Divine Deviance", font=('Pristina', '150', 'bold'),
                                  fill='white', justify=CENTER)
    background_canvas.create_text(w / 2, h / 2 - 240, anchor=CENTER, text="Lock and Key Club presents...",
                                  font=('Pristina', '40', 'bold'),
                                  fill='white', justify=CENTER)

    start_button = Button(background_canvas, text="Begin Week\nTwo's Journey",
                          font=(s_font, '40', 'bold'), fg="white", bg="black",
                          command=lambda: intro_one(), relief='raised')
    start_button.place(anchor=CENTER, relx=0.5, rely=0.65)

    window.mainloop()
