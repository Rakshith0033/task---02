import tkinter as tk
from tkinter import messagebox

# Function to calculate result
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select an operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create GUI window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("600x500")
app.configure(bg="#000010")  # Very dark blue

# Title
tk.Label(app, text="Simple Calculator", font=("Arial", 24, "bold"), bg="#000010", fg="white").pack(pady=20)

# First number
tk.Label(app, text="Enter first number:", bg="#000010", fg="white", font=("Arial", 14)).pack()
entry1 = tk.Entry(app, font=("Arial", 16), bg="white", fg="black", width=25)
entry1.pack(pady=5)

# Second number
tk.Label(app, text="Enter second number:", bg="#000010", fg="white", font=("Arial", 14)).pack()
entry2 = tk.Entry(app, font=("Arial", 16), bg="white", fg="black", width=25)
entry2.pack(pady=5)

# Operation selection
tk.Label(app, text="Choose operation:", bg="#000010", fg="white", font=("Arial", 14)).pack(pady=10)
operation_var = tk.StringVar()
operations = ["+", "-", "*", "/"]
for op in operations:
    tk.Radiobutton(app, text=op, variable=operation_var, value=op, font=("Arial", 14), bg="#000010", fg="white", selectcolor="#1a1a1a").pack()

# Calculate button
tk.Button(app, text="Calculate", command=calculate, font=("Arial", 16), bg="#1a1a1a", fg="white", width=20).pack(pady=20)

# Result display
result_label = tk.Label(app, text="Result: ", font=("Arial", 16, "bold"), bg="#000010", fg="white")
result_label.pack(pady=20)

# Run the app
app.mainloop()
