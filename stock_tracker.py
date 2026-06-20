stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

cash_balance = 10000
portfolio = {}

def show_stocks():
    print("\n📈 Available Stocks")
    print("-" * 30)
    for stock, price in stocks.items():
        print(f"{stock} : ${price}")

def buy_stock():
    global cash_balance

    show_stocks()

    stock = input("\nEnter Stock Symbol: ").upper()

    if stock not in stocks:
        print("❌ Invalid Stock")
        return

    qty = int(input("Enter Quantity: "))

    total_cost = stocks[stock] * qty

    if total_cost > cash_balance:
        print("❌ Insufficient Balance")
        return

    cash_balance -= total_cost

    if stock in portfolio:
        portfolio[stock]["qty"] += qty
    else:
        portfolio[stock] = {
            "qty": qty,
            "buy_price": stocks[stock]
        }

    print(f"✅ Purchased {qty} shares of {stock}")
    print(f"💰 Remaining Balance: ${cash_balance}")

def sell_stock():
    global cash_balance

    if not portfolio:
        print("❌ No Stocks in Portfolio")
        return

    stock = input("Enter Stock Symbol to Sell: ").upper()

    if stock not in portfolio:
        print("❌ Stock Not Found")
        return

    qty = int(input("Enter Quantity to Sell: "))

    if qty > portfolio[stock]["qty"]:
        print("❌ Not Enough Shares")
        return

    amount = qty * stocks[stock]

    cash_balance += amount
    portfolio[stock]["qty"] -= qty

    if portfolio[stock]["qty"] == 0:
        del portfolio[stock]

    print(f"✅ Sold {qty} shares of {stock}")
    print(f"💰 Current Balance: ${cash_balance}")

def view_portfolio():

    print("\n📊 PORTFOLIO DASHBOARD")
    print("-" * 60)

    total_value = 0

    if not portfolio:
        print("No Stocks Purchased Yet")
        return

    print("Stock\tQty\tPrice\tValue")

    for stock, details in portfolio.items():

        qty = details["qty"]
        price = stocks[stock]

        value = qty * price

        total_value += value

        print(f"{stock}\t{qty}\t${price}\t${value}")

    print("-" * 60)
    print(f"Portfolio Value : ${total_value}")
    print(f"Cash Balance    : ${cash_balance}")
    print(f"Net Worth       : ${total_value + cash_balance}")

def calculate_profit_loss():

    profit_loss = 0

    for stock, details in portfolio.items():

        qty = details["qty"]

        buy_price = details["buy_price"]

        current_price = stocks[stock]

        profit_loss += (current_price - buy_price) * qty

    print(f"\n📈 Total Profit/Loss : ${profit_loss}")

def save_report():

    file = open("portfolio_report.txt", "w")

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 50 + "\n\n")

    total_value = 0

    for stock, details in portfolio.items():

        qty = details["qty"]

        price = stocks[stock]

        value = qty * price

        total_value += value

        file.write(
            f"{stock} | Qty: {qty} | Price: ${price} | Value: ${value}\n"
        )

    file.write("\n")
    file.write(f"Portfolio Value : ${total_value}\n")
    file.write(f"Cash Balance    : ${cash_balance}\n")
    file.write(f"Net Worth       : ${total_value + cash_balance}\n")

    file.close()

    print("✅ Report Saved as portfolio_report.txt")

while True:

    print("\n")
    print("=" * 50)
    print("💹 VIRTUAL STOCK TRADING SIMULATOR")
    print("=" * 50)
    print("1. View Available Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. View Profit/Loss")
    print("6. Save Report")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        show_stocks()

    elif choice == "2":
        buy_stock()

    elif choice == "3":
        sell_stock()

    elif choice == "4":
        view_portfolio()

    elif choice == "5":
        calculate_profit_loss()

    elif choice == "6":
        save_report()

    elif choice == "7":
        print("👋 Thank You For Using Stock Tracker")
        break

    else:
        print("❌ Invalid Choice")