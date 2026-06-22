import tkinter as tk
from tkinter import messagebox

# Game Board
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# Check Winner
def check_winner(current_board):

    # Rows
    for row in current_board:
        if row[0] != "" and row[0] == row[1] == row[2]:
            return row[0]

    # Columns
    for col in range(3):
        if (
            current_board[0][col] != ""
            and current_board[0][col] == current_board[1][col] == current_board[2][col]
        ):
            return current_board[0][col]

    # Main Diagonal
    if (
        current_board[0][0] != ""
        and current_board[0][0] == current_board[1][1] == current_board[2][2]
    ):
        return current_board[0][0]

    # Reverse Diagonal
    if (
        current_board[0][2] != ""
        and current_board[0][2] == current_board[1][1] == current_board[2][0]
    ):
        return current_board[0][2]

    return None


# Check Draw
def check_draw(current_board):

    for row in current_board:
        for cell in row:
            if cell == "":
                return False

    return True


# Minimax Algorithm
def minimax(current_board, is_maximizing):

    winner = check_winner(current_board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if check_draw(current_board):
        return 0

    if is_maximizing:

        best_score = -100

        for row in range(3):
            for col in range(3):

                if current_board[row][col] == "":

                    current_board[row][col] = "O"

                    score = minimax(current_board, False)

                    current_board[row][col] = ""

                    best_score = max(score, best_score)

        return best_score

    else:

        best_score = 100

        for row in range(3):
            for col in range(3):

                if current_board[row][col] == "":

                    current_board[row][col] = "X"

                    score = minimax(current_board, True)

                    current_board[row][col] = ""

                    best_score = min(score, best_score)

        return best_score


# Best Move for AI
def best_move():

    best_score = -100
    move = None

    for row in range(3):
        for col in range(3):

            if board[row][col] == "":

                board[row][col] = "O"

                score = minimax(board, False)

                board[row][col] = ""

                if score > best_score:

                    best_score = score
                    move = (row, col)

    return move


# Restart Game
def restart_game():

    for row in range(3):
        for col in range(3):

            board[row][col] = ""
            buttons[row][col]["text"] = ""
            buttons[row][col]["fg"] = "white"


# AI Move
def ai_move():

    move = best_move()

    if move:

        row, col = move

        board[row][col] = "O"
        buttons[row][col]["text"] = "O"
        buttons[row][col]["fg"] = "#FF6B6B"


# Human Move
def button_click(row, col):

    if board[row][col] == "":

        board[row][col] = "X"
        buttons[row][col]["text"] = "X"
        buttons[row][col]["fg"] = "#00FF7F"

        winner = check_winner(board)

        if winner:
            messagebox.showinfo("Game Over", f"{winner} Wins!")
            restart_game()
            return

        if check_draw(board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            restart_game()
            return

        ai_move()

        winner = check_winner(board)

        if winner:
            messagebox.showinfo("Game Over", f"{winner} Wins!")
            restart_game()
            return

        if check_draw(board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            restart_game()


# Main Window
root = tk.Tk()

root.title("🎮 Tic-Tac-Toe AI")
root.geometry("800x700")
root.configure(bg="#1E1E1E")

# Heading
heading = tk.Label(
    root,
    text="🎮 Tic-Tac-Toe AI",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E1E",
    fg="#00BFFF"
)
heading.pack(pady=15)

# Subtitle
subtitle = tk.Label(
    root,
    text="Human (X) vs AI (O) • Minimax Algorithm",
    font=("Segoe UI", 12),
    bg="#1E1E1E",
    fg="white"
)
subtitle.pack()

# Board Frame
board_frame = tk.Frame(root, bg="#1E1E1E")
board_frame.pack(pady=20)

buttons = []

for row in range(3):

    button_row = []

    for col in range(3):

        btn = tk.Button(
            board_frame,
            text="",
            font=("Segoe UI", 28, "bold"),
            width=4,
            height=2,
            bg="#2C3E50",
            fg="white",
            activebackground="#3498DB",
            activeforeground="white",
            relief="raised",
            bd=4,
            command=lambda r=row, c=col: button_click(r, c)
        )

        btn.grid(
            row=row,
            column=col,
            padx=6,
            pady=6
        )

        button_row.append(btn)

    buttons.append(button_row)

# Restart Button
restart_btn = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Segoe UI", 13, "bold"),
    bg="#0078D7",
    fg="white",
    padx=15,
    pady=8,
    command=restart_game
)

restart_btn.pack(pady=15)

# Footer
footer = tk.Label(
    root,
    text="CodSoft AI Internship Project",
    font=("Segoe UI", 10),
    bg="#1E1E1E",
    fg="#AAAAAA"
)

footer.pack(side="bottom", pady=10)

root.mainloop()