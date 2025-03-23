import tkinter as tk
from math import *

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry_var.get().replace("^","**")
            result = eval(expression)
            history.append(f"{expression} = {result}")
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")

    elif text == "C":
        entry_var.set("")
    elif text == "History":
        show_history()
    elif text == "Clear History":
        history.clear()
        show_history()
    elif text in ["sin", "cos", "tan", "log", "sqrt", "exp"]:
        try:
            expression = f"{text}({entry_var.get()})"
            result = eval(expression)
            history.append(f"{expression} = {result}")
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + text)
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("400x300")

    tk.Label(history_window, text="Calcualtion History", font="courier 14 bold").pack(pady=5)
    text_widget = tk.Text(history_window, font="Courier 12", height=10, width=40)
    text_widget.pack(pady=5, padx=10)

    for record in history:
        text_widget.insert(tk.END, record + "\n")
    text_widget.config(state=tk.DISABLED)  
    clear_btn = tk.Button(history_window, text="Clear History", command=lambda: [history.clear(), history_window.destroy()], font="Courier 12", bg="red", fg="white")
    clear_btn.pack(pady=5)
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("600x600")
root.configure(bg="black")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Courier 20 bold", bd=10, relief=tk.SUNKEN, bg="gray", fg="white")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

history= []

buttons = [
    ["7", "8", "9", "+", "-"],
    ["4", "5", "6", "*", "/"],
    ["1", "2", "3", "(", ")"],
    ["C", "0", "=", "^", "mod"],
    ["sin", "cos", "tan", "log", "sqrt"],
    ["exp", "pi", "e", "%", "rad"],
    ["History", "Clear History"]
]

frame = tk.Frame(root, bg="black")
frame.pack()

for row in buttons:
    button_frame = tk.Frame(frame, bg="black")
    button_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    for char in row:
        btn=tk.Button(button_frame, text=char, font="Courier 15 bold", padx=20, pady=20, bg="black", fg="white")
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", on_click)
root.mainloop()