# Day 033
# APIs

import requests
import json
import smtplib
import time
import tkinter as tk
import datetime as dt


def iss_location_on_sky() -> None:
    api_url: str = "http://api.open-notify.org/iss-now.json"
    iss_location: requests.Response = requests.get(url=api_url)

    if not iss_location.raise_for_status():
        with open("./data/iss_location.json", "w") as file:
            json.dump(iss_location.json(), file, indent=4)


def kanye_quotes() -> str:
    api_url2: str = "http://api.kanye.rest"
    kanye: requests.Response = requests.get(api_url2)
    if not kanye.raise_for_status():
        kanye_quote: str = kanye.json()["quote"]
        with open("./data/kanye_quotes.txt", "w") as file:
            file.write(kanye_quote)
        return kanye_quote
    return ""


def kanye_app() -> None:
    def new_canvas() -> None:
        _quote: str = kanye_quotes()
        canvas.itemconfig(quote_text, text=_quote)

    window: tk.Tk = tk.Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50)
    canvas: tk.Canvas = tk.Canvas(width=300, height=414)
    background_img: tk.PhotoImage = tk.PhotoImage(file="./data/kanye_bg.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text: int = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="white")

    new_canvas()

    canvas.grid(row=0, column=0)
    kanye_img: tk.PhotoImage = tk.PhotoImage(file="./data/kanye.png")
    kanye_button: tk.Button = tk.Button(image=kanye_img, highlightthickness=0, command=new_canvas)
    kanye_button.grid(row=1, column=0)
    window.mainloop()


def sun_position_and_time() -> None:
    api_url2: str = "http://api.sunrise-sunset.org/json"
    sun_position = requests.get(api_url2)
    sun_position.raise_for_status()
    print(sun_position.json())

    with open("./data/sun_position.json", "w") as file:
        json.dump(sun_position.json(), file, indent=4)


def send_email_iss_above() -> None:
    MY_LAT: float = 39.399872  # Portugal
    MY_LONG: float = -8.224454

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data: dict = response.json()

    iss_latitude: float = float(data["iss_position"]["latitude"])
    iss_longitude: float = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response1: requests.Response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()
    data1: dict = response1.json()
    sunrise: int = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset: int = int(data1["results"]["sunset"].split("T")[1].split(":")[0])

    time_now: dt.datetime = dt.datetime.now()

    def timer_check() -> None:
        is_close: bool = (MY_LONG + 5 >= iss_longitude >= MY_LONG - 5 and MY_LAT + 5 >= iss_latitude >= MY_LAT - 5)
        is_night: bool = sunrise >= time_now.hour >= sunset

        if is_night and is_close:
            smtp_url: str = "smtp.gmail.com"
            smtp_port: int = 587
            email_from: str = ""
            email_password: str = ""
            email_to: str = ""
            email_msg: str = "testing"

            connection: smtplib.SMTP = smtplib.SMTP(smtp_url, port=smtp_port)
            connection.starttls()
            connection.login(user=email_from, password=email_password)
            connection.sendmail(from_addr=email_from, to_addrs=[email_from, email_to], msg=email_msg)
            print(f"EMAIL SENT ->  {dt.datetime.now()}")

        print(f"timer checking now. not sending email ->  {dt.datetime.now()}")

    timer_check()


# iss_location_on_sky()
# kanye_quotes()
# kanye_app()
# sun_position_and_time()
while True:
    send_email_iss_above()
    time.sleep(60)
