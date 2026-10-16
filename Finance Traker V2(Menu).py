
import tkinter as tk
from tkinter import messagebox

# ---------- Theme ----------
BG = "#101114"
PANEL = "#202126"
GREEN = "#B6F09C"
WHITE = "#F5F5F5"
MUTED = "#92949B"
RED = "#F0B59C"

root = tk.Tk()
root.title("Penny | Finance Tracker")
root.geometry("760x540")
root.minsize(650, 480)
root.configure(bg=BG)

income = tk.StringVar()
expenses = tk.StringVar()
goal = tk.StringVar()

def clear():
    for widget in content.winfo_children():
        widget.destroy()

def heading(title, subtitle):
    tk.Label(
        content, text=title, bg=BG, fg=WHITE,
        font=("Segoe UI", 23, "bold")
    ).pack(anchor="w")

    tk.Label(
        content, text=subtitle, bg=BG, fg=MUTED,
        font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(5, 22))

def field(label, variable):
    tk.Label(
        content, text=label, bg=BG, fg=MUTED,
        font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(8, 5))

    tk.Entry(
        content, textvariable=variable,
        bg=PANEL, fg=WHITE, insertbackground=WHITE,
        relief="flat", font=("Segoe UI", 12),
        highlightthickness=1, highlightbackground=PANEL
    ).pack(fill="x", ipady=10)

def button(parent, text, command, primary=False):
    return tk.Button(
        parent, text=text, command=command,
        bg=GREEN if primary else PANEL,
        fg=BG if primary else WHITE,
        activebackground=GREEN,
        activeforeground=BG,
        relief="flat", borderwidth=0,
        font=("Segoe UI", 10, "bold"),
        cursor="hand2", padx=16, pady=11
    )

def show_dashboard():
    clear()
    heading("Your finances", "A clearer view of your money.")

    field("Monthly income", income)
    field("Monthly expenses", expenses)
    field("Monthly savings goal", goal)

    button(
        content, "Calculate balance",
        calculate, primary=True
    ).pack(fill="x", pady=22)

def calculate():
    try:
        earned = float(income.get())
        spent = float(expenses.get())
        target = float(goal.get())

        if min(earned, spent, target) < 0:
            raise ValueError

        balance = earned - spent
        clear()

        heading("Monthly summary", "Here's where you stand.")

        for label, amount in [
            ("Income", earned),
            ("Expenses", spent),
            ("Remaining balance", balance),
            ("Savings goal", target)
        ]:
            card = tk.Frame(content, bg=PANEL)
            card.pack(fill="x", pady=4)

            tk.Label(
                card, text=label, bg=PANEL, fg=MUTED,
                font=("Segoe UI", 10)
            ).pack(side="left", padx=14, pady=13)

            tk.Label(
                card, text=f"${amount:,.2f}",
                bg=PANEL, fg=GREEN if amount >= 0 else RED,
                font=("Segoe UI", 11, "bold")
            ).pack(side="right", padx=14)

        if balance >= target:
            result = "You're on track to meet your savings goal!"
        else:
            result = (
                f"You need ${target - balance:,.2f} more "
                "to reach your goal."
            )

        tk.Label(
            content, text=result, bg=BG, fg=GREEN,
            wraplength=440, justify="left",
            font=("Segoe UI", 11)
        ).pack(anchor="w", pady=15)

        button(
            content, "Back to dashboard",
            show_dashboard
        ).pack(fill="x")

    except ValueError:
        messagebox.showerror(
            "Invalid input",
            "Enter valid, non-negative numbers in all fields."
        )

def show_budget():
    clear()
    heading("Next month's budget", "Plan ahead before you spend.")

    future_income = tk.StringVar()
    future_expenses = tk.StringVar()
    future_goal = tk.StringVar()

    field("Expected income", future_income)
    field("Expected expenses", future_expenses)
    field("Savings goal", future_goal)

    def calculate_future():
        try:
            earned = float(future_income.get())
            spent = float(future_expenses.get())
            target = float(future_goal.get())

            if min(earned, spent, target) < 0:
                raise ValueError

            balance = earned - spent
            messagebox.showinfo(
                "Budget forecast",
                f"Expected balance: ${balance:,.2f}\n\n"
                + (
                    "Savings goal on track!"
                    if balance >= target
                    else f"Goal shortfall: ${target - balance:,.2f}"
                )
            )

            if balance < 0:
                messagebox.showwarning(
                    "Budget warning",
                    "Your expected expenses exceed your income."
                )

        except ValueError:
            messagebox.showerror(
                "Invalid input",
                "Enter valid, non-negative numbers."
            )

    button(
        content, "Calculate forecast",
        calculate_future, primary=True
    ).pack(fill="x", pady=22)

def show_investing():
    clear()
    heading("Investing", "Learn before putting money at risk.")

    tk.Label(
        content,
        text=(
            "Investing involves risk, and returns are not guaranteed.\n\n"
            "Learn about these options:\n\n"
            "01   Stocks — ownership in a company\n\n"
            "02   Bonds — lending to a borrower\n\n"
            "03   Funds — diversified baskets of investments\n\n"
            "Build an emergency savings buffer before investing."
        ),
        bg=BG, fg=WHITE, justify="left",
        font=("Segoe UI", 11), wraplength=450
    ).pack(anchor="w")

# ---------- Layout ----------
sidebar = tk.Frame(root, bg=PANEL, width=190)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(
    sidebar, text="◈  penny", bg=PANEL, fg=GREEN,
    font=("Segoe UI", 20, "bold")
).pack(anchor="w", padx=20, pady=(28, 36))

for text, command in [
    ("Dashboard", show_dashboard),
    ("Monthly budget", show_budget),
    ("Investing", show_investing)
]:
    tk.Button(
        sidebar, text=text, command=command,
        bg=PANEL, fg=WHITE, activebackground=BG,
        activeforeground=GREEN, relief="flat",
        anchor="w", font=("Segoe UI", 10),
        padx=20, pady=13, cursor="hand2"
    ).pack(fill="x")

tk.Label(
    sidebar, text="PERSONAL FINANCE",
    bg=PANEL, fg=MUTED,
    font=("Segoe UI", 8)
).pack(side="bottom", anchor="w", padx=20, pady=22)

content = tk.Frame(root, bg=BG, padx=35, pady=30)
content.pack(side="left", fill="both", expand=True)

show_dashboard()
root.mainloop()
