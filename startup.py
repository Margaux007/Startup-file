import tkinter as tk
import subprocess
import os
import signal

# Store process references (if needed in future)
processes = {}

# Function to run app.py in virtual environment
def run_app():
    print("Running app.py in virtual environment...")
    subprocess.Popen([
        "lxterminal", "-e",
        "bash -c 'source /home/team10/rebarvista/bin/activate && python3 /home/team10/RebarWeb/app.py; exec bash'"
    ])

# Function to run master.py in virtual environment
def run_master():
    print("Running master.py in virtual environment...")
    subprocess.Popen([
        "lxterminal", "-e",
        "bash -c 'source /home/team10/rebarvista/bin/activate && python3 /home/team10/RebarWeb/master.py; exec bash'"
    ])

# Opens a plain terminal
def open_terminal():
    print("Opening terminal...")
    subprocess.Popen(["lxterminal"])

# Exit button to close the GUI
def quit_app():
    print("Exiting GUI.")
    root.destroy()

# --- GUI Layout ---
root = tk.Tk()
root.title("Boot Menu")
root.geometry("400x350")

tk.Label(root, text="Choose an action:", font=("Arial", 18)).pack(pady=20)

button_font = ("Arial", 14)
button_width = 20
button_height = 2

tk.Button(root, text="Run app.py", font=button_font, width=button_width, height=button_height, command=run_app).pack(pady=5)
tk.Button(root, text="Run master.py", font=button_font, width=button_width, height=button_height, command=run_master).pack(pady=5)
tk.Button(root, text="Open Terminal", font=button_font, width=button_width, height=button_height, command=open_terminal).pack(pady=5)
tk.Button(root, text="Exit", font=button_font, width=button_width, height=button_height, command=quit_app).pack(pady=10)

root.mainloop()
