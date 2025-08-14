from tkinter import *
from tkinter import messagebox

# Define quiz data
questions = [
    {
        "question": "You’re more energized by:",
        "options": ["Spending time alone", "Social gatherings", "Deep conversations", "Being in nature"],
        "traits": ["I", "E", "I", "E"]
    },
    {
        "question": "When approaching a new task, you:",
        "options": ["Plan everything ahead", "Go with the flow", "Seek inspiration", "Analyze all outcomes"],
        "traits": ["J", "P", "N", "T"]
    },
    {
        "question": "You trust information that is:",
        "options": ["Tangible and practical", "Theoretical and abstract", "Emotionally resonant", "Logically sound"],
        "traits": ["S", "N", "F", "T"]
    },
    {
        "question": "When resolving conflict, you:",
        "options": ["Seek harmony", "Stick to logic", "Avoid confrontation", "Speak your mind"],
        "traits": ["F", "T", "I", "E"]
    },
    {
        "question": "Your workspace is usually:",
        "options": ["Organized and neat", "Creative chaos", "Functional", "Minimalist"],
        "traits": ["J", "P", "T", "I"]
    },
    {
        "question": "In a group, you tend to:",
        "options": ["Take charge", "Support others", "Observe quietly", "Bring energy"],
        "traits": ["J", "F", "I", "E"]
    },
    {
        "question": "You value advice that is:",
        "options": ["Objective and firm", "Empathetic and supportive", "Insightful and deep", "Simple and practical"],
        "traits": ["T", "F", "N", "S"]
    },
    {
        "question": "Plans for the weekend are:",
        "options": ["Scheduled", "Spontaneous", "Solo adventures", "Social meetups"],
        "traits": ["J", "P", "I", "E"]
    },
    {
        "question": "When making decisions, you prioritize:",
        "options": ["Facts", "Feelings", "Possibilities", "Consistency"],
        "traits": ["T", "F", "N", "J"]
    },
    {
        "question": "You notice:",
        "options": ["The present moment", "Underlying meanings", "People’s emotions", "Patterns"],
        "traits": ["S", "N", "F", "T"]
    },
    {
        "question": "You prefer work that involves:",
        "options": ["Predictable routines", "Unplanned creativity", "Helping others", "Solving problems"],
        "traits": ["J", "P", "F", "T"]
    },
    {
        "question": "When talking, you are:",
        "options": ["Animated", "Reserved", "Reflective", "Quick-witted"],
        "traits": ["E", "I", "N", "T"]
    },
    {
        "question": "In a story, you prefer:",
        "options": ["The message", "The realism", "The suspense", "The emotions"],
        "traits": ["N", "S", "J", "F"]
    },
    {
        "question": "On your birthday, you prefer:",
        "options": ["A big party", "A quiet day", "Unexpected plans", "A heartfelt gesture"],
        "traits": ["E", "I", "P", "F"]
    },
    {
        "question": "Your dream home would be:",
        "options": ["Modern and efficient", "Cozy and warm", "Unique and artistic", "Organized and minimal"],
        "traits": ["T", "F", "N", "J"]
    }
]

# Track answers
answers = []

# Create window
root = Tk()
root.title("MBTI Quiz")
root.geometry("800x600")
root.configure(bg="#f5f0e1")  # beige theme

current_q = 0
user_name = ""

# Score counters
scores = {"I": 0, "E": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

# Main frame
frame = Frame(root, bg="#f5f0e1")
frame.pack(expand=True)

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def show_intro():
    clear_frame()
    title = Label(frame, text="Welcome to the MBTI Quiz", font=("Times", 24, "bold"), bg="#f5f0e1", fg="#7a5230")
    title.pack(pady=20)

    subtitle = Label(frame, text="Enter your name below:", font=("Times", 18, "italic"), bg="#f5f0e1", fg="#7a5230")
    subtitle.pack(pady=10)

    name_entry = Entry(frame, font=("Times", 16), justify="center", bg="#fff9f0")
    name_entry.pack(pady=5)

    def store_name():
        global user_name
        user_name = name_entry.get().strip()
        if user_name:
            show_mbti_intro()
        else:
            messagebox.showerror("Error", "Please enter your name")

    start_btn = Button(frame, text="Continue", command=store_name, font=("Times", 14), bg="#d4b483", fg="white")
    start_btn.pack(pady=20)

def show_mbti_intro():
    clear_frame()
    intro_text = (
        "The MBTI is based on Carl Jung’s theory of psychological types. It categorizes people into 16 types "
        "based on preferences in four areas: Extraversion/Introversion, Sensing/Intuition, "
        "Thinking/Feeling, and Judging/Perceiving.\n\n"
        "The MBTI emphasizes how our preferences shape our perceptions, decisions, and behaviors. "
        "Understanding your type can help in personal growth, career alignment, and better relationships."
    )

    title = Label(frame, text=f"Hello, {user_name}!", font=("Times", 20, "bold"), bg="#f5f0e1", fg="#7a5230")
    title.pack(pady=10)

    intro_label = Label(frame, text=intro_text, wraplength=700, font=("Times", 14), bg="#f5f0e1", justify="center")
    intro_label.pack(pady=20)

    Button(frame, text="Start Quiz", command=show_question, font=("Times", 14), bg="#7a5230", fg="white").pack(pady=20)

def show_question():
    clear_frame()
    global current_q

    if current_q >= len(questions):
        show_result()
        return

    q_data = questions[current_q]

    q_label = Label(frame, text=q_data["question"], font=("Times", 18, "italic"), wraplength=700,
                    bg="#f5f0e1", fg="#7a5230", justify="center")
    q_label.pack(pady=30)

    for i, option in enumerate(q_data["options"]):
        def select(opt=i):
            scores[q_data["traits"][opt]] += 1
            next_question()
        Button(frame, text=option, command=select, font=("Times", 14), width=30,
               bg="#fff5e6", fg="#4e342e", relief="groove").pack(pady=8)

def next_question():
    global current_q
    current_q += 1
    show_question()

def show_result():
    clear_frame()

    result_text = f"{user_name}, here’s your MBTI tendency overview:\n\n"

    pairs = [("I", "E"), ("S", "N"), ("T", "F"), ("J", "P")]
    mbti_type = ""

    for a, b in pairs:
        total = scores[a] + scores[b]
        if total == 0:
            continue
        percent_a = (scores[a] / total) * 100
        percent_b = (scores[b] / total) * 100
        result_text += f"{a}/{b}: {percent_a:.1f}% / {percent_b:.1f}%\n"
        mbti_type += a if percent_a > percent_b else b

    Label(frame, text="Your MBTI Result", font=("Times", 22, "bold"), bg="#f5f0e1", fg="#7a5230").pack(pady=20)
    Label(frame, text=result_text, font=("Times", 14), bg="#f5f0e1", fg="#4e342e", justify="center").pack(pady=10)

    Label(frame, text=f"Your most likely type: {mbti_type}", font=("Times", 16, "bold italic"),
          bg="#f5f0e1", fg="#7a5230").pack(pady=20)

    Button(frame, text="Retake Quiz", command=restart_quiz, font=("Times", 12),
           bg="#d4b483", fg="white").pack(pady=10)

def restart_quiz():
    global current_q, scores, user_name
    current_q = 0
    scores = {k: 0 for k in scores}
    user_name = ""
    show_intro()

show_intro()
root.mainloop()

