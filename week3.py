from tkinter import *
from tkinter import font
from PIL import ImageTk
import PIL.Image

s_font = 'Bell MT'
fancy_font = 'Impact'
orange = '#FFCA60'
gray = '#DCDBDB'
red = '#A40A0A'

# 'Snap ITC'
# 'Stencil'
# 'Showcard'
# 'Rockwell'
# 'Latin Wide'
# 'Impact'
# 'Gill Sans'
# 'Cooper Black'
# 'Britannic Bold'
# 'Bernard MT Condensed'


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


def check_answer_tattoo(user_entry, answer, relx, rely, color, frame, next_function):
    user_entry = user_entry.lower().strip("\n")
    if user_entry == answer:
        correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
        correct_label = Label(frame, image=correct_image)
        correct_label.image = correct_image
        correct_label.place(anchor=CENTER, relx=relx, rely=rely)

        next_btn = Button(frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg=color,
                          command=lambda: next_function())
        next_btn.place(anchor=CENTER, relx=0.67, rely=0.9)
    else:
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=relx, rely=rely)


def intro_one():
    intro_frame.destroy()

    global f_intro
    f_intro = Frame(window, bg='black')
    f_intro.pack(expand=1, fill=BOTH)

    story = Label(f_intro, text="\tAfter having solved two cases for the Society of Divine Deviants, you feel like you "
                                "need to get away for a bit. You didn’t mind helping, but the process certainly takes"
                                " a toll and you’re ready for some downtime. Just as you’re packing up your car for a"
                                " weekend camping trip, you feel an oddly cool breeze as your nose is met with the "
                                "overwhelming stench of tobacco and body sweat. You turn, meeting the gaze of a "
                                "ghostly young man dressed in tattered, stained clothing.\n\n\t\"Oh shit, I didn’t mean"
                                " to scare you man,\" he says in a pained, exhausted voice. \"My name’s Alex and I was"
                                " told by some pretty creepy lookin’ dudes that you could help me out.\"\n\n\tUnphased,"
                                " you stand before the ghost, silently deciding how to respond. Alex interprets this"
                                " silence as an opportunity to explain his situation.",
                  font=(s_font, '25'), bg='black', fg='white', wraplength=1100, justify=LEFT)
    story.place(anchor=CENTER, relx=0.5, rely=0.45)

    next_btn = Button(f_intro, text="Next", font=(fancy_font, '25', 'bold'), fg='black', bg='white',
                      command=lambda: intro_two())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def intro_two():
    f_intro.destroy()

    global f_intro2
    f_intro2 = Frame(window, bg='black')
    f_intro2.pack(expand=1, fill=BOTH)

    story2 = Label(f_intro2, text="\t\"I know I look like shit now,"
                                " but I didn’t used to live this life, I swear. Growing up, I was a pretty talented"
                                " guy. I figured I’d join a band, tour for a few years, make some dough, then settle"
                                " down in a suburb with a family. You know the whole white picket fence dream. But "
                                "the lifestyle sucked me in and I couldn’t help myself. Drugs, alcohol, strippers, "
                                "and just about every other shady thing you could think of - I did all of it. And "
                                "it didn’t take long for my little brother Archie to get sucked in too. He got the "
                                "brains of the family, always studying and all that. He had so much ahead of him,"
                                " but I was a bad influence. When he found out I’d overdosed, he went missing and"
                                " nobody has heard from him since.\"\n\n\tYou don’t even know what to say. You’ve "
                                "completed two cases, but something about this one feels different. Your "
                                "apprehension is clearly visible, causing Alex to drop to his knees, sobbing.",
                   font=(s_font, '25'), bg='black', fg='white', wraplength=1100, justify=LEFT)
    story2.place(anchor=CENTER, relx=0.5, rely=0.45)

    next_btn = Button(f_intro2, text="Next", font=(fancy_font, '25', 'bold'), fg='black', bg='white',
                      command=lambda: intro_three())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def intro_three():
    f_intro2.destroy()

    global f_intro3
    f_intro3 = Frame(window, bg='black')
    f_intro3.pack(expand=1, fill=BOTH)

    story3 = Label(f_intro3, text="\t\"I don’t want you to feel sorry for me. I made my choices and now I’m paying for "
                                  "them, but I could never forgive myself if I let Archie kill himself too. Please, "
                                  "I’m begging you, help me find him and get him some help.\"\n\n\tYou nod, agreeing "
                                  "to help.\n\n\tAlex thanks you and immediately leads you to his phone. You find a "
                                  "string of cryptic texts that Archie sent to Alex right before Alex died. Alex "
                                  "thinks that figuring out what these texts mean could help lead to Archie.",
                   font=(s_font, '25'), bg='black', fg='white', wraplength=1100, justify=LEFT)
    story3.place(anchor=CENTER, relx=0.5, rely=0.45)

    next_btn = Button(f_intro3, text="Next", font=(fancy_font, '25', 'bold'), fg='black', bg='white',
                      command=lambda: chapter_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def chapter_one():
    f_intro3.destroy()

    global chapter_one_frame
    chapter_one_frame = Frame(window, bg='black')
    chapter_one_frame.pack(expand=1, fill=BOTH)

    gluttony = ImageTk.PhotoImage(PIL.Image.open("images/images3/background.jpg"))
    chapter_one_frame.lust = gluttony
    w = gluttony.width()
    h = gluttony.height()

    gluttony_canvas = Canvas(chapter_one_frame, width=w, height=h, highlightthickness=0)
    gluttony_canvas.place(anchor=CENTER, relx=0.5, rely=0.5)

    gluttony_canvas.create_image(0, 0, anchor=NW, image=gluttony)

    gluttony_canvas.create_text(w / 2 + 3, h / 2 + 128, anchor=S, text="Gluttony", font=(fancy_font, '150', 'bold'),
                            fill='black', justify=CENTER)
    gluttony_canvas.create_text(w / 2, h / 2 + 125, anchor=S, text="Gluttony", font=(fancy_font, '150', 'bold'),
                            fill=red, justify=CENTER)
    gluttony_canvas.create_text(w / 2 + 3, h / 2 - 197, anchor=CENTER, text="Chapter 3", font=(fancy_font, '65', 'bold'),
                            fill='black', justify=CENTER)
    gluttony_canvas.create_text(w / 2, h / 2 - 200, anchor=CENTER, text="Chapter 3", font=(fancy_font, '65', 'bold'),
                            fill=red, justify=CENTER)

    next_btn = Button(chapter_one_frame, text="Start", font=(fancy_font, '40', 'bold'), fg='white', bg='black',
                      command=lambda: frame_one())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.85)


def frame_one():
    chapter_one_frame.destroy()

    global f1
    f1 = Frame(window, bg=red)
    f1.pack(expand=1, fill=BOTH)

    instructions = Label(f1, text="You look at the first text sent by Archie:",
                         font=(s_font, '25'), bg=red)
    instructions.place(anchor=CENTER, relx=0.5, rely=0.04)

    text_frame = Frame(f1, bg='black', borderwidth=5)
    text_frame.place(anchor=N, relx=0.5, rely=0.08)

    message_frame = Frame(text_frame, bg='black')
    message_frame.grid(row=0, column=0, columnspan=3, pady=(12, 15))

    text_a = Label(message_frame, text="\"Wanna catch a", font=(s_font, '30'), bg='black', fg='white')
    text_a.pack(side=LEFT)

    text_b = Label(message_frame, text="line", font=(s_font, '30', 'bold'), bg='black', fg='white')
    text_b.pack(side=LEFT)

    text_c = Label(message_frame, text="? Just say the", font=(s_font, '30'), bg='black', fg='white')
    text_c.pack(side=LEFT)

    text_d = Label(message_frame, text="word", font=(s_font, '30', 'bold'), bg='black', fg='white')
    text_d.pack(side=LEFT)

    text_e = Label(message_frame, text="and I'll", font=(s_font, '30'), bg='black', fg='white')
    text_e.pack(side=LEFT)

    text_f = Label(message_frame, text="letter", font=(s_font, '30', 'bold'), bg='black', fg='white')
    text_f.pack(side=LEFT)

    text_g = Label(message_frame, text="rip.\"", font=(s_font, '30'), bg='black', fg='white')
    text_g.pack(side=LEFT)

    font_size = '30'
    song_size = '40'

    # the cars
    cars_frame = Frame(text_frame, bg=red)
    cars_frame.grid(row=1, column=0)

    candy_song = Label(cars_frame, text=" 4", font=(s_font, song_size, 'bold'), bg=red, fg='white')
    candy_song.grid(column=0, row=1)

    candy_image = ImageTk.PhotoImage(PIL.Image.open("images/images3/candy-o.jpg").resize((175, 175)))
    candy_label = Label(cars_frame, image=candy_image, bg='white')
    candy_label.image = candy_image
    candy_label.grid(column=1, row=0, rowspan=3, padx=10, pady=10)

    candy_row1 = Label(cars_frame, text="17 - 4 -  5", font=(s_font, font_size), bg=red, fg='white')
    candy_row1.grid(column=2, row=0)

    candy_row2 = Label(cars_frame, text=" 3 - 5 -  3", font=(s_font, font_size), bg=red, fg='white')
    candy_row2.grid(column=2, row=1)

    candy_row3 = Label(cars_frame, text="10 - 6 - 10", font=(s_font, font_size), bg=red, fg='white')
    candy_row3.grid(column=2, row=2)

    # the frights
    frights_frame = Frame(text_frame, bg='black', borderwidth=2, relief='solid')
    frights_frame.grid(row=2, column=0)

    frights_song = Label(frights_frame, text="12", font=(s_font, song_size, 'bold'), bg='black', fg='white')
    frights_song.grid(column=0, row=0, rowspan=2)

    frights_image = ImageTk.PhotoImage(PIL.Image.open("images/images3/frights.jpg").resize((175, 175)))
    frights_label = Label(frights_frame, image=frights_image, bg='white')
    frights_label.image = frights_image
    frights_label.grid(column=1, row=0, rowspan=2, padx=10, pady=3)

    frights_row1 = Label(frights_frame, text="3 - 12 - 4", font=(s_font, font_size), bg='black', fg='white')
    frights_row1.grid(column=2, row=0)

    frights_row2 = Label(frights_frame, text="9 -  2 - 8", font=(s_font, font_size), bg='black', fg='white')
    frights_row2.grid(column=2, row=1)

    # the strokes
    strokes_frame = Frame(text_frame, bg='black', borderwidth=2, relief='solid')
    strokes_frame.grid(row=1, column=1)

    strokes_song = Label(strokes_frame, text="3", font=(s_font, song_size, 'bold'), bg='black', fg='white')
    strokes_song.grid(column=0, row=1)

    strokes_image = ImageTk.PhotoImage(PIL.Image.open("images/images3/room.png").resize((175, 175)))
    strokes_label = Label(strokes_frame, image=strokes_image, bg='white')
    strokes_label.image = strokes_image
    strokes_label.grid(column=1, row=0, rowspan=3, padx=10, pady=3)

    strokes_row1 = Label(strokes_frame, text="17 - 2 - 1", font=(s_font, font_size), bg='black', fg='white')
    strokes_row1.grid(column=2, row=0, padx=3)

    strokes_row2 = Label(strokes_frame, text=" 8 - 7 - 2", font=(s_font, font_size), bg='black', fg='white')
    strokes_row2.grid(column=2, row=1)

    strokes_row3 = Label(strokes_frame, text="14 - 4 - 3", font=(s_font, font_size), bg='black', fg='white')
    strokes_row3.grid(column=2, row=2)

    # the red pears
    red_frame = Frame(text_frame, bg=red)
    red_frame.grid(row=2, column=1)

    red_song = Label(red_frame, text="5", font=(s_font, song_size, 'bold'), bg=red, fg='white')
    red_song.grid(column=0, row=1)

    red_image = ImageTk.PhotoImage(PIL.Image.open("images/images3/red.jpg").resize((175, 175)))
    red_label = Label(red_frame, image=red_image, bg='white')
    red_label.image = red_image
    red_label.grid(column=1, row=0, rowspan=3, padx=10, pady=10)

    red_row1 = Label(red_frame, text="24 - 4 - 2", font=(s_font, font_size), bg=red, fg='white')
    red_row1.grid(column=2, row=0, padx=3)

    red_row2 = Label(red_frame, text="12 - 5 - 3", font=(s_font, font_size), bg=red, fg='white')
    red_row2.grid(column=2, row=1)

    red_row3 = Label(red_frame, text="29 - 5 - 5", font=(s_font, font_size), bg=red, fg='white')
    red_row3.grid(column=2, row=2)

    # violent femmes
    violent_frame = Frame(text_frame, bg=red)
    violent_frame.grid(row=1, column=2)

    violent_song = Label(violent_frame, text="2", font=(s_font, song_size, 'bold'), bg=red, fg='white')
    violent_song.grid(column=0, row=1)

    violent_image = ImageTk.PhotoImage(PIL.Image.open("images/images3/femmes.jpg").resize((175, 175)))
    violent_label = Label(violent_frame, image=violent_image, bg='white')
    violent_label.image = violent_image
    violent_label.grid(column=1, row=0, rowspan=3, padx=10, pady=10)

    violent_row1 = Label(violent_frame, text=" 9 - 5 - 2", font=(s_font, font_size), bg=red, fg='white')
    violent_row1.grid(column=2, row=0)

    violent_row2 = Label(violent_frame, text="19 - 5 - 9", font=(s_font, font_size), bg=red, fg='white')
    violent_row2.grid(column=2, row=1)

    violent_row3 = Label(violent_frame, text="29 - 7 - 3", font=(s_font, font_size), bg=red, fg='white')
    violent_row3.grid(column=2, row=2)

    # answer
    entry_frame = Frame(text_frame, bg='black', borderwidth=2, relief='solid')
    entry_frame.grid(row=2, column=2)

    text = Label(entry_frame, text="Where should you look next?", font=(s_font, '22'), bg='black',
                 fg='white')
    text.pack(side=TOP, padx=3, pady=(40, 15))

    entry = Entry(entry_frame, font=(s_font, '23'))
    entry.pack(side=TOP, pady=(15, 40))

    submit_btn = Button(f1, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_singular(entry.get(), "american oldies", 0.67,
                                                              0.785, 'black', f1, frame_two))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_two():
    f1.destroy()

    global f2
    f2 = Frame(window, bg=red)
    f2.pack(expand=1, fill=BOTH)

    instructions = Label(f2, text="Once at the record store, you read the next text sent by Archie:",
                         font=(s_font, '25'), bg=red)
    instructions.place(anchor=CENTER, relx=0.5, rely=0.07)

    e_font = '32'

    equation_frame = Frame(f2, bg='black', borderwidth=5, relief='solid')
    equation_frame.place(anchor=CENTER, relx=0.25, rely=0.5)

    row_egg = Frame(equation_frame, bg='black')
    row_egg.pack(side=TOP)

    egg_a = Label(row_egg, bg='black', fg='white', text="egg", font=(s_font, e_font), underline=0, padx=0)
    egg_a.pack(side=LEFT)

    egg_a = Label(row_egg, bg='black', fg='white', text="s", font=(s_font, e_font, 'bold'), padx=0)
    egg_a.pack(side=LEFT)

    multiply = Label(equation_frame, bg='black', fg='white', text="x", font=(s_font, e_font))
    multiply.pack(side=TOP)

    row_mid = Frame(equation_frame, bg='black')
    row_mid.pack(side=TOP)

    mid_a = Label(row_mid, bg='black', fg='white', text="midwes", font=(s_font, e_font), padx=0)
    mid_a.pack(side=LEFT)

    mid_b = Label(row_mid, bg='black', fg='white', text="t", font=(s_font, e_font, 'bold'), padx=0)
    mid_b.pack(side=LEFT)

    divide = Label(equation_frame, bg='black', fg='white', text="÷", font=(s_font, e_font))
    divide.pack(side=TOP)

    row_emancipation = Frame(equation_frame, bg='black')
    row_emancipation.pack(side=TOP)

    eman_a = Label(row_emancipation, bg='black', fg='white', text="e", font=(s_font, e_font, 'bold'), padx=0)
    eman_a.pack(side=LEFT)

    eman_b = Label(row_emancipation, bg='black', fg='white', text="manci", font=(s_font, e_font), underline=0, padx=0)
    eman_b.pack(side=LEFT)

    eman_c = Label(row_emancipation, bg='black', fg='white', text="pa", font=(s_font, e_font), underline=0, padx=0)
    eman_c.pack(side=LEFT)

    eman_d = Label(row_emancipation, bg='black', fg='white', text="t", font=(s_font, e_font, 'bold'), padx=0)
    eman_d.pack(side=LEFT)

    eman_e = Label(row_emancipation, bg='black', fg='white', text="ion", font=(s_font, e_font), padx=0)
    eman_e.pack(side=LEFT)

    plus1 = Label(equation_frame, bg='black', fg='white', text="+", font=(s_font, e_font))
    plus1.pack(side=TOP)

    row_anthology = Frame(equation_frame, bg='black')
    row_anthology.pack(side=TOP)

    anth_a = Label(row_anthology, bg='black', fg='white', text="antho", font=(s_font, e_font), padx=0)
    anth_a.pack(side=LEFT)

    anth_b = Label(row_anthology, bg='black', fg='white', text="logy", font=(s_font, e_font), underline=0, padx=0)
    anth_b.pack(side=LEFT)

    plus2 = Label(equation_frame, bg='black', fg='white', text="+", font=(s_font, e_font))
    plus2.pack(side=TOP)

    row_armaged = Frame(equation_frame, bg='black')
    row_armaged.pack(side=TOP)

    armaged_a = Label(row_armaged, bg='black', fg='white', text="a", font=(s_font, e_font), padx=0)
    armaged_a.pack(side=LEFT)

    armaged_b = Label(row_armaged, bg='black', fg='white', text="r", font=(s_font, e_font, 'bold'), padx=0)
    armaged_b.pack(side=LEFT)

    armaged_c = Label(row_armaged, bg='black', fg='white', text="mag", font=(s_font, e_font), underline=1, padx=0)
    armaged_c.pack(side=LEFT)

    armaged_d = Label(row_armaged, bg='black', fg='white', text="e", font=(s_font, e_font, 'bold'), padx=0)
    armaged_d.pack(side=LEFT)

    armaged_a = Label(row_armaged, bg='black', fg='white', text="ddon", font=(s_font, e_font), padx=0)
    armaged_a.pack(side=LEFT)

    answer_frame = Frame(f2, bg='black')
    answer_frame.place(anchor=CENTER, relx=0.66, rely=0.5)

    question = Label(answer_frame, bg='black', fg='white', text="Where should you look next?", font=(s_font, '30'))
    question.pack(side=TOP, padx=10, pady=(10, 5))

    entry = Entry(answer_frame, font=(s_font, e_font))
    entry.pack(side=TOP, pady=(5, 10))

    submit_btn = Button(f2, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_singular(entry.get(), "5103 maple street", 0.51,
                                                              0.65, 'black', f2, frame_three))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_three():
    f2.destroy()

    global f3
    f3 = Frame(window, bg=red)
    f3.pack(expand=1, fill=BOTH)

    instructions = Label(f3, text="\tAlex recognizes this address as the home of his band's drummer, Jimmy. When you "
                                  "get to Jimmy's house, you find Jimmy passed out on the couch in the living room, "
                                  "but Archie is nowhere to be seen. After waking up a still drunk Jimmy, you ask him "
                                  "if he knows where Archie is. Slurring his words and failing to make eye contact, "
                                  "Jimmy tells you that Archie left sometime late last night, but he can't "
                                  "remember where he said he was going.\n\n\tAt a loss for where to search next, "
                                  "Alex spots Archie's phone among the empty bottles and dirty clothes littering"
                                  " the floor. Alex reasons that if you can get into his phone, maybe you could "
                                  "figure out where he went after leaving Jimmy's.\n\n\tAlex doesn't remember the "
                                  "password exactly, but he knows it had something to do with connecting the dots "
                                  "on Jimmy's tattoos. You turn back to Jimmy and find that he has crashed on the sofa"
                                  " again. You figure he won't mind if you study his tattoos if it means saving his "
                                  "friend...",
                         font=(s_font, '23'), bg=red, wraplength=1100, justify=LEFT)
    instructions.place(anchor=CENTER, relx=0.5, rely=0.425)

    next_btn = Button(f3, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_four())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_four():
    f3.destroy()

    global f4
    f4 = Frame(window, bg=red)
    f4.pack(expand=1, fill=BOTH)

    tattoo_frame = Frame(f4, bg=red)
    tattoo_frame.place(anchor=N, relx=0.5, rely=0.03)

    tat_font = '25'

    # row 1
    row1 = Frame(f4, bg=red)
    row1.place(anchor=NW, relx=0.03, rely=0.01)

    description1 = Label(row1, bg=red, text="Left\nArm", font=(s_font, tat_font, 'bold'))
    description1.grid(row=0, column=0)

    row1_img1 = ImageTk.PhotoImage(PIL.Image.open("images/images3/notre.png").resize((175, 175)))
    row1_label1 = Label(row1, image=row1_img1, bg='black', borderwidth=3)
    row1_label1.image = row1_img1
    row1_label1.grid(row=0, column=1, padx=20)

    row1_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images3/amsterdam.jpg").resize((175, 175)))
    row1_label2 = Label(row1, image=row1_img2, bg='black', borderwidth=3)
    row1_label2.image = row1_img2
    row1_label2.grid(row=0, column=2, padx=(0, 20))

    row1_img3 = ImageTk.PhotoImage(PIL.Image.open("images/images3/ben.jpg").resize((175, 175)))
    row1_label3 = Label(row1, image=row1_img3, bg='black', borderwidth=3)
    row1_label3.image = row1_img3
    row1_label3.grid(row=0, column=3, padx=(0, 20))

    row1_img4 = ImageTk.PhotoImage(PIL.Image.open("images/images3/sprout.jpg").resize((175, 175)))
    row1_label4 = Label(row1, image=row1_img4, bg='black', borderwidth=3)
    row1_label4.image = row1_img4
    row1_label4.grid(row=0, column=4)

    # row 2
    row2 = Frame(f4, bg=red)
    row2.place(anchor=NW, relx=0.018, rely=0.35)

    description2 = Label(row2, bg=red, text="Right\nArm\nand\nBack", font=(s_font, tat_font, 'bold'))
    description2.grid(row=0, column=0)

    row2_img1 = ImageTk.PhotoImage(PIL.Image.open("images/images3/orleans.jpg").resize((175, 175)))
    row2_label1 = Label(row2, image=row2_img1, bg='black', borderwidth=3)
    row2_label1.image = row2_img1
    row2_label1.grid(row=0, column=1, padx=(15, 20))

    row2_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images3/atlanta.jpg").resize((175, 175)))
    row2_label2 = Label(row2, image=row2_img2, bg='black', borderwidth=3)
    row2_label2.image = row2_img2
    row2_label2.grid(row=0, column=2, padx=(0, 20))

    row2_img3 = ImageTk.PhotoImage(PIL.Image.open("images/images3/miami.jpg").resize((175, 175)))
    row2_label3 = Label(row2, image=row2_img3, bg='black', borderwidth=3)
    row2_label3.image = row2_img3
    row2_label3.grid(row=0, column=3, padx=(0, 20))

    # row 3
    row3 = Frame(f4, bg=red)
    row3.place(anchor=NW, relx=0.03, rely=0.69)

    description3 = Label(row3, bg=red, text="Left\nLeg", font=(s_font, tat_font, 'bold'))
    description3.grid(row=0, column=0)

    row3_img1 = ImageTk.PhotoImage(PIL.Image.open("images/images3/bridge.jpg").resize((175, 175)))
    row3_label1 = Label(row3, image=row3_img1, bg='black', borderwidth=3)
    row3_label1.image = row3_img1
    row3_label1.grid(row=0, column=1, padx=20)

    row3_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images3/bell.jpg").resize((175, 175)))
    row3_label2 = Label(row3, image=row3_img2, bg='black', borderwidth=3)
    row3_label2.image = row3_img2
    row3_label2.grid(row=0, column=2, padx=(0, 20))

    row3_img3 = ImageTk.PhotoImage(PIL.Image.open("images/images3/dc.png").resize((175, 175)))
    row3_label3 = Label(row3, image=row3_img3, bg='black', borderwidth=3)
    row3_label3.image = row3_img3
    row3_label3.grid(row=0, column=3, padx=(0, 20))

    # row 4 - which is actually a column
    row4 = Frame(f4, bg=red)
    row4.place(anchor=N, relx=0.85, rely=0.01)

    description4 = Label(row4, bg=red, text="Right Leg", font=(s_font, tat_font, 'bold'))
    description4.grid(row=0, column=0, columnspan=3)

    row4_img1 = ImageTk.PhotoImage(PIL.Image.open("images/images3/frankie.jpg").resize((175, 175)))
    row4_label1 = Label(row4, image=row4_img1, bg='black', borderwidth=3)
    row4_label1.image = row4_img1
    row4_label1.grid(row=1, column=0)

    row4_img2 = ImageTk.PhotoImage(PIL.Image.open("images/images3/gamble.jpg").resize((175, 175)))
    row4_label2 = Label(row4, image=row4_img2, bg='black', borderwidth=3)
    row4_label2.image = row4_img2
    row4_label2.grid(row=2, column=0, pady=20)

    row4_img3 = ImageTk.PhotoImage(PIL.Image.open("images/images3/phoenix.jpg").resize((175, 175)))
    row4_label3 = Label(row4, image=row4_img3, bg='black', borderwidth=3)
    row4_label3.image = row4_img3
    row4_label3.grid(row=3, column=0)

    # phone password
    entry_frame = Frame(f4, bg='black')
    entry_frame.place(anchor=N, relx=0.67, rely=0.4)

    text = Label(entry_frame, text="Archie has a \n4 digit pin:", font=(s_font, '25'), fg='white', bg='black')
    text.pack(side=TOP, padx=10, pady=(10, 0))

    entry = Entry(entry_frame, font=(s_font, '25'), width=10)
    entry.pack(side=TOP, pady=(20, 10))

    submit_btn = Button(f4, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_tattoo(entry.get(), "4717", 0.67, 0.34, 'black', f4, frame_five))
    submit_btn.place(anchor=CENTER, relx=0.67, rely=0.75)


def frame_five():
    f4.destroy()

    global f5
    f5 = Frame(window, bg=red)
    f5.pack(expand=1, fill=BOTH)

    text = Label(f5, text="\tYou unlock Archie's phone and discover that the last place he searched for on Google Maps"
                          " was a friend's house on Wendwood Drive. You call Archie's friend and find out that Archie "
                          "never got there last night. You reason that he must have gotten stopped on Warwick on the "
                          "way there.\n\n\tAlex says that Archie drove a 2002 light blue Honda Odyssey. You gotta drive"
                          " down Warwick toward Wendwood Drive and find that van.", bg=red, font=(s_font, '25'),
                 wraplength=1000)
    text.place(anchor=CENTER, relx=0.5, rely=0.35)

    entry_frame = Frame(f5, bg='black')
    entry_frame.place(anchor=CENTER, relx=0.5, rely=0.7)

    entry_text = Label(entry_frame, bg='black', fg='white', text="What is the license plate on Archie's van?",
                       font=(s_font, '25'))
    entry_text.pack(side=TOP, pady=(10, 5), padx=10)

    entry = Entry(entry_frame, font=(s_font, '25'), width=15)
    entry.pack(side=TOP, pady=(5, 10))

    submit_btn = Button(f5, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_singular(entry.get(), "use-4881", 0.5, 0.74, 'black', f5,
                                                              frame_six))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_six():
    f5.destroy()

    global f6
    f6 = Frame(window, bg=red)
    f6.pack(expand=1, fill=BOTH)

    text = Label(f6, text="When you get to the van, you can hear the engine humming and the faint sound of music "
                          "playing from inside. You open the driver's door to find Archie slumped unconscious on the"
                          " steering wheel and Alex's voice singing from the car's speakers. Despite shaking him and "
                          "calling his name, you can't get Archie to wake up. At a loss for what else to do, you rush "
                          "Archie to the hospital and hope that there's still time for the doctors to save him.\n\n"
                          "You've done all you can this week. Email sarah.benton.18@cnu.edu a picture of your pet(s) so"
                          " we can know you completed Week 3.",
                 font=(s_font, '28'), bg=red, wraplength=900)
    text.place(anchor=CENTER, relx=0.5, rely=0.5)


if __name__ == "__main__":
    window = Tk()

    window.title("Divine Deviance Week 3")
    window.geometry("1440x900")

    intro_frame = Frame(window, bg='black')
    intro_frame.pack(expand=1, fill=BOTH)

    fire_image = ImageTk.PhotoImage(PIL.Image.open("images/images3/sparks2.png"))
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

    start_button = Button(background_canvas, text="Begin Week\nThree's Journey",
                          font=(s_font, '40', 'bold'), fg="white", bg="black",
                          command=lambda: intro_one(), relief='raised')
    start_button.place(anchor=CENTER, relx=0.5, rely=0.65)

    window.mainloop()
