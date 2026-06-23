import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = tk.Tk()

root.title("🎬 Netflix Style Telugu Movie Recommender")
root.geometry("1400x850")
root.configure(bg="#141414")

# Heading
heading = tk.Label(
    root,
    text="🎬 Telugu Movie Recommendation System",
    font=("Segoe UI", 24, "bold"),
    bg="#141414",
    fg="#E50914"
)

heading.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Netflix Style Movie Recommender",
    font=("Segoe UI", 12),
    bg="#141414",
    fg="white"
)

subtitle.pack()

genre_label = tk.Label(
    root,
    text="Select Genre",
    font=("Segoe UI", 14, "bold"),
    bg="#141414",
    fg="white"
)

genre_label.pack(pady=10)

genre_dropdown = ttk.Combobox(
    root,
    values=[
        "Action",
        "Comedy",
        "Romance",
        "Family",
        "Thriller",
        "Sci-Fi"
    ],
    width=25,
    state="readonly"
)

genre_dropdown.pack(pady=10)
genre_dropdown.current(0)

# Main Area
cards_frame = tk.Frame(
    root,
    bg="#141414"
)

cards_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)



movie_data = {

    "Action": [
        ("RRR", "8.0", "Epic action drama.", "posters/rrr.jpg"),
        ("Pushpa", "7.6", "Red sandalwood smuggler.", "posters/pushpa.jpg"),
        ("Salaar", "6.7", "Gangster action drama.", "posters/salaar.jpg"),
        ("Akhanda", "6.8", "Mass action entertainer.", "posters/akhanda.jpg")
    ],

    "Comedy": [
        ("Jathi Ratnalu", "7.3", "Comedy of three friends.", "posters/jathi ratnalu.jpg"),
        ("MAD", "7.4", "College comedy entertainer.", "posters/mad.jpg"),
        ("F2", "6.8", "Family comedy drama.", "posters/f2.jpg"),
        ("F3", "5.8", "Sequel to F2.", "posters/f3.jpg")
    ],

    "Romance": [
        ("Sita Ramam", "8.5", "Beautiful love story.", "posters/sita ramam.jpg"),
        ("Hi Nanna", "8.2", "Emotional family drama.", "posters/hi nanna.jpg"),
        ("Majili", "7.8", "Romantic sports drama.", "posters/majili.jpg"),
        ("Tholi Prema", "7.6", "Modern love story.", "posters/tholi prema.jpg")
    ],

    "Family": [
        ("SVSC", "7.5", "Story of two brothers.", "posters/svsc.jpg"),
        ("F2", "6.8", "Family entertainer.", "posters/f2.jpg"),
        ("Shatamanam Bhavati", "7.2", "Family values drama.", "posters/shatamanam bhavati.jpg"),
        ("Sankrathiki Vasthunnam", "8.0", "Festival family movie.", "posters/sankrathiki vasthunnam.jpg")
    ],

    "Thriller": [
        ("HIT", "7.7", "Crime investigation thriller.", "posters/hit.jpg"),
        ("HIT 2", "7.2", "Murder mystery thriller.", "posters/hit 2.jpg"),
        ("Agent Sai", "8.3", "Detective thriller.", "posters/agent sai srinivas athreya.jpg"),
        ("Kshanam", "8.2", "Suspense thriller.", "posters/kshanam.jpg")
    ],

    "Sci-Fi": [
        ("Kalki 2898 AD", "8.0", "Futuristic sci-fi epic.", "posters/kalki 2898 ad.jpg"),
        ("Aditya 369", "8.4", "Time travel classic.", "posters/aditya 369.jpg"),
        ("24", "7.8", "Science fiction thriller.", "posters/24.jpg"),
        ("Kalki 2", "Upcoming", "Sci-fi adventure.", "posters/kalki 2.jpg")
    ]
}


def clear_cards():

    for widget in cards_frame.winfo_children():
        widget.destroy()


def recommend_movies():

    clear_cards()

    genre = genre_dropdown.get()

    if genre not in movie_data:
        return

    movies = movie_data[genre]

    for movie, rating, desc, poster_path in movies:

        card = tk.Frame(
            cards_frame,
            bg="#1F1F1F",
            bd=2,
            relief="ridge"
        )

        card.pack(
            side="left",
            padx=15,
            pady=15,
            fill="y"
        )

        try:

            img = Image.open(poster_path)
            img = img.resize((180, 250))

            photo = ImageTk.PhotoImage(img)

            poster = tk.Label(
                card,
                image=photo,
                bg="#1F1F1F"
            )

            poster.image = photo
            poster.pack(pady=10)

        except Exception as e:

            poster = tk.Label(
                card,
                text="Poster Not Found",
                bg="#1F1F1F",
                fg="white"
            )

            poster.pack(pady=10)

        title = tk.Label(
            card,
            text=movie,
            font=("Segoe UI", 12, "bold"),
            bg="#1F1F1F",
            fg="white"
        )

        title.pack()

        rating_label = tk.Label(
            card,
            text=f"⭐ {rating}",
            bg="#1F1F1F",
            fg="#FFD700"
        )

        rating_label.pack()

        desc_label = tk.Label(
            card,
            text=desc,
            wraplength=180,
            justify="center",
            bg="#1F1F1F",
            fg="white"
        )

        desc_label.pack(pady=10)
recommend_button = tk.Button(
    root,
    text="🎬 Recommend Movies",
    font=("Segoe UI", 12, "bold"),
    bg="#E50914",
    fg="white",
    padx=15,
    pady=8,
    command=recommend_movies
)

recommend_button.pack(pady=15)

footer = tk.Label(
    root,
    text="Developed by Anooha | CodSoft AI Internship",
    bg="#141414",
    fg="gray",
    font=("Segoe UI", 10)
)
footer.pack(side="bottom", pady=10)


root.mainloop()