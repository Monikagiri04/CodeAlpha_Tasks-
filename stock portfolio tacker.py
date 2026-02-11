# stock_portfolio_tracker.py
#simple stock portfolio tracker

# Hardcoded stock prices
prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2500,
    "HDFCBANK": 1600,
    "ITC": 450
}

portfolio = {}
total_value = 0

print("Available stocks:", ",".join(prices.keys()))
print("Type 'done' when you are finished.\n")

# Taking stock inputs from user
while True:
    Stock_name = input("Enter stock name: ").upper()

    if Stock_name == "DONE":
        break

    if Stock_name not in prices:
        print("stock not found. please try again.")
        continue

    quantity = int(input("Enter Quantity: "))

    #Add quantity if stock already exists
    if Stock_name in portfolio:
        portfolio[Stock_name] += quantity
    else:
        portfolio[Stock_name] = quantity

    # calculating total investment
    print("\n---portfolio summary---") 

    for stock, qty in portfolio.items():
        value = prices[stock]*qty
        total_value += value
        print(stock,"-Quantity:",qty,"| value: rs", value)

    print("------------------------")
    print("Total Investment Value: rs", total_value)


#Ask user if they want to save data
choice = input ("\nDo you want to save this data to a file? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt","w") as file :
        file.write("portfolio summary\n")
        file.write("---------------------------\n")

        for stock,qty in portfolio.items():
            value = prices [stock]* qty
            file.write(f"{stock} - Quantity:{qty} | value: rs{value}\n")

        file.write("---------------------------\n")
        file.write(f"Total Investment Value: rs{total_value}\n")

    print("Portfolio saved successfully.")    
