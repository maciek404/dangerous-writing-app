import tkinter as tk
import time
from tkinter import filedialog, ttk

INK = "#1C1B1A"
PANEL = "#242220"
PAPER = "#EDE6D6"
SAGE = "#6B8F71"
EMBER = "#C1502E"
MUTED = "#8A8478"

FONT_WRITE = ("Georgia", 19)
FONT_UI = ("Helvetica Neue", 11)
FONT_UI_BOLD = ("Helvetica Neue", 13, "bold")
FONT_COUNT = ("Helvetica Neue", 18, "bold")

WORD_GLOBAL = 500

last_keypress_time = None
tick_running = False

root = tk.Tk()
root.title("Dangerous Writing App")
root.geometry("1400x1100")
root.configure(bg=INK)


def clear_text():
    text_area.delete("1.0", tk.END)
    word_count_label.config(text="0")
    save_button.config(state="disabled")
    show_placeholder()


def update_word_count():
    user_text = text_area.get("1.0", tk.END)
    total_words = len(user_text.split())
    if total_words >= WORD_GLOBAL:
        save_button.config(state="normal")
    else:
        save_button.config(state="disabled")
    word_count_label.configure(text=total_words)


def reset_timer(event):
    global last_keypress_time, tick_running
    last_keypress_time = time.time()
    update_word_count()
    if not tick_running:
        text_area.delete("1.0", tk.END)
        text_area.config(fg=PAPER)
        tick_running = True
        tick()


def tick():
    global tick_running
    limit = time_limit.get()
    elapsed = time.time() - last_keypress_time
    remaining = max(0, limit - elapsed)
    progress_bar["value"] = (remaining / limit) * 100

    if remaining < 2:
        progress_bar.configure(style="ember.Horizontal.TProgressbar")
    else:
        progress_bar.configure(style="ink.Horizontal.TProgressbar")

    if elapsed >= limit:
        show_lost_message()
        clear_text()
        tick_running = False
        return

    text_area.after(100, tick)


def show_lost_message():
    lost_text_label.config(text="Text lost!")
    root.after(2500, hide_lost_message)


def hide_lost_message():
    lost_text_label.config(text="")


def save_text():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        content = text_area.get("1.0", tk.END)
        with open(file_path, "w") as f:
            f.write(content)

def show_placeholder():
    text_area.config(fg=MUTED)
    text_area.insert("1.0", "Keep writing. Stop for five seconds and it's gone.")
    text_area.mark_set("insert", "1.0")

style = ttk.Style()
style.theme_use("default")

for name, color in (("ink", INK), ("ember", EMBER)):
    style.configure(
        f"{name}.Horizontal.TProgressbar",
        troughcolor=PANEL,
        background=color,
        bordercolor=INK,
        lightcolor=color,
        darkcolor=color,
        thickness=20,
        borderwidth=0,
    )

progress_bar = ttk.Progressbar(
    root, style="ink.Horizontal.TProgressbar", maximum=100
)
progress_bar.pack(fill="x", pady=(0, 0))

container = tk.Frame(root, bg=INK)
container.pack(fill="both", expand=True, padx=70, pady=50)

text_area = tk.Text(
    container,
    font=FONT_WRITE,
    wrap="word",
    bg=INK,
    fg=MUTED,
    insertbackground=EMBER,
    insertwidth=3,
    relief="flat",
    bd=0,
    padx=38,
    pady=35,
    highlightthickness=0,
    spacing1=4,
    spacing3=5,

)
text_area.pack(fill="both", expand=True)
text_area.bind("<Key>", reset_timer)

status_row = tk.Frame(container, bg=INK)
status_row.pack(fill="x", pady=(14, 6))

word_count_label = tk.Label(
    status_row, text="0", font=FONT_COUNT, bg=INK, fg=EMBER
)
word_count_label.pack()

lost_text_label = tk.Label(
    status_row, text="", font=FONT_UI_BOLD, bg=INK, fg=EMBER
)
lost_text_label.pack(side="right")

controls_row = tk.Frame(container, bg=INK)
controls_row.pack(fill="x")

time_limit = tk.IntVar(value=5)
slider_label = tk.Label(
    controls_row, text="Time limit in sec", font=FONT_UI, bg=INK, fg=MUTED
)
slider_label.pack(side="left", pady=(12, 0))

time_slider = tk.Scale(
    controls_row,
    from_=3,
    to=15,
    orient="horizontal",
    variable=time_limit,
    length=180,
    bg=INK,
    fg=PAPER,
    troughcolor=PANEL,
    highlightthickness=0,
    bd=0,
    sliderrelief="flat",
    activebackground=EMBER,
    font=FONT_UI,
)
time_slider.pack(side="left", padx=(10, 0))

save_button = tk.Button(
    controls_row,
    text="Save",
    state="disabled",
    command=save_text,
    font=FONT_UI_BOLD,
    bg=MUTED,
    fg=INK,
    activebackground=EMBER,
    relief="flat",
    padx=18,
    pady=6,
    bd=0,
    disabledforeground=INK,
    cursor="plus",
)
save_button.pack(side="right")

show_placeholder()
text_area.focus_force()

root.mainloop()