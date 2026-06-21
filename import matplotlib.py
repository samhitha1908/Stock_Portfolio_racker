import matplotlib.pyplot as plt

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350
}

portfolio = {}
total_value = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Invalid stock symbol!")

stock_names = []
stock_values = []

print("\nPortfolio Summary")
print("-" * 30)

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    stock_names.append(stock)
    stock_values.append(value)

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print("-" * 30)
print("Total Investment Value = $", total_value)

choice = input("\nSave to file? (yes/no): ")

if choice.lower() == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-" * 30 + "\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares = ${value}\n")

        file.write(f"\nTotal Investment Value = ${total_value}")

    print("Saved to portfolio.txt")

# Pie Chart
plt.pie(stock_values, labels=stock_names, autopct='%1.1f%%')
plt.title("Stock Portfolio Distribution")
plt.show()