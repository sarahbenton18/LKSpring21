from tkinter import *
from PIL import ImageTk
import PIL.Image

s_font = 'Bell MT'
fancy_font = 'Bernard MT Condensed'
green = '#107D23'
gray = '#DCDBDB'


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def check_answer_next(user_entry, answer, relx, rely, color, frame, next_function):
    user_entry = user_entry.lower()
    if (user_entry not in answer) or (user_entry == "") or (user_entry == " "):
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=relx, rely=rely)
    else:
        user_list.append(user_entry)
        correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
        correct_label = Label(frame, image=correct_image)
        correct_label.image = correct_image
        correct_label.place(anchor=CENTER, relx=relx, rely=rely)

    for answer in answer_list:
        if answer not in user_list:
            return

    discover.place(anchor=CENTER, relx=0.5, rely=0.65)

    next_btn = Button(frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg=color,
                      command=lambda: next_function())
    next_btn.place(anchor=CENTER, relx=0.65, rely=0.9)


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


def intro_one():
    intro_frame.destroy()

    global f_intro
    f_intro = Frame(window, bg='black')
    f_intro.pack(expand=1, fill=BOTH)

    text = Label(f_intro, text="\tThe conclusion of your third case has taken an emotional toll on you as you prepare"
                               " for your next case. Even though you understand the importance of your work, you can"
                               " never quite get used to the sight of a ghostly figure approaching you; this thought"
                               " crosses your mind as you see a relatively sickly looking middle-aged man coming"
                               " toward you. Without hesitation, you introduce yourself to the man and ask him if"
                               " he’s okay.\n\n\t\"Wow, you’re the first person to acknowledge me in ten years. You"
                               " can really start to feel invisible as a ghost - who would’ve thought? Anyway, my "
                               "name is Bernard Phillips. I was contacted by The Society of Divine Deviants and told"
                               " that you could help me. I’m hoping you can live up to your reputation.\"\n\n\t"
                               "Admittedly flattered by the mention of your budding reputation, you agree to help"
                               " the man. You ask him how he died and how you could help.", wraplength=1000,
                 font=(s_font, '22'), fg='white', bg='black', justify=LEFT)
    text.place(anchor=CENTER, relx=0.5, rely=0.4)

    next_btn = Button(f_intro, text="Next", font=(fancy_font, '25', 'bold'), fg='black', bg='white',
                      command=lambda: intro_two())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def intro_two():
    f_intro.destroy()

    global f_intro_2
    f_intro_2 = Frame(window, bg='black')
    f_intro_2.pack(expand=1, fill=BOTH)

    text = Label(f_intro_2, text="\t\"Well you see, I don’t have a great relationship with my siblings. I’m one of"
                                 " nine and I know all eight of them hate me, and at least the feeling is mutual."
                                 " Our family owns a very successful home renovation and construction company that"
                                 " all of the children help run. Well, all of the children except for me.\n\n\t"
                                 "\"I guess those bastards just assumed I would move on with my life. But oh no, "
                                 "it made my blood boil. I couldn't just stand back and watch them each make six "
                                 "figures a year and keep me out of the picture. I knew I had to do something. I "
                                 "knew what could make their business crumble to the ground. I started sabotaging "
                                 "their projects - I started small with a missing screw here and a missing nail "
                                 "there. But it wasn't enough. I had to go bigger and get more extreme. When newly"
                                 " renovated houses started collapsing, my siblings caught on to the mischief.",
                 wraplength=1000, font=(s_font, '22'), fg='white', bg='black', justify=LEFT)
    text.place(anchor=CENTER, relx=0.5, rely=0.4)

    next_btn = Button(f_intro_2, text="Next", font=(fancy_font, '25', 'bold'), fg='black', bg='white',
                      command=lambda: intro_three())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def intro_three():
    f_intro_2.destroy()

    global f_intro_3
    f_intro_3 = Frame(window, bg='black')
    f_intro_3.pack(expand=1, fill=BOTH)

    text = Label(f_intro_3, text="\t\"As I was preparing my next act of sabotage, one of my siblings axed me right there"
                                 " in the house. I don’t know which one of them killed me, but I know I was murdered by"
                                 " one of my siblings. Looking back, my jealousy was out of hand and I regret trying "
                                 "to tank their business. Please, help me figure out which one of my siblings killed"
                                 " me so I can try to make it right.\"\n\n\tYou don’t know what to say to Bernard. "
                                 "You don’t condone what he did, but the desperation in his voice makes you truly "
                                 "believe he’s ready to apologize. You shake his hand and tell him you’ll do "
                                 "everything you can to help.\n\n\tYou decide the best place to start would be to "
                                 "look through all the evidence the police gathered. You know a guy and he's able to "
                                 "hook up with everything in the Bernard Phillips Cold Case File.",
                 wraplength=1000, font=(s_font, '22'), fg='white', bg='black', justify=LEFT)
    text.place(anchor=CENTER, relx=0.5, rely=0.4)

    next_btn = Button(f_intro_3, text="Next", font=(fancy_font, '25', 'bold'), fg='black', bg='white',
                      command=lambda: chapter_four())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def chapter_four():
    f_intro_3.destroy()

    global chapter_four_frame
    chapter_four_frame = Frame(window, bg='black')
    chapter_four_frame.pack(expand=1, fill=BOTH)

    envy = ImageTk.PhotoImage(PIL.Image.open("images/images4/envy.jpg"))
    chapter_four_frame.envy = envy
    w = envy.width()
    h = envy.height()

    envy_canvas = Canvas(chapter_four_frame, width=w, height=h, highlightthickness=0)
    envy_canvas.place(anchor=CENTER, relx=0.5, rely=0.5)

    envy_canvas.create_image(0, 0, anchor=NW, image=envy)

    envy_canvas.create_text(w / 2 + 3, h / 2 + 153, anchor=S, text="ENVY", font=(fancy_font, '225', 'bold'),
                            fill='black', justify=CENTER)
    envy_canvas.create_text(w / 2, h / 2 + 150, anchor=S, text="ENVY", font=(fancy_font, '225', 'bold'),
                            fill='white', justify=CENTER)
    envy_canvas.create_text(w / 2 + 3, h / 2 - 247, anchor=CENTER, text="Chapter 4", font=(fancy_font, '65', 'bold'),
                            fill='black', justify=CENTER)
    envy_canvas.create_text(w / 2, h / 2 - 250, anchor=CENTER, text="Chapter 4", font=(fancy_font, '65', 'bold'),
                            fill='white', justify=CENTER)

    next_btn = Button(chapter_four_frame, text="Start", font=(fancy_font, '40', 'bold'), fg='white', bg='black',
                      command=lambda: frame_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.85)


def frame_one():
    chapter_four_frame.destroy()

    global f1
    f1 = Frame(window, bg=green)
    f1.pack(expand=1, fill=BOTH)

    # finger print puzzle

    description = Label(f1, text="7 finger prints were found at the crime scene.", font=(s_font, '25', 'bold'),
                        bg=green, wraplength=1100)
    description.place(anchor=N, relx=0.5, rely=0.01)

    finger_frame = Frame(f1, bg=green)
    finger_frame.place(anchor=N, relx=0.5, rely=0.08)

    padx = 40
    pady = 20

    finger1 = Frame(finger_frame, bg='black', borderwidth=3)
    finger1.grid(row=0, column=0)

    finger1_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/print1.png").resize((175, 225)))
    finger1_label = Label(finger1, bg='white', image=finger1_image)
    finger1_label.image = finger1_image
    finger1_label.pack(side=TOP)

    finger2 = Frame(finger_frame, bg='black', borderwidth=3)
    finger2.grid(row=0, column=1, padx=padx)

    finger2_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/print2.png").resize((175, 225)))
    finger2_label = Label(finger2, bg='white', image=finger2_image)
    finger2_label.image = finger2_image
    finger2_label.pack(side=TOP)

    finger3 = Frame(finger_frame, bg='black', borderwidth=3)
    finger3.grid(row=0, column=2)

    finger3_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/print3.png").resize((175, 225)))
    finger3_label = Label(finger3, bg='white', image=finger3_image)
    finger3_label.image = finger3_image
    finger3_label.pack(side=TOP)

    finger4 = Frame(finger_frame, bg='black', borderwidth=3)
    finger4.grid(row=0, column=3, padx=(padx, 0))

    finger4_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/print4.png").resize((175, 225)))
    finger4_label = Label(finger4, bg='white', image=finger4_image)
    finger4_label.image = finger4_image
    finger4_label.pack(side=TOP)

    finger5 = Frame(finger_frame, bg='black', borderwidth=3)
    finger5.grid(row=1, column=0, pady=(pady, 0))

    finger5_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/print5.png").resize((175, 225)))
    finger5_label = Label(finger5, bg='white', image=finger5_image)
    finger5_label.image = finger5_image
    finger5_label.pack(side=TOP)

    finger6 = Frame(finger_frame, bg='black', borderwidth=3)
    finger6.grid(row=1, column=1, pady=(pady, 0))

    finger6_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/print6.png").resize((175, 225)))
    finger6_label = Label(finger6, bg='white', image=finger6_image)
    finger6_label.image = finger6_image
    finger6_label.pack(side=TOP)

    finger7 = Frame(finger_frame, bg='black', borderwidth=3)
    finger7.grid(row=1, column=2, pady=(pady, 0))

    finger7_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/print7.png").resize((175, 225)))
    finger7_label = Label(finger7, bg='white', image=finger7_image)
    finger7_label.image = finger7_image
    finger7_label.pack(side=TOP)

    entry_frame = Frame(finger_frame, bg='black', borderwidth=3)
    entry_frame.grid(row=1, column=3, pady=(pady, 0), padx=(padx, 0))

    question = Label(entry_frame, text="Who wasn't at the crime scene?", bg='black', font=(s_font, '25'),
                     fg='white', wraplength=250)
    question.pack(side=TOP, pady=(25, 0))

    entry = Entry(entry_frame, font=(s_font, '20'), width=15)
    entry.pack(side=TOP, pady=(15, 60))

    submit_btn = Button(f1, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_answer_singular(entry.get(), "ernest", 0.73, 0.695,
                                                                        'black', f1, frame_two)))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_two():
    f1.destroy()

    global f2
    f2 = Frame(window, bg=green)
    f2.pack(expand=1, fill=BOTH)

    map_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/map.png").resize((850, 400)))
    map_label = Label(f2, bg='black', image=map_image)
    map_label.image = map_image
    map_label.place(anchor=N, relx=0.5, rely=0.01)

    question_frame = Frame(f2, bg='black')
    question_frame.place(anchor=N, relx=0.5, rely=0.65)

    question = Label(question_frame, bg='black', fg='white', text="If the murder happened at the yellow x, which "
                                                                  "suspect couldn't have done it?", font=(s_font, '25'))
    question.pack(side=TOP, pady=(10, 5), padx=10)

    entry = Entry(question_frame, font=(s_font, '25'), width=20)
    entry.pack(side=TOP, pady=(0, 10))

    submit_btn = Button(f2, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_answer_singular(entry.get(), "amelia", 0.53, 0.765,
                                                                            'black', f2, frame_three)))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_three():
    f2.destroy()

    global f3
    f3 = Frame(window, bg=green)
    f3.pack(expand=1, fill=BOTH)

    # find paint chips

    text = Label(f3, text="As it turns out, the guy you know didn't hook you up with 'all' the evidence. There's one"
                          " more thing your guy has for you. Your guy tells you to go to Riverview Farm Park. "
                          "Find the scenic outlook right on the water. As you head toward the pier, the paths "
                          "diverge, but meet back again at the pier. There's a fallen tree that looks like a wishbone "
                          "in the wooded area that's encircled by the diverging paths. Your guy buried the rest of the"
                          " evidence under that tree.\n Once you've collected the new evidence, click next.",
                 font=(s_font, '25'), bg=green, wraplength=900)
    text.place(anchor=CENTER, relx=0.5, rely=0.45)

    next_btn = Button(f3, text="Next", font=(fancy_font, '25', 'bold'), bg='black', fg='white',
                      command=lambda: frame_four())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_four():
    f3.destroy()

    global f4
    f4 = Frame(window, bg=green)
    f4.pack(expand=1, fill=BOTH)

    global user_list
    user_list = []

    global answer_list
    answer_list = ["etched glass", "bohemianism", "voyage", "cherry juice", "billard green", "dark secret"]

    description = Label(f4, text="These were the paint samples found on each of the remaining suspects. First, figure"
                                 " out where the construction company buys their paint. Then go there and determine "
                                 "the names of the paint colors. Input their names in alphabetical order.",
                        font=(s_font, '25'), wraplength=1100, bg=green)
    description.place(anchor=N, relx=0.5, rely=0.05)

    global discover
    discover = Label(f4, text="All but \"Etched Glass\" were found on Bernard's body. \"Etched Glass\" was the only"
                              " paint found on Robert's shoes, so it couldn't have been Robert.", font=(s_font, '25'),
                     wraplength=1100, bg=green)

    entry_frame = Frame(f4, bg=green)
    entry_frame.place(anchor=N, relx=0.5, rely=0.25)

    label_1 = Label(entry_frame, text="1)", font=(s_font, '30', 'bold'), bg=green)
    label_1.grid(row=0, column=0)

    entry_1 = Entry(entry_frame, font=(s_font, '30'), width=20)
    entry_1.grid(row=0, column=1, padx=(5, 60))

    label_2 = Label(entry_frame, text="2)", font=(s_font, '30', 'bold'), bg=green)
    label_2.grid(row=1, column=0, pady=15)

    entry_2 = Entry(entry_frame, font=(s_font, '30'), width=20)
    entry_2.grid(row=1, column=1, padx=(5, 60))

    label_3 = Label(entry_frame, text="3)", font=(s_font, '30', 'bold'), bg=green)
    label_3.grid(row=2, column=0)

    entry_3 = Entry(entry_frame, font=(s_font, '30'), width=20)
    entry_3.grid(row=2, column=1, padx=(5, 60))

    label_4 = Label(entry_frame, text="4)", font=(s_font, '30', 'bold'), bg=green)
    label_4.grid(row=0, column=2)

    entry_4 = Entry(entry_frame, font=(s_font, '30'), width=20)
    entry_4.grid(row=0, column=3, padx=(5, 0))

    label_5 = Label(entry_frame, text="5)", font=(s_font, '30', 'bold'), bg=green)
    label_5.grid(row=1, column=2)

    entry_5 = Entry(entry_frame, font=(s_font, '30'), width=20)
    entry_5.grid(row=1, column=3, padx=(5, 0))

    label_6 = Label(entry_frame, text="6)", font=(s_font, '30', 'bold'), bg=green)
    label_6.grid(row=2, column=2)

    entry_6 = Entry(entry_frame, font=(s_font, '30'), width=20)
    entry_6.grid(row=2, column=3, padx=(5, 0))

    submit_btn = Button(f4, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_answer_next(entry_1.get(), "billard green", 0.5, 0.29,
                                                                        'black', f4, frame_five),
                                                      check_answer_next(entry_2.get(), "bohemianism", 0.5, 0.39,
                                                                        'black', f4, frame_five),
                                                      check_answer_next(entry_3.get(), "cherry juice", 0.5, 0.49,
                                                                        'black', f4, frame_five),
                                                      check_answer_next(entry_4.get(), "dark secret", 0.9, 0.29,
                                                                        'black', f4, frame_five),
                                                      check_answer_next(entry_5.get(), "etched glass", 0.9, 0.39,
                                                                        'black', f4, frame_five),
                                                      check_answer_next(entry_6.get(), "voyage", 0.9, 0.49,
                                                                        'black', f4, frame_five)))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_five():
    f4.destroy()

    global f5
    f5 = Frame(window, bg=green)
    f5.pack(expand=1, fill=BOTH)

    description = Label(f5, bg=green, text="There are only 5 suspects left. You look at where they were on the night"
                                           " of February 27, 2011, the night of Bernard's murder.", wraplength=900,
                        font=(s_font, '25'))
    description.place(anchor=N, relx=0.5, rely=0.01)

    alibi_frame = Frame(f5, bg='black')
    alibi_frame.place(anchor=CENTER, relx=0.5, rely=0.4)

    font_size = '18'

    alibi1 = Label(alibi_frame, bg='black', fg='white', text="Eliza and Samuel say they were having dinner at Longhorn"
                                                             " Steakhouse with their spouses at 6:30 pm.",
                   font=(s_font, font_size), wraplength=1100)
    alibi1.pack(side=TOP, padx=20, pady=20)

    alibi2 = Label(alibi_frame, bg='black', fg='white', text="Jackson says he left the house at 7:30 pm and "
                                                             "went to Starbucks to work on company marketing.",
                   font=(s_font, font_size), wraplength=1100)
    alibi2.pack(side=TOP, padx=20)

    alibi3 = Label(alibi_frame, bg='black', fg='white', text="Lucille says she was at Chick-fil-A until 8:30 pm.",
                   font=(s_font, font_size), wraplength=1100)
    alibi3.pack(side=TOP, padx=20, pady=20)

    alibi4 = Label(alibi_frame, bg='black', fg='white', text="Eliza says she stayed at the Longhorn bar for drinks "
                                                             "with her husband after Samuel left with his wife.",
                   font=(s_font, font_size), wraplength=1100)
    alibi4.pack(side=TOP, padx=20)

    alibi5 = Label(alibi_frame, bg='black', fg='white', text="Samuel says he stopped by the house right after leaving"
                                                             " dinner and discovered the body around 8:45 pm.",
                   font=(s_font, font_size), wraplength=1100)
    alibi5.pack(side=TOP, padx=20, pady=20)

    alibi6 = Label(alibi_frame, bg='black', fg='white', text="Ernest says Jameson was with him working on goal-setting"
                                                             " for the company at the office all evening.",
                   font=(s_font, font_size), wraplength=1100)
    alibi6.pack(side=TOP, padx=20, pady=(0, 20))

    question_frame = Frame(f5, bg='black')
    question_frame.place(anchor=N, relx=0.5, rely=0.67)

    question = Label(question_frame, bg='black', fg='white', text="Who's alibi cannot be true?", font=(s_font, '25'))
    question.pack(side=TOP, pady=(10, 5), padx=10)

    entry = Entry(question_frame, font=(s_font, '25'), width=20)
    entry.pack(side=TOP, pady=(0, 10))

    submit_btn = Button(f5, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_answer_singular(entry.get(), "lucille", 0.53, 0.79,
                                                                            'black', f5, frame_six)))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_six():
    f5.destroy()

    global f6
    f6 = Frame(window, bg=green)
    f6.pack(expand=1, fill=BOTH)

    final = Label(f6, text="You have successfully identified Bernard’s killer. Lucille felt like she couldn’t stand "
                           "by and watch Bernard tear down their company any longer. You inform Bernard’s ghost of your"
                           " findings, and help facilitate his communication with Lucille and the rest of his "
                           "siblings. Through this discussion, Bernard is able to make peace with what his jealousy "
                           "drove him to do to his siblings and with what Lucille did to him.", font=(s_font, '25'),
                  wraplength=900, bg=green)
    final.place(anchor=CENTER, relx=0.5, rely=0.35)

    email = Label(f6, text="Email sarah.benton.18@cnu.edu your favorite song / band so we can know you have complete "
                           "Week 4. Great job so far! Keep it up!", bg=green, font=(s_font, '25'), wraplength=900)
    email.place(anchor=CENTER, relx=0.5, rely=0.8)


if __name__ == "__main__":
    window = Tk()

    window.title("Divine Deviance Week 4")
    window.geometry("1440x900")

    intro_frame = Frame(window, bg='black')
    intro_frame.pack(expand=1, fill=BOTH)

    fire_image = ImageTk.PhotoImage(PIL.Image.open("images/images4/sparks.png"))
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

    start_button = Button(background_canvas, text="Begin Week\nFour's Journey",
                          font=(s_font, '40', 'bold'), fg="white", bg="black",
                          command=lambda: intro_one(), relief='raised')
    start_button.place(anchor=CENTER, relx=0.5, rely=0.65)

    window.mainloop()