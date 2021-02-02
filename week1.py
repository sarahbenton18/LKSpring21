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


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def check_phone_number(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, color, frame, next_func):
    answer = "7215237885"

    if (len(d1) > 1) or (len(d2) > 1) or (len(d3) > 1) or (len(d4) > 1) or (len(d5) > 1) or (len(d6) > 1) or \
            (len(d7) > 1) or (len(d8) > 1) or (len(d9) > 1) or (len(d10) > 1):
        warning_label = Label(frame, text="Each box can only have one character", relief='solid', bg=teal,
                              font=(fancy_font, '18'))
        warning_label.place(anchor=CENTER, relx=0.33, rely=0.9)
        frame.after(4000, warning_label.destroy)

    if (d1 == answer[0]) and (d2 == answer[1]) and (d3 == answer[2]) and (d4 == answer[3]) and (d5 == answer[4]) and \
            (d6 == answer[5]) and (d7 == answer[6]) and (d8 == answer[7]) and (d9 == answer[8]) and (d10 == answer[9]):
        correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
        correct_label = Label(frame, image=correct_image)
        correct_label.image = correct_image
        correct_label.place(anchor=CENTER, relx=0.85, rely=0.75)

        warning_label = Label(frame, text="(Don't actually call the number)", bg=teal,
                              font=(fancy_font, '18'))
        warning_label.place(anchor=CENTER, relx=0.33, rely=0.9)

        next_btn = Button(frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg=color,
                          command=lambda: next_func())
        next_btn.place(anchor=CENTER, relx=0.65, rely=0.9)
    else:
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=0.85, rely=0.75)


def check_gps_coordinates(d1, d2, d3, d4, d5, user_year, color, frame, next_func):
    answer = "45265"
    year = "1970"

    if (len(d1) > 1) or (len(d2) > 1) or (len(d3) > 1) or (len(d4) > 1) or (len(d5) > 1):
        warning_label = Label(frame, text="Each box can only have one character", relief='solid', bg=teal,
                              font=(fancy_font, '18'))
        warning_label.place(anchor=CENTER, relx=0.5, rely=0.3)
        frame.after(4000, warning_label.destroy)

    if (d1 == answer[0]) and (d2 == answer[1]) and (d3 == answer[2]) and (d4 == answer[3]) and (d5 == answer[4]):
        correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
        correct_label = Label(frame, image=correct_image)
        correct_label.image = correct_image
        correct_label.place(anchor=CENTER, relx=0.825, rely=0.18)
    else:
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=0.825, rely=0.18)

    if user_year == year:
        correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
        correct_label = Label(frame, image=correct_image)
        correct_label.image = correct_image
        correct_label.place(anchor=CENTER, relx=0.825, rely=0.75)

    else:
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=0.825, rely=0.75)

    if (d1 == answer[0]) and (d2 == answer[1]) and (d3 == answer[2]) and (d4 == answer[3]) and (d5 == answer[4]) and \
            (user_year == year):
        next_btn = Button(frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg=color,
                          command=lambda: next_func())
        next_btn.place(anchor=CENTER, relx=0.65, rely=0.9)


def check_answer_next(user_entry, answer, relx, rely, color, frame, next_function):
    user_entry = user_entry.lower()
    if (user_entry not in answer) or (user_entry == "") or (user_entry == " "):
        x_image = ImageTk.PhotoImage(PIL.Image.open("images/x.png").resize((35, 35)))
        wrong_label = Label(frame, image=x_image)
        wrong_label.image = x_image
        wrong_label.place(anchor=CENTER, relx=relx + 0.15, rely=rely)
    else:
        user_list.append(user_entry)

    for answer in answer_list:
        if answer not in user_list:
            return

    correct_image = ImageTk.PhotoImage(PIL.Image.open("images/check2.jpg").resize((35, 35)))
    correct_label = Label(frame, image=correct_image)
    correct_label.image = correct_image
    correct_label.place(anchor=CENTER, relx=relx + 0.15, rely=rely)

    next_btn = Button(frame, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg=color,
                      command=lambda: next_function())
    next_btn.place(anchor=CENTER, relx=0.65, rely=0.9)


def frame_one():
    intro_frame.destroy()

    global f1
    f1 = Frame(window, bg=teal)
    f1.pack(expand=1, fill=BOTH)

    top_label = Label(f1, text="You receive a letter...", font=(fancy_font, '30', 'bold'), bg=teal)
    top_label.place(anchor=CENTER, relx=0.5, rely=0.075)

    letter = Label(f1, text="\tSouls lost in blood. We hear their whispers on the wind and watch them haunt this world."
                            " They are stuck in limbo, trapped in the swamp of their own deviance, but have a lust to "
                            "cross over to the other side. As they suffer in icy rain, we refuse "
                            "to turn our backs on this violence. Those who do are frauds. So, we have come out of the "
                            "darkness looking for an addition to our ranks. If you share in our wrath for those trapped"
                            " with the living and you're interested in learning more, give us a ring.\n\t\t\t\t~Dante",
                   wraplength=850, justify=LEFT,
                   font=(type_font, 20),
                   bg=teal)
    letter.place(anchor=CENTER, relx=0.5, rely=0.4)

    e1 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e1.place(anchor=CENTER, relx=0.25, rely=0.75)

    e2 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e2.place(anchor=CENTER, relx=0.3, rely=0.75)

    e3 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e3.place(anchor=CENTER, relx=0.35, rely=0.75)

    dash1 = Label(f1, font=(fancy_font, '40', 'bold'), text='-', bg=teal)
    dash1.place(anchor=CENTER, relx=0.4, rely=0.75)

    e4 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e4.place(anchor=CENTER, relx=0.45, rely=0.75)

    e5 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e5.place(anchor=CENTER, relx=0.5, rely=0.75)

    e6 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e6.place(anchor=CENTER, relx=0.55, rely=0.75)

    dash2 = Label(f1, font=(fancy_font, '40', 'bold'), text='-', bg=teal)
    dash2.place(anchor=CENTER, relx=0.6, rely=0.75)

    e7 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e7.place(anchor=CENTER, relx=0.65, rely=0.75)

    e8 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e8.place(anchor=CENTER, relx=0.7, rely=0.75)

    e9 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e9.place(anchor=CENTER, relx=0.75, rely=0.75)

    e10 = Entry(f1, font=(fancy_font, '40', 'bold'), justify=CENTER, width=2)
    e10.place(anchor=CENTER, relx=0.8, rely=0.75)

    submit_btn = Button(f1, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_phone_number(
                              e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(),
                              e10.get(), 'black', f1, frame_two))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_two():
    f1.destroy()

    global f2
    f2 = Frame(window, bg=teal)
    f2.pack(expand=1, fill=BOTH)

    # go to cabin and burn

    description = Label(f2, text="\tWhen you call the number, a gruff voice answers the phone and tells you to meet him"
                                 " at a specified address at 6pm the following day if you would like to continue. There"
                                 " aren’t many interesting things going on in your life, so you decide to meet him. "
                                 "After all, what do you have to lose?\n\n\tAfter driving along unmarked roads through "
                                 "dense, seemingly uninhabited woods you arrive at the address given to you the "
                                 "previous day. You turn onto what you guess used to be a gravel driveway, but what has"
                                 " now become overgrown with brush and weeds. With your high beams illuminating your "
                                 "path, you creep up the long driveway until you come to a clearing. You see a cabin "
                                 "that looks just as overgrown and abandoned as the driveway. You see no other vehicles"
                                 " or people. You exit your car and explore the clearing. Finding no one, you meekly "
                                 "say, “Hello?” to the still, silent clearing.\n\n\tA light flickers on in the cabin. "
                                 "You figure the person you are supposed to meet is already inside. The rotting boards "
                                 "of the steps creak under the weight of your feet as you enter the cabin through the"
                                 " front door. You find the source of the light - a growing fire in the fireplace - but"
                                 " see no one else. You are beginning to get a little creeped out by your situation. "
                                 "You are supposed to meet someone, but the entire cabin is empty. There are no pieces"
                                 " of furniture or rugs or wall hangings or curtains and the windows are boarded up. "
                                 "Apart from the fireplace, the only other thing in the room is the overwhelming scent "
                                 "of vodka. You decide it’s time to get out.", font=(s_font, '17'),
                        wraplength=1000, justify=LEFT, bg=teal)
    description.place(anchor=CENTER, relx=0.5, rely=0.42)

    next_btn = Button(f2, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_two_a())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_two_a():
    f2.destroy()

    global f2a
    f2a = Frame(window, bg=teal)
    f2a.pack(expand=1, fill=BOTH)

    description = Label(f2a, text="\tBefore you move toward the door, you notice that the fire that had been growing in"
                                  " the fireplace has spilled out of the hearth and caught fire on the wooden floor. "
                                  "You run over to stomp out the flame, but the fire rapidly spreads around the "
                                  "perimeter of the room, catching on the vodka that had been poured out before you "
                                  "arrived. As the fire roars around you, you sprint toward the door, only to watch it"
                                  " slam shut before you can escape. You try to open it, but it is locked from the "
                                  "outside. You bang on the door and scream for help from whoever shut it, but no one"
                                  " is coming to help you. You give up on the door and try to burst through a boarded "
                                  "up window to no avail. The fire is growing quicker than you could imagine and there"
                                  " seems to be no escape. You retreat to the middle of the room as the flames "
                                  "encircle you.\n\n\tWith the heat bearing down around you and your lungs filled with"
                                  " smoke, you feel your life slipping away and there’s nothing left for you to do to "
                                  "stop it. Curled up in a ball on the ground in the middle of the cabin, everything "
                                  "goes dark.", font=(s_font, '20'), wraplength=1000, justify=LEFT, bg=teal)
    description.place(anchor=CENTER, relx=0.5, rely=0.45)

    next_btn = Button(f2a, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_three())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_three():
    f2a.destroy()

    global f3
    f3 = Frame(window, bg=teal)
    f3.pack(expand=1, fill=BOTH)

    # you wake up and there's a ghost!

    description = Label(f3, text="\tWhen you wake up, you find yourself lying in the grass just outside the scorched "
                                 "cabin. The smell of smoke still lingers in the crisp morning air as you begin to "
                                 "remember what happened last night. The smoke. The flames. The locked door. The "
                                 "boarded up windows. The panic. You don’t remember ever making it out. In fact, you"
                                 " recall taking your last breath inside the cabin… But somehow you are outside now. "
                                 "And, most importantly, you’re still alive. Apart from a few minor burns, an "
                                 "insistent, moderately explosive cough, and your charred clothes, you feel fine."
                                 "\n\n\tYou notice a piece of paper on the ground next to you. Picking it up, you "
                                 "find that it simply says “Good luck.” With what? You have no idea.\n\nDropping the "
                                 "paper on the ground where you found it, you decide to head back to your car and get"
                                 " as far from this cursed place as possible. You search through your pockets, "
                                 "relieved to find that your keys are still with you. When you look up from your "
                                 "pockets, about to take a step down the path toward the driveway, you freeze, finding"
                                 " yourself face to face with another person.\n\n\tAlarmed by the sudden and "
                                 "unexpected presence, you jolt backwards.", font=(s_font, '17'), wraplength=1000,
                        justify=LEFT, bg=teal)
    description.place(anchor=CENTER, relx=0.5, rely=0.45)

    next_btn = Button(f3, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_four())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_four():
    f3.destroy()

    global f4
    f4 = Frame(window, bg=teal)
    f4.pack(expand=1, fill=BOTH)

    # greedy ghost introduction!
    description = Label(f4, text="\tA ghostly old man stands before you.\n\n\t\"Please,\" he says. \"You have to "
                                 "help me.\"\n\n\tUnsure if he is the one who trapped you in the cabin, is the one "
                                 "who saved you before you burned alive, is another future victim like you, or is just"
                                 " some random old man, you say nothing.\n\n\t\"I’m trapped here,\" continues the old"
                                 " man, still looking distressed. \"I only ever cared about money and material "
                                 "possessions. Greed consumed my life. But now… Now I can see how much damage this "
                                 "caused to those around me. I can’t rest until I do something about it.\"\n\n\tYou’re"
                                 " not entirely sure why this guy is spewing his strange life story. You think it "
                                 "could be another trick like the cabin, so you start walking around him.\n\n\t\""
                                 "Wait!\" pleads the old man, reaching a hand out to you. His hand passes through "
                                 "your shoulder, sending goosebumps down your spine. You suddenly realize that the"
                                 " ghostly old man is actually a ghost.", font=(s_font, '16'), wraplength=800,
                        justify=LEFT, bg=teal)
    description.place(anchor=CENTER, relx=0.33, rely=0.45)

    ghost_image = ImageTk.PhotoImage(PIL.Image.open("images/Sullivan.jpeg").resize((350, 400)))
    ghost_label = Label(f4, image=ghost_image)
    ghost_label.image = ghost_image
    ghost_label.place(anchor=CENTER, relx=0.8, rely=0.5)

    next_btn = Button(f4, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_four_a())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_four_a():
    f4.destroy()

    global f4a
    f4a = Frame(window, bg=teal)
    f4a.pack(expand=1, fill=BOTH)

    description = Label(f4a, text="\n\n\t\"They said you would help me,\" "
                                 "continues the old man. \"You have to help me.\"\n\n\tPerplexed as to how you could"
                                 " possibly be seeing a ghost, you demand that the ghost tell you what is happening."
                                 " The ghost admits that he’s just as confused as you. All he knows is that some "
                                 "group called the Society of the Divine Deviants led him here and told him to "
                                 "find you. The ghost says they said that you would help him right his sins. Only "
                                 "then would you get more information about the Society and your newfound ability "
                                 "of ghost sight.\n\n\tUnable to think of another viable option, you agree to help"
                                 " the ghost.\n\n\tThe ghost then tells you more about himself. His name is Howard "
                                 "Sullivan and he worked for over 40 years as a politician in DC. He cared less about "
                                 "his constituents and more about how to secure the greatest profits for himself. "
                                 "This attitude resulted in countless deals and pieces of legislation that often "
                                 "hurt the people who elected him, but benefited the special interest groups that"
                                 " were willing to pay him off. Looking back, he can see that he was sleazy and "
                                 "prepared to do anything to increase his wealth. Now that he’s dead, he needs all "
                                 "that money to go back to a good cause. He needs your help finding his fortune and "
                                 "donating it to the right charity. Step 1, drain his bank account.",
                        font=(s_font, '17'), wraplength=1000, justify=LEFT, bg=teal)
    description.place(anchor=CENTER, relx=0.5, rely=0.4)

    next_btn = Button(f4a, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                      command=lambda: frame_five())
    next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_five():
    f4a.destroy()

    global f5
    f5 = Frame(window, bg=teal)
    f5.pack(expand=1, fill=BOTH)

    global answer_list
    answer_list = ["easter island"]

    global user_list
    user_list = []

    top_label = Label(f5, text="After logging into Howard's bank account, a security question pops up to verify your "
                               "identity.",
                      font=(fancy_font, '25', 'bold'), bg=teal)
    top_label.place(anchor=CENTER, relx=0.5, rely=0.05)

    # security question frame
    question_frame = Frame(f5, bg='#DCDBDB', borderwidth=3, relief='solid')
    question_frame.place(anchor=CENTER, relx=0.5, rely=0.175)
    # question_frame.grid(row=1)

    question = Label(question_frame, text="Where was your third honeymoon?",
                     font=(comp_font, '25'), bg='#DCDBDB')
    question.pack(side=TOP, pady=5, padx=5)

    q_entry = Entry(question_frame, font=(comp_font, '20'), justify=CENTER)
    q_entry.pack(side=BOTTOM, pady=5)

    instruction_frame_row_one = Frame(f5, bg=teal)
    instruction_frame_row_one.place(anchor=CENTER, relx=0.5, rely=0.34)

    label_one = Label(instruction_frame_row_one, text="Howard has been ", font=(fancy_font, '25'), bg=teal)
    label_one.pack(side=LEFT)

    label_two = Label(instruction_frame_row_one, text="absent", font=(fancy_font, '25', 'bold'), bg=teal)
    label_two.pack(side=LEFT)

    label_three = Label(instruction_frame_row_one, text="for most of his life... Never taking ",
                        font=(fancy_font, '25'), bg=teal)
    label_three.pack(side=LEFT)

    instruction_frame_row_two = Frame(f5, bg=teal)
    instruction_frame_row_two.place(anchor=CENTER, relx=0.5, rely=0.44)

    label_four = Label(instruction_frame_row_one, text="stock", font=(fancy_font, '25', 'bold'), bg=teal)
    label_four.pack(side=LEFT)

    label_five = Label(instruction_frame_row_one, text="of what really matters.", font=(fancy_font, '25'), bg=teal)
    label_five.pack(side=LEFT)

    label_six = Label(instruction_frame_row_two, text="His mind ",
                      font=(fancy_font, '25'), bg=teal)
    label_six.pack(side=LEFT)

    label_seven = Label(instruction_frame_row_two, text="scrambles", font=(fancy_font, '25', 'bold'), bg=teal)
    label_seven.pack(side=LEFT)

    label_eight = Label(instruction_frame_row_two, text="to no avail. So you click on the hint and this box pops up.",
                        font=(fancy_font, '25'), bg=teal)
    label_eight.pack(side=LEFT)

    # stock information
    stock_frame = Frame(f5, bg='#DCDBDB', borderwidth=3, relief='solid')
    stock_frame.place(anchor=CENTER, relx=0.5, rely=0.65)
    # stock_frame.grid(row=3)

    stock1 = Label(stock_frame, text="ESCA", font=(comp_font, '40'), bg='#DCDBDB')
    stock1.grid(row=0, column=0, padx=20, pady=10)

    stock2 = Label(stock_frame, text="EXPR", font=(comp_font, '40'), bg='#DCDBDB')
    stock2.grid(row=1, column=0, padx=20, pady=10)

    stock3 = Label(stock_frame, text="ABNB", font=(comp_font, '40'), bg='#DCDBDB')
    stock3.grid(row=0, column=1, padx=20, pady=10)

    stock4 = Label(stock_frame, text="GLOB", font=(comp_font, '40'), bg='#DCDBDB')
    stock4.grid(row=1, column=1, padx=20, pady=10)

    # stock5 = Label(stock_frame, text="{:<8} :  ${:>3}.{:>3}".format("FB", "20", "91"), font=(comp_font, '25'),
    #                bg='#DCDBDB')
    # stock5.grid(row=0, column=1, padx=7, pady=2)
    #
    # stock6 = Label(stock_frame, text="{:<8} :  ${:>3}.{:>3}".format("AMZN", "232", "89"), font=(comp_font, '25'),
    #                bg='#DCDBDB')
    # stock6.grid(row=1, column=1, padx=7, pady=2)
    #
    # stock7 = Label(stock_frame, text="{:<8} :  ${:>3}.{:>3}".format("NINOY", "24", "95"), font=(comp_font, '25'),
    #                bg='#DCDBDB')
    # stock7.grid(row=2, column=1, padx=7, pady=2)
    #
    # stock8 = Label(stock_frame, text="{:<8} :  ${:>3}.{:>3}".format("GRPN", "105", "00"), font=(comp_font, '25'),
    #                bg='#DCDBDB')
    # stock8.grid(row=3, column=1, padx=7, pady=2)

    submit_btn = Button(f5, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: check_answer_next(q_entry.get(), "easter island", 0.5, 0.217, 'black', f5,
                                                          frame_six))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def frame_six():
    f5.destroy()

    global f6
    f6 = Frame(window, bg=teal)
    f6.pack(expand=1, fill=BOTH)

    purple = '#DEB3DA'

    top_label = Label(f6, text="Like any good investor, Howard diversified his portfolio. Now you must find his "
                               "gold bars.", font=(fancy_font, '25', 'bold'), bg=teal)
    top_label.place(anchor=CENTER, relx=0.5, rely=0.05)

    # gps coordinate frame
    gps_frame = Frame(f6, bg=teal)
    gps_frame.place(anchor=CENTER, relx=0.5, rely=0.175)

    # gem coordinates
    gem_version = Frame(gps_frame, bg='#DCDBDB', borderwidth=3, relief='solid')
    gem_version.pack(side=LEFT, padx=(5, 10))

    row1 = Frame(gem_version, bg=gray)
    row1.grid(row=0, column=0, padx=3, pady=(2, 0))

    row_1_p1 = Label(row1, text="37° 03' ", bg=gray, font=(comp_font, '28'))
    row_1_p1.pack(side=LEFT)

    emerald = ImageTk.PhotoImage(PIL.Image.open("images/emerald.png").resize((43, 43)))
    row_1_p2 = Label(row1, image=emerald, bg=gray)
    row_1_p2.image = emerald
    row_1_p2.pack(side=LEFT)

    amethyst = ImageTk.PhotoImage(PIL.Image.open("images/amethyst.png").resize((43, 43)))
    row_1_p3 = Label(row1, image=amethyst, bg=gray)
    row_1_p3.image = emerald
    row_1_p3.pack(side=LEFT)

    row_1_p4 = Label(row1, text=". 7\" N", bg=gray, font=(comp_font, '28'))
    row_1_p4.pack(side=LEFT)

    row2 = Frame(gem_version, bg=gray)
    row2.grid(row=1, column=0, padx=3, pady=(0, 2))

    row_2_p1 = Label(row2, text="76° ", bg=gray, font=(comp_font, '28'))
    row_2_p1.pack(side=LEFT)

    ruby = ImageTk.PhotoImage(PIL.Image.open("images/ruby.png").resize((43, 43)))
    row_2_p2 = Label(row2, image=ruby, bg=gray)
    row_2_p2.image = ruby
    row_2_p2.pack(side=LEFT)

    sapphire = ImageTk.PhotoImage(PIL.Image.open("images/sapphire.png").resize((43, 43)))
    row_2_p3 = Label(row2, image=sapphire, bg=gray)
    row_2_p3.image = sapphire
    row_2_p3.pack(side=LEFT)

    row_2_p4 = Label(row2, text="' 03 . ", bg=gray, font=(comp_font, '28'))
    row_2_p4.pack(side=LEFT)

    row_2_p5 = Label(row2, image=amethyst, bg=gray)
    row_2_p5.image = amethyst
    row_2_p5.pack(side=LEFT)

    row_2_p6 = Label(row2, text="\" W", bg=gray, font=(comp_font, '28'))
    row_2_p6.pack(side=LEFT)

    # entry coordinates
    entry_version = Frame(gps_frame, bg='#DCDBDB', borderwidth=3, relief='solid')
    entry_version.pack(side=RIGHT, padx=(3, 10))

    row1b = Frame(entry_version, bg=gray)
    row1b.grid(row=0, column=0, padx=3, pady=(2, 0))

    row_1b_p1 = Label(row1b, text="37° 03' ", bg=gray, font=(comp_font, '28'))
    row_1b_p1.pack(side=LEFT)

    entry1 = Entry(row1b, font=(comp_font, '28'), justify=CENTER, width=2)
    entry1.pack(side=LEFT, padx=(0, 4))

    entry2 = Entry(row1b, font=(comp_font, '28'), justify=CENTER, width=2)
    entry2.pack(side=LEFT)

    row_1b_p2 = Label(row1b, text=" . 7\" N", bg=gray, font=(comp_font, '28'))
    row_1b_p2.pack(side=LEFT)

    row2b = Frame(entry_version, bg=gray)
    row2b.grid(row=1, column=0, padx=3, pady=(0, 2))

    row_2b_p1 = Label(row2b, text="76° ", bg=gray, font=(comp_font, '28'))
    row_2b_p1.pack(side=LEFT)

    entry3 = Entry(row2b, font=(comp_font, '28'), justify=CENTER, width=2)
    entry3.pack(side=LEFT, padx=(0, 4))

    entry4 = Entry(row2b, font=(comp_font, '28'), justify=CENTER, width=2)
    entry4.pack(side=LEFT)

    row_2b_p2 = Label(row2b, text=" ' 03 . ", bg=gray, font=(comp_font, '28'))
    row_2b_p2.pack(side=LEFT)

    entry5 = Entry(row2b, font=(comp_font, '28'), justify=CENTER, width=2)
    entry5.pack(side=LEFT)

    row_2b_p3 = Label(row2b, text=" \" W", bg=gray, font=(comp_font, '28'))
    row_2b_p3.pack(side=LEFT)

    # gem frame
    gem_frame = Frame(f6, bg='#DCDBDB', borderwidth=3, relief='solid')
    gem_frame.place(anchor=CENTER, relx=0.5, rely=0.475)

    gem1_image = ImageTk.PhotoImage(PIL.Image.open("images/gem1.png").resize((200, 175)))
    gem1 = Label(gem_frame, image=gem1_image, bg='black')
    gem1.image = gem1_image
    gem1.grid(row=0, column=0)

    gem2_image = ImageTk.PhotoImage(PIL.Image.open("images/gem2.png").resize((200, 175)))
    gem2 = Label(gem_frame, image=gem2_image, bg='black')
    gem2.image = gem2_image
    gem2.grid(row=0, column=1)

    gem3_image = ImageTk.PhotoImage(PIL.Image.open("images/gem3.png").resize((200, 175)))
    gem3 = Label(gem_frame, image=gem3_image, bg='black')
    gem3.image = gem3_image
    gem3.grid(row=0, column=2)

    gem4_image = ImageTk.PhotoImage(PIL.Image.open("images/gem4.png").resize((200, 175)))
    gem4 = Label(gem_frame, image=gem4_image, bg='black')
    gem4.image = gem4_image
    gem4.grid(row=0, column=3)

    # gold bar location description
    description = Label(f6, text="Buried near the place where a branch of the arched tree meets the base of another "
                                 "tree.", wraplength=500, bg=purple, font=(comp_font, '20'), borderwidth=3,
                        relief='solid', padx=5, pady=5)
    description.place(anchor=CENTER, relx=0.33, rely=0.75)

    # gold bar question frame
    question_frame = Frame(f6, bg=purple, borderwidth=3, relief='solid')
    question_frame.place(anchor=CENTER, relx=0.66, rely=0.75)

    question = Label(question_frame, text="When did his daughter die?", font=(comp_font, '20'), bg=purple)
    question.pack(side=TOP, pady=5, padx=5)

    q_entry = Entry(question_frame, font=(comp_font, '20'), justify=CENTER)
    q_entry.pack(side=BOTTOM, pady=5)

    submit_btn = Button(f6, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_gps_coordinates(entry1.get(), entry2.get(), entry3.get(),
                                                                            entry4.get(), entry5.get(), q_entry.get(),
                                                                            'black', f6, frame_seven)))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.9)


def safe_button(num):
    current = text['text']
    new = current + num
    text.config(text=new)


def enter_button():
    current = text['text']

    if current == "81362":
        next_btn = Button(f7, text="Next", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                          command=lambda: frame_eight())
        next_btn.place(anchor=CENTER, relx=0.5, rely=0.9)

        green_circle = safe_canvas.create_oval(0, 0, 35, 35, fill='green')

    else:
        text.config(text="")


def frame_seven():
    f6.destroy()

    global f7
    f7 = Frame(window, bg=teal)
    f7.pack(expand=1, fill=BOTH)

    # green = '#27BD24'
    green = '#BFF2FA'

    top_label = Label(f7, text="You are able to find his safety deposit box inside the bank, but you need a "
                               "combination.", font=(fancy_font, '25', 'bold'), bg=teal)
    top_label.place(anchor=CENTER, relx=0.5, rely=0.1)

    # combo description frame
    i_frame = Frame(f7, bg=green, relief='solid', borderwidth=3)
    i_frame.place(anchor=CENTER, relx=0.25, rely=0.5)

    instructions = Label(i_frame, text="Look around the Bank of America parking lot\n", wraplength=400, bg=green,
                         font=(comp_font, '25'))
    instructions.pack(side=TOP)

    q_one = Label(i_frame, text="Last digit of street address", bg=green, justify=LEFT, font=(comp_font, '25'))
    q_one.pack(side=TOP, pady=10, padx=10)

    q_two = Label(i_frame, text="# lamp posts", bg=green, justify=LEFT, font=(comp_font, '25'))
    q_two.pack(side=TOP, pady=10)

    q_three = Label(i_frame, text="# drive-thru teller lanes", bg=green, justify=LEFT, font=(comp_font, '25'))
    q_three.pack(side=TOP, pady=10)

    q_four = Label(i_frame, text="# handicap spaces", bg=green, justify=LEFT, font=(comp_font, '25'))
    q_four.pack(side=TOP, pady=10)

    # q_five = Label(i_frame, text="#", bg=gray, justify=LEFT, font=(comp_font, '25'))
    # q_five.pack(side=TOP)

    # safe frame
    safe_frame = Frame(f7, bg='black', relief='solid', borderwidth=3)
    safe_frame.place(anchor=CENTER, relx=0.75, rely=0.5)

    # top part
    top_frame = Frame(safe_frame, bg='black')
    top_frame.pack(side=TOP, pady=(5, 10))

    global text
    text = Label(top_frame, text="", width=15, bg='black', justify=LEFT, fg=green, font=(comp_font, '40'))
    text.pack(side=LEFT)

    global safe_canvas
    safe_canvas = Canvas(top_frame, bg='black', highlightthickness=0, height=35, width=35)
    red_circle = safe_canvas.create_oval(0, 0, 35, 35, fill='red')
    safe_canvas.pack(side=RIGHT, padx=(0, 30))

    # button panel
    buttons = Frame(safe_frame, bg=green)
    buttons.pack(side=BOTTOM)

    font_size = '30'

    but_1 = Button(buttons, text="1", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('1'))
    but_1.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

    but_2 = Button(buttons, text="2", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('2'))
    but_2.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

    but_3 = Button(buttons, text="3", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('3'))
    but_3.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')

    but_4 = Button(buttons, text="4", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('4'))
    but_4.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

    but_5 = Button(buttons, text="5", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('5'))
    but_5.grid(row=1, column=1, padx=2, pady=2, sticky='nesw')

    but_6 = Button(buttons, text="6", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('6'))
    but_6.grid(row=1, column=2, padx=2, pady=2, sticky='nesw')

    but_7 = Button(buttons, text="7", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('7'))
    but_7.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')

    but_8 = Button(buttons, text="8", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('8'))
    but_8 .grid(row=2, column=1, padx=2, pady=2, sticky='nesw')

    but_9 = Button(buttons, text="9", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', command=lambda: safe_button('9'))
    but_9.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')

    but_0 = Button(buttons, text="0", font=(comp_font, font_size), relief="raised", borderwidth=3, fg=green,
                   bg='black', width=7, command=lambda: safe_button('0'))
    but_0.grid(row=3, column=1, padx=2, pady=2, sticky='nesw')

    but_clear = Button(buttons, text="clear", font=(comp_font, '20', 'bold'), relief="raised", borderwidth=3,
                       fg='white', bg='black', width=10, command=lambda: text.config(text=""))
    but_clear.grid(row=3, column=0, padx=2, pady=2, sticky='nesw')

    but_enter = Button(buttons, text="enter", font=(comp_font, '20', 'bold'), relief="raised", borderwidth=3,
                       fg='white', bg='black', width=10, command=lambda: enter_button())
    but_enter.grid(row=3, column=2, padx=2, pady=2, sticky='nesw')


def frame_eight():
    f7.destroy()

    global f8
    f8 = Frame(window, bg=teal)
    f8.pack(expand=1, fill=BOTH)

    global answer_list
    answer_list = ["feeding america", "st. jude children's research hospital", "american cancer society",
                   "make-a-wish", "american red cross", "toys for tots", "defeat diabetes foundation",
                   "ronald mcdonald house charities", "bill & melinda gates foundation", "wwf"]

    global user_list
    user_list = []

    top_label = Label(f8, text="After retrieving the gold bars from the safety deposit box, you are ready to donate "
                               "the money.\nHoward wants to spread his fortune around, so he has picked ten charities. "
                               "Order them to figure out how much to donate to each.", font=(fancy_font, '20', 'bold'),
                      bg=teal)
    top_label.place(anchor=CENTER, relx=0.5, rely=0.07)

    # information frame
    info_frame = Frame(f8, bg=gray, relief='solid', borderwidth=3)
    info_frame.place(anchor=CENTER, relx=0.31, rely=0.5)

    logo_frame = Frame(info_frame, bg='white')
    logo_frame.pack(side=TOP)

    cross_image = ImageTk.PhotoImage(PIL.Image.open("images/cross.jpg").resize((150, 75)))
    cross = Label(logo_frame, image=cross_image, bg='white')
    cross.image = cross_image
    cross.grid(row=0, column=0)

    bill_image = ImageTk.PhotoImage(PIL.Image.open("images/bill.png").resize((150, 75)))
    bill = Label(logo_frame, image=bill_image, bg='white')
    bill.image = bill_image
    bill.grid(row=0, column=1)

    cancer_image = ImageTk.PhotoImage(PIL.Image.open("images/cancer.png").resize((150, 75)))
    cancer = Label(logo_frame, image=cancer_image, bg='white')
    cancer.image = cancer_image
    cancer.grid(row=0, column=2)

    diabetes_image = ImageTk.PhotoImage(PIL.Image.open("images/diabetes.png").resize((150, 75)))
    diabetes = Label(logo_frame, image=diabetes_image, bg='white')
    diabetes.image = diabetes_image
    diabetes.grid(row=0, column=3)

    feed_image = ImageTk.PhotoImage(PIL.Image.open("images/feed.png").resize((150, 75)))
    feed = Label(logo_frame, image=feed_image, bg='white')
    feed.image = feed_image
    feed.grid(row=0, column=4)

    jude_image = ImageTk.PhotoImage(PIL.Image.open("images/jude.png").resize((150, 75)))
    jude = Label(logo_frame, image=jude_image, bg='white')
    jude.image = jude_image
    jude.grid(row=1, column=0)

    mc_image = ImageTk.PhotoImage(PIL.Image.open("images/mc.jpg").resize((150, 75)))
    mc = Label(logo_frame, image=mc_image, bg='white')
    mc.image = mc_image
    mc.grid(row=1, column=1)

    tots_image = ImageTk.PhotoImage(PIL.Image.open("images/tots.jpg").resize((150, 75)))
    tots = Label(logo_frame, image=tots_image, bg='white')
    tots.image = tots_image
    tots.grid(row=1, column=2)

    wish_image = ImageTk.PhotoImage(PIL.Image.open("images/wish.png").resize((150, 75)))
    wish = Label(logo_frame, image=wish_image, bg='white')
    wish.image = wish_image
    wish.grid(row=1, column=3)

    wwf_image = ImageTk.PhotoImage(PIL.Image.open("images/wwf.jpg").resize((150, 75)))
    wwf = Label(logo_frame, image=wwf_image, bg='white')
    wwf.image = wwf_image
    wwf.grid(row=1, column=4)

    # description frame
    sent_frame = Frame(info_frame, bg=gray)
    sent_frame.pack(side=BOTTOM)

    row1 = Label(sent_frame, text="Of the two children's charities in the first half of the list, the one founded "
                                  "earlier appears earlier on the list.", wraplength=725, font=(comp_font, '15'),
                 bg=gray)
    row1.pack(side=TOP)

    row2 = Label(sent_frame, text="Charities directly related to cancer are next to each other.", wraplength=725,
                 font=(comp_font, '15'), bg=gray)
    row2.pack(side=TOP)

    row3 = Label(sent_frame, text="Charities with the word America in their title must be in the first half.",
                 wraplength=725, font=(comp_font, '15'), bg=gray)
    row3.pack(side=TOP)

    row4 = Label(sent_frame, text="The logo without color is last.", wraplength=725, font=(comp_font, '15'), bg=gray)
    row4.pack(side=TOP)

    row5 = Label(sent_frame, text="Bill and Melinda Gates Foundation is next to another charity with a name in the "
                                  "title.", wraplength=725, font=(comp_font, '15'), bg=gray)
    row5.pack(side=TOP)

    row5a = Label(sent_frame, text="If there is a disease in the name of the charity, it is a prime number.",
                  wraplength=725, font=(comp_font, '15'), bg=gray)
    row5a.pack(side=TOP)

    row6 = Label(sent_frame, text="Toys for Tots and Ronald McDonald House Charities come later in the list than "
                                  "the Make-A-Wish.", wraplength=725, font=(comp_font, '15'), bg=gray)
    row6.pack(side=TOP)

    row7 = Label(sent_frame, text="All charities directly related to children fall on even numbers.",
                 font=(comp_font, '15'), bg=gray)
    row7.pack(side=TOP)

    row8 = Label(sent_frame, text="The oldest charity is number five.", wraplength=725, font=(comp_font, '15'), bg=gray)
    row8.pack(side=TOP)

    # entry frame
    entry_frame = Frame(f8, bg=gray, relief='solid', borderwidth=3)
    entry_frame.place(anchor=CENTER, relx=0.78, rely=0.5)

    row1_label = Label(entry_frame, text="1 (25%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row1_label.grid(row=0, column=0)

    row1_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row1_entry.grid(row=0, column=1)

    row2_label = Label(entry_frame, text="2 (20%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row2_label.grid(row=1, column=0)

    row2_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row2_entry.grid(row=1, column=1)

    row3_label = Label(entry_frame, text="3 (15%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row3_label.grid(row=2, column=0)

    row3_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row3_entry.grid(row=2, column=1)

    row4_label = Label(entry_frame, text="4 (10%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row4_label.grid(row=3, column=0)

    row4_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row4_entry.grid(row=3, column=1)

    row5_label = Label(entry_frame, text="5 (8%)- ", font=(comp_font, '20', 'bold'), bg=gray)
    row5_label.grid(row=5, column=0)

    row5_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row5_entry.grid(row=5, column=1)

    row6_label = Label(entry_frame, text="6 (7%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row6_label.grid(row=6, column=0)

    row6_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row6_entry.grid(row=6, column=1)

    row7_label = Label(entry_frame, text="7 (6%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row7_label.grid(row=7, column=0)

    row7_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row7_entry.grid(row=7, column=1)

    row8_label = Label(entry_frame, text="8 (4%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row8_label.grid(row=8, column=0)

    row8_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row8_entry.grid(row=8, column=1)

    row9_label = Label(entry_frame, text="9 (2%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row9_label.grid(row=9, column=0)

    row9_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row9_entry.grid(row=9, column=1)

    row10_label = Label(entry_frame, text="10 (1%) - ", font=(comp_font, '20', 'bold'), bg=gray)
    row10_label.grid(row=10, column=0)

    row10_entry = Entry(entry_frame, font=(comp_font, '20'), width=20)
    row10_entry.grid(row=10, column=1)

    helpful_label = Label(f8, text="Be sure to type your answers as seen in the logo (e.g. WWF, Make-A-Wish, "
                                   "Bill & ...)", wraplength=200, font=(fancy_font, '15'), bg=teal)
    helpful_label.place(anchor=CENTER, relx=0.8, rely=0.9)

    submit_btn = Button(f8, text="Submit", font=(fancy_font, '25', 'bold'), fg='white', bg='black',
                        command=lambda: combine_funcs(check_answer_next(row1_entry.get(), "feeding america", 0.81, 0.5,
                                                                        'black', f8, frame_nine),
                                                      check_answer_next(row2_entry.get(), "st. jude children's research"
                                                                                          " hospital", 0.81, 0.5,
                                                                        'black', f8, frame_nine),
                                                      check_answer_next(row3_entry.get(), "american cancer society",
                                                                        0.81, 0.5, 'black', f8, frame_nine),
                                                      check_answer_next(row4_entry.get(), "make-a-wish",
                                                                        0.81, 0.5, 'black', f8, frame_nine),
                                                      check_answer_next(row5_entry.get(), "american red cross", 0.81,
                                                                        0.5, 'black', f8, frame_nine),
                                                      check_answer_next(row6_entry.get(), "toys for tots", 0.81, 0.5,
                                                                        'black', f8, frame_nine),
                                                      check_answer_next(row7_entry.get(), "defeat diabetes foundation",
                                                                        0.81, 0.5, 'black', f8, frame_nine),
                                                      check_answer_next(row8_entry.get(), "ronald mcdonald house "
                                                                                          "charities", 0.81, 0.5,
                                                                        'black', f8, frame_nine),
                                                      check_answer_next(row9_entry.get(), "bill & melinda gates "
                                                                                          "foundation", 0.81, 0.5,
                                                                        'black', f8, frame_nine),
                                                      check_answer_next(row10_entry.get(), "wwf", 0.81,
                                                                        0.5, 'black', f8, frame_nine)
                                                      ))
    submit_btn.place(anchor=CENTER, relx=0.5, rely=0.925)


def frame_nine():
    f8.destroy()

    global f9
    f9 = Frame(window, bg=teal)
    f9.pack(expand=1, fill=BOTH)

    top_label = Label(f9, text="You disperse Howard's fortune to the charities of his choice, thus completing his "
                               "quest to transform his life of ruthless greed into a benefit to others. Howard thanks"
                               " you for all your help along the way.\n Before you get the chance to ask him anything "
                               "about what happened in the cabin or the Society of Divine Deviants, his ghost dissolves"
                               " away before your eyes, taking any answers with him.", wraplength=800,
                      font=(s_font, '30', 'bold'), bg=teal)
    top_label.place(anchor=CENTER, relx=0.5, rely=0.4)

    congrats_label = Label(f9, text="Congratulations! You have finished Week 1. Please email us a TV show "
                                    "recommendation so we can know you completed this week :)", wraplength=800,
                           font=(s_font, '20', 'bold'), bg=teal)
    congrats_label.place(anchor=CENTER, relx=0.5, rely=0.9)


if __name__ == "__main__":
    window = Tk()
    window.title("Divine Deviance Week 1")
    window.state('zoomed')

    intro_frame = Frame(window, bg=teal)
    intro_frame.pack(expand=1, fill=BOTH)

    lk_label = Label(intro_frame, text="Lock and Key Club presents...", font=(fancy_font, '50', 'bold'), bg=teal)
    lk_label.place(anchor=CENTER, relx=0.5, rely=.15)

    intro_label = Label(intro_frame, text="Divine Deviance:\nWeek One", font=(fancy_font, '100', 'bold'), borderwidth=5,
                        relief='solid', padx=10, bg=teal)
    intro_label.place(anchor=CENTER, relx=0.5, rely=0.5)

    start_button = Button(intro_frame, text="Start", font=(fancy_font, '25', 'bold'), fg="white", bg="black",
                          command=lambda: frame_one())
    start_button.place(anchor=CENTER, relx=0.5, rely=0.9)

    # print(font.families())

    window.mainloop()
