import random
import tkinter as tk
from tkinter import messagebox

# Parameters
STARTING_BALANCE = 3500
STOCK_NAMES = ["AAPL", "GOOGL", "TSLA", "MSFT", "AMZN", "FB", "NFLX", "NVDA", "INTC", "IBM"]
INITIAL_STOCK_PRICES = [150, 2800, 700, 300, 3300, 250, 500, 600, 55, 120]

# State
balance = STARTING_BALANCE
portfolio = {}

# Functions
def get_stock_price(stock):
    return INITIAL_STOCK_PRICES[STOCK_NAMES.index(stock)] * (1 + random.uniform(-0.05, 0.05))

def buy_stock():
    global balance
    stock = stock_name_var.get()
    amount = amount_var.get()
    price = get_stock_price(stock)
    if price * amount > balance:
        messagebox.showerror("Error", "Insufficient funds")
        return
    balance -= price * amount
    portfolio[stock] = portfolio.get(stock, 0) + amount
    update_ui()

def sell_stock():
    global balance
    stock = stock_name_var.get()
    amount = amount_var.get()
    if stock not in portfolio or portfolio[stock] < amount:
        messagebox.showerror("Error", "Not enough stock to sell")
        return
    price = get_stock_price(stock)
    balance += price * amount
    portfolio[stock] -= amount
    if portfolio[stock] == 0:
        del portfolio[stock]
    update_ui()

def update_ui():
    balance_label.config(text=f"Balance: ${balance:.2f}")
    portfolio_label.config(text=f"Portfolio: {portfolio}")
    stock_prices_text = "\n".join([f"{stock}: ${get_stock_price(stock):.2f}" for stock in STOCK_NAMES])
    stock_prices_label.config(text=f"Stock Prices:\n{stock_prices_text}")

# GUI
root = tk.Tk()
root.title("Stock Trading Game")

# Variables
stock_name_var = tk.StringVar(root)
stock_name_var.set(STOCK_NAMES[0])
amount_var = tk.IntVar(root)
amount_var.set(1)

# Labels
balance_label = tk.Label(root, text=f"Balance: ${balance:.2f}")
balance_label.pack(pady=10)

portfolio_label = tk.Label(root, text=f"Portfolio: {portfolio}")
portfolio_label.pack(pady=10)

stock_prices_label = tk.Label(root, text="")
stock_prices_label.pack(pady=10)

stock_name_label = tk.Label(root, text="Stock Name:")
stock_name_label.pack()

# Dropdown menu for stock selection
stock_name_menu = tk.OptionMenu(root, stock_name_var, *STOCK_NAMES)
stock_name_menu.pack()

# Amount input
amount_label = tk.Label(root, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(root, textvariable=amount_var)
amount_entry.pack()

# Buy Button
buy_button = tk.Button(root, text="Buy", command=buy_stock)
buy_button.pack(pady=5)

# Sell Button
sell_button = tk.Button(root, text="Sell", command=sell_stock)
sell_button.pack(pady=5)

# Initial UI update
update_ui()

# Run the main loop
root.mainloop()
