import tkinter as tk
from tkinter import messagebox
from database import add_expense, fetch_expenses
from analysis import analyze_expenses, plot_summary

def add_expense_ui():
    def save_expense():
        amount = float(entry_amount.get())
        description = entry_description.get()
        category = entry_category.get()
        date = entry_date.get()
        add_expense(amount, description, category, date)
        messagebox.showinfo("Success", "Expense added successfully!")

    window = tk.Tk()
    window.title("Add Expense")

    tk.Label(window, text="Amount").grid(row=0)
    tk.Label(window, text="Description").grid(row=1)
    tk.Label(window, text="Category").grid(row=2)
    tk.Label(window, text="Date (YYYY-MM-DD)").grid(row=3)

    entry_amount = tk.Entry(window)
    entry_description = tk.Entry(window)
    entry_category = tk.Entry(window)
    entry_date = tk.Entry(window)

    entry_amount.grid(row=0, column=1)
    entry_description.grid(row=1, column=1)
    entry_category.grid(row=2, column=1)
    entry_date.grid(row=3, column=1)

    tk.Button(window, text='Save', command=save_expense).grid(row=4, column=1, pady=4)
    window.mainloop()

def view_expenses_ui():
    expenses = fetch_expenses()
    window = tk.Tk()
    window.title("View Expenses")

    for i, expense in enumerate(expenses):
        tk.Label(window, text=expense).grid(row=i, column=0)

    window.mainloop()

def view_summary_ui():
    expenses = fetch_expenses()
    summary = analyze_expenses(expenses)
    plot_summary(summary)
