from tkinter import *
from tkinter import messagebox

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Define color scheme for dark theme
background_color = "#2E2E2E"
foreground_color = "#FFFFFF"

# Set the background color of the main window
root.configure(bg=background_color)

# Create StringVar instances for principal, rate, months, and days
principal_var = StringVar()
rate_var = StringVar()
months_var = StringVar()
days_var = StringVar()
year_var = StringVar

def validate_positive_number(value):
    """Check if the value is a positive number."""
    try:
        float_value = float(value)
        return float_value > 0
    except ValueError:
        return False

def calculate_compound_interest(principal, rate, n, t):
    # Convert rate to decimal
    rate = float(rate) / 100
    # Apply the compound interest formula
    amount = principal * (1 + rate / n) ** (n * t)
    return amount

def show():
    selected_option = clicked.get()
    
    if selected_option == "months":
        if not validate_positive_number(principal_var.get()) or not validate_positive_number(rate_var.get()) or not months_var.get().isdigit():
            messagebox.showerror("Input Error", "Please enter valid positive numbers for all fields.")
            return
        
        principal = float(principal_var.get())
        rate = float(rate_var.get())
        months = int(months_var.get())
        # Convert months to years
        t = months / 12
        # Compounded monthly
        amount = calculate_compound_interest(principal, rate, 12, t)
        label.config(text=f"Amount after {months} months: {amount:.2f}")
        
    elif selected_option == "days":
        if not validate_positive_number(principal_var.get()) or not validate_positive_number(rate_var.get()) or not days_var.get().isdigit():
            messagebox.showerror("Input Error", "Please enter valid positive numbers for all fields.")
            return
        
        principal = float(principal_var.get())
        rate = float(rate_var.get())
        days = int(days_var.get())
        # Convert days to years
        t = days / 365
        # Compounded daily
        amount = calculate_compound_interest(principal, rate, 365, t)
        label.config(text=f"Amount after {days} days: {amount:.2f}")
        
    else:
        label.config(text="Please select an option.")

def clear():
    """Clear all input fields and selections."""
    principal_var.set("")
    rate_var.set("")
    months_var.set("")
    days_var.set("")
    clicked.set("None")
    label.config(text=" ")
    months_entry.pack_forget()
    months_label.pack_forget()
    days_entry.pack_forget()
    days_label.pack_forget()

# Create Labels and Entry widgets with dark theme
principal_label = Label(root, text='Principal Amount', font=('cursive', 10, 'bold'), bg=background_color, fg=foreground_color)
principal_label.pack()
principal_entry = Entry(root, textvariable=principal_var, font=('cursive', 10, 'normal'), bg='#3D3D3D', fg=foreground_color)
principal_entry.pack()

rate_label = Label(root, text='Annual Interest Rate (%)', font=('cursive', 10, 'bold'), bg=background_color, fg=foreground_color)
rate_label.pack()
rate_entry = Entry(root, textvariable=rate_var, font=('cursive', 10, 'normal'), bg='#3D3D3D', fg=foreground_color)
rate_entry.pack()

months_label = Label(root, text='Months', font=('cursive', 10, 'bold'), bg=background_color, fg=foreground_color)
months_entry = Entry(root, textvariable=months_var, font=('cursive', 10, 'normal'), bg='#3D3D3D', fg=foreground_color)

days_label = Label(root, text='Days', font=('cursive', 10, 'bold'), bg=background_color, fg=foreground_color)
days_entry = Entry(root, textvariable=days_var, font=('cursive', 10, 'normal'), bg='#3D3D3D', fg=foreground_color)

# Dropdown menu options
options = [
    "None",
    "months",
    "days",
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("None")

# Create Dropdown menu with dark theme
drop = OptionMenu(root, clicked, *options)
drop.config(bg='#3D3D3D', fg=foreground_color, font=('cursive', 10))
drop.pack()

# Create button to calculate compound interest
button = Button(root, text="Calculate", command=show, font=('cursive', 10), bg='#4B4B4B', fg=foreground_color)
button.pack()

# Create button to clear all fields
clear_button = Button(root, text="Clear", command=clear, font=('cursive', 10), bg='#4B4B4B', fg=foreground_color)
clear_button.pack()

# Create Label to display results
label = Label(root, text=" ", font=('cursive', 12), bg=background_color, fg=foreground_color)
label.pack()

# Initially hide the entry fields for months and days
months_entry.pack_forget()
months_label.pack_forget()
days_entry.pack_forget()
days_label.pack_forget()

# Show/hide fields based on selection
def update_fields(*args):
    selected_option = clicked.get()
    if selected_option == "months":
        months_entry.pack()
        months_label.pack()
        days_entry.pack_forget()
        days_label.pack_forget()
    elif selected_option == "days":
        days_entry.pack()
        days_label.pack()
        months_entry.pack_forget()
        months_label.pack_forget()
    else:
        months_entry.pack_forget()
        months_label.pack_forget()
        days_entry.pack_forget()
        days_label.pack_forget()

# Bind the dropdown menu change to update fields
clicked.trace("w", update_fields)

# Execute tkinter
root.mainloop()
