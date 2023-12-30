import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("800x600")

# Create the display frame
display_frame = tk.Frame(window)
display_frame.pack(fill="both", expand=True)

# Create the display label
display_label = tk.Label(display_frame, text="0")
display_label.pack(fill="both", expand=True)

# Create the button frame
button_frame = tk.Frame(window)
button_frame.pack(fill="both", expand=True)

# Create the buttons
buttons = [
    tk.Button(button_frame, text="1"),
    tk.Button(button_frame, text="2"),
    tk.Button(button_frame, text="3"),
    tk.Button(button_frame, text="+"),
    tk.Button(button_frame, text="4"),
    tk.Button(button_frame, text="5"),
    tk.Button(button_frame, text="6"),
    tk.Button(button_frame, text="-"),
    tk.Button(button_frame, text="7"),
    tk.Button(button_frame, text="8"),
    tk.Button(button_frame, text="9"),
    tk.Button(button_frame, text="*"),
    tk.Button(button_frame, text="0"),
    tk.Button(button_frame, text="."),
    tk.Button(button_frame, text="/"),
    tk.Button(button_frame, text="=")
]

for button in buttons:
    button.pack(fill="both", expand=True)

# Create the event handlers
def button_click(event):
    button = event.widget
    text = button["text"]

    if text == "=":
        result = eval(display_label["text"])
        display_label["text"] = str(result)
    else:
        display_label["text"] += text

for button in buttons:
    button.bind("<Button-1>", button_click)

# Create the copyright label
copyright_label = tk.Label(window, text="[C] FlamesCo 20XX Build time 12.29.20XX 5:18 PM PST")
copyright_label.pack(side="bottom")

# Start the main loop
window.mainloop()
