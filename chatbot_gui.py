import tkinter as tk
from tkinter import scrolledtext
import datetime

# Function to process messages
def send_message():

    user_message = user_input.get().lower().strip()

    if user_message == "":
        return

    chat_area.insert(tk.END, f"You: {user_message}\n")

    # Predefined Responses
    if user_message in ["hi", "hello", "hey"]:
        bot_reply = "Hello! How can I help you?"

    elif "how are you" in user_message:
        bot_reply = "I am doing great. Thanks for asking!"

    elif "your name" in user_message:
        bot_reply = "My name is CodSoft AI Chatbot."

    elif "what is ai" in user_message or user_message == "ai":
        bot_reply = "AI stands for Artificial Intelligence."

    elif "machine learning" in user_message:
        bot_reply = "Machine Learning is a subset of AI."

    elif "python" in user_message:
        bot_reply = "Python is a popular programming language."

    elif user_message == "c":
        bot_reply = "C is a procedural programming language."

    elif "java" in user_message:
        bot_reply = "Java is an object-oriented programming language."

    elif "data science" in user_message:
        bot_reply = "Data Science is the process of extracting insights from data."

    elif "college" in user_message:
        bot_reply = "College helps students gain knowledge and skills."

    elif "internship" in user_message:
        bot_reply = "Internships provide practical industry experience."

    elif "good morning" in user_message:
        bot_reply = "Good morning! Have a productive day."

    elif "good afternoon" in user_message:
        bot_reply = "Good afternoon! Hope you're doing well."

    elif "good evening" in user_message:
        bot_reply = "Good evening! How was your day?"

    elif "who created you" in user_message:
        bot_reply = "I was created as part of a CodSoft AI Internship project."

    elif "thank you" in user_message or "thanks" in user_message or "thank u" in user_message:
        bot_reply = "You're welcome!"

    elif "time" in user_message:
        bot_reply = "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in user_message:
        bot_reply = "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")

    elif user_message == "bye":
        bot_reply = "Goodbye! Have a great day."

    else:
        bot_reply = "Sorry, I don't understand that. Please try another question."

    chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n")
    chat_area.see(tk.END)

    user_input.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("CodSoft AI Chatbot")
root.geometry("750x700")
root.configure(bg="#1E1E1E")

# Heading
heading = tk.Label(
    root,
    text="🤖 CodSoft AI Chatbot",
    font=("Segoe UI", 22, "bold"),
    bg="#1E1E1E",
    fg="#00BFFF"
)
heading.pack(pady=15)

# Chat Area with Scrollbar
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=75,
    height=25,
    font=("Segoe UI", 11),
    bg="#252526",
    fg="white",
    insertbackground="white"
)
chat_area.pack(padx=15, pady=10)

# Welcome Message
chat_area.insert(
    tk.END,
    "🤖 Welcome to CodSoft AI Chatbot\n\n"
    "You can ask about:\n"
    "• AI\n"
    "• Machine Learning\n"
    "• Python\n"
    "• Data Science\n"
    "• Internship\n"
    "• Date & Time\n\n"
)

# Input Frame
input_frame = tk.Frame(root, bg="#1E1E1E")
input_frame.pack(pady=10)

# Input Box
user_input = tk.Entry(
    input_frame,
    width=45,
    font=("Segoe UI", 12)
)
user_input.pack(side=tk.LEFT, padx=10)

# Press Enter to Send
user_input.bind("<Return>", lambda event: send_message())

# Send Button
send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=10
)
send_button.pack(side=tk.LEFT)

root.mainloop()