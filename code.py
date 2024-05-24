import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("500x800")
        
        self.master.configure(bg="#d9e6f2") 
        self.question_style = {"font": ("Arial", 10), "wraplength": 350, "bg": "#d9e6f2"}  
        self.entry_style = {"font": ("Arial", 10)}
        self.button_style = {"font": ("Arial", 10), "bg": "#3399ff", "fg": "white"}
        self.score_style = {"font": ("Arial", 10), "bg": "#d9e6f2"}
        
        self.questions = {
            "What is the capital of France?": "Paris",
            "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
            "What is the chemical symbol for water?": "H2O",
            "Which planet is known as the Red Planet?": "Mars",
            "Who painted the Mona Lisa?": "Leonardo da Vinci"
        }
        
        self.question_var = tk.StringVar()
        self.answer_var = tk.StringVar()
        self.score = 0
        
        self.question_label = tk.Label(master, textvariable=self.question_var, **self.question_style)
        self.question_label.pack(pady=20)
        self.next_question()
        
        self.answer_entry = tk.Entry(master, textvariable=self.answer_var, **self.entry_style)
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer, **self.button_style)
        self.submit_button.pack(pady=10)
        
        self.score_label = tk.Label(master, text=f"Score: {self.score}", **self.score_style)
        self.score_label.pack()

    def next_question(self):
        question = random.choice(list(self.questions.keys()))
        self.question_var.set(question)

    def check_answer(self):
        question = self.question_var.get()
        answer = self.answer_var.get()
        correct_answer = self.questions.get(question)
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "You got it right!")
            self.score += 1
        else:
            messagebox.showinfo("Incorrect!", f"Sorry, the correct answer is: {correct_answer}")
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()