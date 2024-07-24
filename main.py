import tkinter as tk
from database import create_table
from ui import add_expense_ui, view_expenses_ui, view_summary_ui

def main():
    create_table()

    window = tk.Tk()
    window.title("Expense Tracker")

    tk.Button(window, text='Add Expense', command=add_expense_ui).pack(pady=10)
    tk.Button(window, text='View Expenses', command=view_expenses_ui).pack(pady=10)
    tk.Button(window, text='View Summary', command=view_summary_ui).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
