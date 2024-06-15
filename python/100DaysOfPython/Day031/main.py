# -------------------------- MODULES ---------------------------- #
import random
import tkinter as tk
import pandas as pd

# -------------------------- VARIABLES ---------------------------- #
BACKGROUND_COLOR: str = "#B1DDC6"
FONT_A: tuple = ("Ariel", 40, "italic")
FONT_B: tuple = ("Ariel", 60, "bold")
FILE_card_front: str = "./images/card_front.png"
FILE_card_back: str = "./images/card_back.png"
FILE_right: str = "./images/right.png"
FILE_wrong: str = "./images/wrong.png"
FILE_data: str = "./data/french_words.csv"
user_score: int = 0


# ------------------------- FUNCTIONS --------------------------- #
def create_canvas_front(_canvas: tk.Canvas, number: int, df: pd.DataFrame) -> None:
    text_a: str = df["French"][number]
    _canvas.create_image(400, 263, image=card_front)
    _canvas.create_text(400, 150, text=text_a, font=FONT_A)


def create_canvas_back(_canvas: tk.Canvas, number: int, df: pd.DataFrame) -> None:
    text_a: str = df["French"][number]
    text_b: str = df["English"][number]
    _canvas.create_image(400, 263, image=card_back)
    _canvas.create_text(400, 150, text=text_a, font=FONT_A)
    _canvas.create_text(400, 263, text=text_b, font=FONT_B)


def bt_right() -> None:
    user_result(1)


def bt_wrong() -> None:
    user_result(0)


def user_result(_score: int) -> None:
    global user_score
    user_score += _score
    if _score:
        create_canvas_full("a")
    else:
        create_canvas_full("b")


def read_csv_file() -> pd.DataFrame:
    with open(FILE_data, "r") as file:
        return pd.read_csv(file)


def to_csv_file() -> None:
    with open(".\\data\\user_scores.txt", "w") as file:
        file.write(f"User Score:  {user_score} points.")


def search_random(df: pd.DataFrame) -> int:
    random_number: int = random.randint(0, len(df) - 1)
    return random_number


def timer() -> None:
    window.after(2000)


def create_canvas_full(_a_or_b: str) -> None:
    canvas: tk.Canvas = tk.Canvas(width=800, height=526)

    df: pd.DataFrame = read_csv_file()
    number: int = search_random(df)

    if "a" in _a_or_b:
        create_canvas_front(canvas, number, df)
    else:
        create_canvas_back(canvas, number, df)

    # timer()
    canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
    canvas.grid(row=0, column=0, columnspan=2)


# -------------------------- MAIN ---------------------------- #
window: tk.Tk = tk.Tk()
window.title("Flash Cards Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front: tk.PhotoImage = tk.PhotoImage(file=FILE_card_front)
card_back: tk.PhotoImage = tk.PhotoImage(file=FILE_card_back)
right_sign: tk.PhotoImage = tk.PhotoImage(file=FILE_right)
wrong_sign: tk.PhotoImage = tk.PhotoImage(file=FILE_wrong)

create_canvas_full("a")

tk.Button(window, image=right_sign, command=bt_right, compound="center", highlightthickness=0,
          bg=BACKGROUND_COLOR).grid(row=1, column=0)
tk.Button(window, image=wrong_sign, command=bt_wrong, compound="center", highlightthickness=0,
          bg=BACKGROUND_COLOR).grid(row=1, column=1)

window.mainloop()

to_csv_file()
