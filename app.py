import time
import random
import tkinter as tk
from tkinter import messagebox

# Random sentences
SENTENCES = ["The quick brown fox jumps over the lazy dog.","She sells seashells by the seashore.","How much wood would a woodchuck chuck if a woodchuck could chuck wood?","Peter Piper picked a peck of pickled peppers.","I scream, you scream, we all scream for ice cream.","The cat in the hat came back.","Sally sells seashells by the seashore.","An apple a day keeps the doctor away.","Life is like a box of chocolates.","The early bird catches the worm."]

# Functions
def calculate_typing_speed(text, time_taken):
    words = text.split()
    num_words = len(words)
    num_characters = len(text)
    minutes = time_taken / 60
    speed_wpm = num_words / minutes
    speed_cpm = num_characters / minutes
    return speed_wpm, speed_cpm

def start_typing():
    global start_time
    start_time = time.time()
    sentence = random.choice(SENTENCES)
    text_display.config(text=sentence)
    start_button.config(state=tk.DISABLED)
    end_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.DISABLED)
    update_timer()

def stop_typing():
    global start_time
    end_time = time.time()
    time_taken = end_time - start_time
    speed_wpm, speed_cpm = calculate_typing_speed(text_entry.get("1.0", "end-1c"), time_taken)
    messagebox.showinfo("Typing Speed Test", f"Time taken: {time_taken:.2f} seconds\nSpeed: {speed_wpm:.2f} words per minute\nSpeed: {speed_cpm:.2f} characters per minute")
    start_button.config(state=tk.NORMAL)
    end_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.NORMAL)
    timer_label.after_cancel(timer_id)

def reset_typing():
    text_entry.delete("1.0", tk.END)
    timer_label.config(text="Time: 0.00 seconds")
    sentence = random.choice(SENTENCES)
    text_display.config(text=sentence)

def update_timer():
    elapsed_time = time.time() - start_time
    timer_label.config(text=f"Time: {elapsed_time:.2f} seconds")
    global timer_id
    timer_id = timer_label.after(100, update_timer)


# Widget section
root = tk.Tk()
root.title("Typing Speed Test")
root.configure(bg="black")

main_frame = tk.Frame(root, bg="black")
main_frame.pack(padx=20, pady=20)

text_label = tk.Label(main_frame, text="Type the following text as fast as you can:", fg="white", bg="black", font=("Segoe UI", 12))
text_label.pack()

text_display = tk.Label(main_frame, text="", fg="blue", bg="black", font=("Segoe UI", 14, "bold"))
text_display.pack(pady=10)

text_entry = tk.Text(main_frame, width=50, height=5, bg="black", fg="white", insertbackground="white", font=("Segoe UI", 12))
text_entry.pack()

timer_label = tk.Label(main_frame, text="Time: 0.00 seconds", fg="white", bg="black", font=("Segoe UI", 12))
timer_label.pack(pady=10)

start_button = tk.Button(main_frame, text="Start", bg="blue", fg="white", font=("Segoe UI", 12), command=start_typing)
start_button.pack(side=tk.LEFT, padx=5)
start_button.config(highlightbackground="blue")
root.bind("<Control-s>", lambda event: start_button.invoke())  # Shortcut key: Ctrl + s for Start

end_button = tk.Button(main_frame, text="End", bg="blue", fg="white", font=("Segoe UI", 12), command=stop_typing, state=tk.DISABLED)
end_button.pack(side=tk.LEFT, padx=5)
end_button.config(highlightbackground="blue")
root.bind("<Control-e>", lambda event: end_button.invoke())  # Shortcut key: Ctrl + e for End

reset_button = tk.Button(main_frame, text="Reset", bg="blue", fg="white", font=("Segoe UI", 12), command=reset_typing)
reset_button.pack(side=tk.LEFT, padx=5)
reset_button.config(highlightbackground="blue")
root.bind("<Control-r>", lambda event: reset_button.invoke())  # Shortcut key: Ctrl + r for Reset

root.mainloop()