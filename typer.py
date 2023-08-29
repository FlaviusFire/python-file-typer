import time
import keyboard
import tkinter as tk
from tkinter import filedialog

def type_with_delay(lines, delay):
    for i in range(delay, 0, -1):
        print(f"Starting typing in {i} seconds...")
        time.sleep(1)
    
    print("Starting typing now...")
    for line in lines:
        keyboard.write(line.strip())  # Strip newline character
        keyboard.press_and_release('enter')
        time.sleep(0.05)  # Small delay between lines

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.askopenfilename(title="Select Input File")
    if not file_path:
        print("No file selected.")
        return
    
    delay = int(input("Enter the delay time (in seconds): "))
    
    try:
        with open(file_path, 'r') as file:
            file_contents = file.readlines()
            type_with_delay(file_contents, delay)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
