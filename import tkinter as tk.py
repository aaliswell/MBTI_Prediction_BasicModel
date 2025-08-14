import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the quiz questions and options
questions = [
    ("You’re at a gathering. What do you prefer?",
     ["Engaging with many, even if briefly",
      "Having deep conversations with a few",
      "Staying near people but not talking much",
      "Observing quietly and enjoying the atmosphere"],
     "IE"),
    # Add 14 more questions here in similar format...
    ("How do you process new information best?",
     ["Step-by-step and factual",
      "Through patterns and possibilities",
      "Practical application and results",
      "Ideas and abstract thinking"],
     "SN"),
    # ... continue to total 15 questions
]

scores = {"I": 0, "E": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
current_question = 0
selected_name = ""

# Create the main app window
root = tk.Tk()
root.title("MBTI Personality Quiz")
root.geometry("1000x700")
root.configure(bg='#f3f0e9')  # Cozy background color

# Load and set the background image
def set_background():
    bg_image = Image.open("sunlit_study_corner_mbti.png")
    bg_image = bg_image.resize((1000, 700))
    bg_photo = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(root, image=bg_photo)
    background_label.image = bg_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

set_background()

container = tk.Frame(root, bg='white', bd=0)
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

name_var = tk.StringVar()
question_label = None
option_buttons = []

# Screens and logic
def start_screen():
    clear_container()
    tk.Label(container, text="Welcome to the MBTI Personality Quiz!", font=("Times New Roman", 24, "italic"), fg="#5a3e2b", bg='white').pack(pady=20)
    tk.Label(container, text="Enter your name:", font=("Times New Roman", 16), bg='white').pack()
    name_entry = tk.Entry(container, textvariable=name_var, font=("Times New Roman", 14), width=30, bd=2, relief="groove", justify='center')
    name_entry.pack(pady=10)
    tk.Button(container, text="Start Quiz", command=show_mbti_intro, font=("Times New Roman", 14), bg="#d4bfa3", relief="ridge").pack(pady=20)

def show_mbti_intro():
    global selected_name
    selected_name = name_var.get()
    if not selected_name.strip():
        messagebox.showwarning("Name Required", "Please enter your name to begin the quiz.")
        return
    clear_container()
    tk.Label(container, text=f"Welcome, {selected_name}!", font=("Times New Roman", 22, "italic"), fg="#5a3e2b", bg='white').pack(pady=10)
    intro_text = ("The Myers-Briggs Type Indicator (MBTI) is a tool that helps you discover your personality type.\n"
                  "It is based on how you perceive the world and make decisions. Let's explore your preferences!")
    tk.Label(container, text=intro_text, wraplength=700, font=("Times New Roman", 14), bg='white', justify='center').pack(pady=20)
    tk.Button(container, text="Continue to Quiz", command=show_question, font=("Times New Roman", 14), bg="#d4bfa3").pack(pady=20)

def show_question():
    clear_container()
    global question_label, option_buttons
    q_text, options, trait_pair = questions[current_question]
    question_label = tk.Label(container, text=q_text, font=("Times New Roman", 18, "italic"), bg='white', fg='#4a3628', wraplength=800)
    question_label.pack(pady=20)
    option_buttons = []
    for idx, opt in enumerate(options):
        btn = tk.Button(container, text=opt, wraplength=600, font=("Times New Roman", 13), width=50, bg="#f0e5d8",
                        relief="groove", command=lambda i=idx: record_answer(i))
        btn.pack(pady=8)
        option_buttons.append(btn)

def record_answer(index):
    global current_question
    trait_pair = questions[current_question][2]
    if trait_pair == "IE":
        scores["I" if index > 1 else "E"] += 1
    elif trait_pair == "SN":
        scores["S" if index < 2 else "N"] += 1
    elif trait_pair == "TF":
        scores["T" if index < 2 else "F"] += 1
    elif trait_pair == "JP":
        scores["J" if index < 2 else "P"] += 1

    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        show_result()

def show_result():
    clear_container()
    mbti_type = ("I" if scores["I"] > scores["E"] else "E") + \
                ("S" if scores["S"] > scores["N"] else "N") + \
                ("T" if scores["T"] > scores["F"] else "F") + \
                ("J" if scores["J"] > scores["P"] else "P")

    tk.Label(container, text=f"{selected_name}, you are {mbti_type}!", font=("Times New Roman", 22, "italic"), fg="#4a2e1e", bg='white').pack(pady=20)

    # Optionally add pie chart or career tips
    result_box = tk.Label(container, text=f"This means you tend to be more {mbti_type} in how you perceive and interact with the world.",
                          wraplength=700, font=("Times New Roman", 14), bg='white', justify='center')
    result_box.pack(pady=20)

    tk.Button(container, text="Retake Quiz", command=restart, font=("Times New Roman", 14), bg="#d4bfa3").pack(pady=10)


def clear_container():
    for widget in container.winfo_children():
        widget.destroy()

def restart():
    global current_question, scores
    current_question = 0
    for k in scores:
        scores[k] = 0
    name_var.set("")
    start_screen()

# Launch the app
start_screen()
root.mainloop()
