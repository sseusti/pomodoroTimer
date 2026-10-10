"""Tkinter user interface and timer logic for Pomodoro."""

import os
import sys
import tkinter as tk


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def resource_path(filename):
    """Return a resource path for both source runs and PyInstaller builds."""
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "assets", filename)


class PomodoroApp:
    def __init__(self, window):
        self.window = window
        self.reps = 0
        self.timer = None
        self.tomato_img = tk.PhotoImage(file=resource_path("tomato.png"))
        self._build_ui()

    def _build_ui(self):
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.title_label = tk.Label(
            self.window, text="Timer", fg=GREEN, bg=YELLOW,
            font=(FONT_NAME, 50, "bold"),
        )
        self.title_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(
            self.window, width=200, height=224, bg=YELLOW, highlightthickness=0
        )
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(
            100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
        )
        self.canvas.grid(row=1, column=1)

        self.start_button = tk.Button(
            self.window, text="Start", highlightthickness=0, width=8,
            command=self.start_timer,
        )
        self.start_button.grid(row=2, column=0)

        reset_button = tk.Button(
            self.window, text="Reset", highlightthickness=0, width=8,
            command=self.reset_timer,
        )
        reset_button.grid(row=2, column=2)

        self.check_mark = tk.Label(
            self.window, fg=GREEN, bg=YELLOW, font=(16,)
        )
        self.check_mark.grid(row=3, column=1)

    def reset_timer(self):
        if self.timer is not None:
            self.window.after_cancel(self.timer)
            self.timer = None
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer", fg=GREEN)
        self.check_mark.config(text="")
        self.reps = 0
        self.start_button.config(state="normal")

    def start_timer(self):
        if self.timer is not None:
            return

        self.reps += 1
        self.start_button.config(state="disabled")

        if self.reps % 8 == 0:
            self.title_label.config(text="Break", fg=RED)
            duration = LONG_BREAK_MIN * 60
        elif self.reps % 2 == 0:
            self.title_label.config(text="Break", fg=PINK)
            duration = SHORT_BREAK_MIN * 60
        else:
            self.title_label.config(text="Work", fg=GREEN)
            duration = WORK_MIN * 60
        self.count_down(duration)

    def count_down(self, count):
        self.timer = None
        minutes, seconds = divmod(count, 60)
        self.canvas.itemconfig(
            self.timer_text, text=f"{minutes:02}:{seconds:02}"
        )

        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_button.config(state="normal")
            self.check_mark.config(text="✔" * (self.reps // 2))


def main():
    window = tk.Tk()
    PomodoroApp(window)
    window.mainloop()
