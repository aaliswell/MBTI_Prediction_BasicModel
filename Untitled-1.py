import tkinter as tk
from tkinter import messagebox
import random

# Colors (adjusted for comfort)
BG_COLOR = "#f5f2e7"   # Soft beige-like
TEXT_COLOR = "#3e2f1c"  # Muted coffee brown
OPTION_BG = "#eae2d3"
OPTION_SELECTED_BG = "#c4b6a5"

# Font
FONT_HEADER = ("Times", 18, "bold italic")
FONT_BODY = ("Times", 14)
FONT_OPTION = ("Times", 12)

# Questions
questions = [
    {"question": "You enjoy spending time with large groups of people.", "options": ["Agree", "Disagree"]},
    {"question": "You prefer to plan things ahead rather than going with the flow.", "options": ["Agree", "Disagree"]},
    {"question": "You enjoy taking on new challenges, even if they are uncertain.", "options": ["Agree", "Disagree"]},
    {"question": "You often make decisions based on logic rather than emotions.", "options": ["Agree", "Disagree"]},
    {"question": "You prefer keeping your options open rather than making plans.", "options": ["Agree", "Disagree"]},
]

# Variables
current_q = 0
selected_option = tk.StringVar()

# Functions
def next_question(event=None):
    global current_q
    if selected_option.get():
        current_q += 1
        if current_q < len(questions):
            load_question()
        else:
            show_result()
    else:
        messagebox.showinfo("Oops!", "Please select an option before continuing.")

def load_question():
    q = questions[current_q]
    question_label.config(text=f"{q['question']}", fg=TEXT_COLOR)
    for idx, opt in enumerate(q["options"]):
        option_buttons[idx].config(text=opt, bg=OPTION_BG, fg=TEXT_COLOR)
        option_buttons[idx].deselect()

def show_result():
    messagebox.showinfo("Quiz Complete", "You have completed the quiz.")

# GUI Setup
root = tk.Tk()
root.title("MBTI Personality Quiz")
root.config(bg=BG_COLOR)
root.geometry("600x400")

# Heading
heading = tk.Label(root, text="Hi, welcome!", font=FONT_HEADER, fg=TEXT_COLOR, bg=BG_COLOR)
heading.pack(pady=10)

# MBTI Intro
intro = tk.Label(
    root,
    text="MBTI (Myers-Briggs Type Indicator) helps you understand how you perceive the world, make decisions, and interact with others.\nThis quiz will ask you 5 questions to give you insight into your personality type.",
    font=FONT_BODY,
    wraplength=550,
    fg=TEXT_COLOR,
    bg=BG_COLOR,
    justify="left"
)
intro.pack(pady=10)

# Question Frame
question_frame = tk.Frame(root, bg=BG_COLOR)
question_frame.pack(pady=10)

question_label = tk.Label(question_frame, font=FONT_BODY, bg=BG_COLOR, fg=TEXT_COLOR, wraplength=550)
question_label.pack()

option_buttons = []
for i in range(2):  # Only 2 options for simplicity
    rb = tk.Radiobutton(
        question_frame,
        variable=selected_option,
        value=str(i),
        font=FONT_OPTION,
        bg=OPTION_BG,
        fg=TEXT_COLOR,
        selectcolor=OPTION_SELECTED_BG,
        anchor="w",
        padx=10,
        pady=5,
        indicatoron=0,
        width=40
    )
    rb.pack(fill="x", pady=2)
    option_buttons.append(rb)

# Next Button
next_btn = tk.Button(root, text="Next", command=next_question, font=FONT_BODY, bg=OPTION_SELECTED_BG)
next_btn.pack(pady=10)

# Enter key binding
root.bind("<Return>", next_question)

# Start
load_question()
root.mainloop()
