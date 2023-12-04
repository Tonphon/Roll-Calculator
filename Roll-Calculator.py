import tkinter as tk
from tkinter import Label, Entry, Button, OptionMenu, StringVar

def CalPercentFromRoll(n):
    if n < 10: return 0
    x = 50/3 #ได้ตรงเรทตัวที่อยากได้
    y = 100/3 #ได้ตตรงเรทตัวที่ไม่อยากได้
    z = 50 #หลุดเรท
    for i in range(int(n/10) - 1):
        x,y,z = x + (y/6) + (z/3),(y/3) + (2*z/3),y/2
    return x

def CalRollFromPercent(n):
    if n >= 100:
        return "Percentages cannot be higher than 100. Please enter a valid input."
    i = 0
    while n > CalPercentFromRoll(i):
        i += 10
        if i >= 1230: break
    return i

def CalPercentFromRollO1(n):
    from math import sqrt
    return ((650 - 200*sqrt(13))/13) * (1 - ((1-sqrt(13))/6)**int(n/10)) + ((650 + 200*sqrt(13))/13) * (1 - ((1+sqrt(13))/6)**int(n/10))

def calculate_result():
    try:
        user_input = float(entry.get())
        selected_method = method_var.get()

        if selected_method == "Calculate Percentage from Total Roll":
            result = CalPercentFromRollO1(user_input)
        elif selected_method == "Calculate Total Roll Needed to Get Percentage":
            result = CalRollFromPercent(user_input)
        else:
            result = "Invalid method selected."

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Main Window
window = tk.Tk()
window.title("Roll Calculator")
window.geometry("800x500")

description_label = Label(window, text="Roll Calculator: This program helps you calculate the chances of getting a specific character")
description_label.pack(pady=10)

label = Label(window, text="Enter the Number of Rolls/Required-Percentage:")
label.pack(pady=10)

entry = Entry(window)
entry.pack(pady=10)

calculate_button = Button(window, text="Calculate", command=calculate_result)
calculate_button.pack(pady=10)

instruction_label = Label(window, text="Instructions:")
instruction_label.pack(pady=5)

instruction_description_label = Label(window, text="Enter the number of rolls and click 'Calculate' to see the result. The methods below will help you choose the right calculation.")
instruction_description_label.pack(pady=10)

method_var = StringVar(window)
method_menu = OptionMenu(window, method_var, "Calculate Percentage from Total Roll", "Calculate Total Roll Needed to Get Percentage")
method_menu.pack(pady=10)

description_label = Label(window, text="Methods:")
description_label.pack(pady=5)

method_description_label = Label(window, text="1. Calculate Percentage from Total Roll:\n   Computes the percentage based on the total number of rolls.")
method_description_label.pack(pady=2)

method_description_label = Label(window, text="2. Calculate Total Roll Needed to Get Percentage:\n   Determines the total rolls required to achieve a specific percentage.")
method_description_label.pack(pady=10)

result_label = Label(window, text="", font=("Arial", 16)) 
result_label.pack(pady=10)

window.mainloop()
