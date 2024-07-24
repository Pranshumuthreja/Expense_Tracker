import matplotlib.pyplot as plt

def analyze_expenses(expenses):
    summary = {}
    for expense in expenses:
        category = expense[3]
        summary[category] = summary.get(category, 0) + expense[1]
    return summary

def plot_summary(summary):
    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='blue')
    plt.xlabel('Categories')
    plt.ylabel('Amount Spent')
    plt.title('Category-wise Expense Summary')
    plt.show()
