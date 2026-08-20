stockprices={"BR" : 300 , "JS" : 180 , "SC" : 120 , "TN" : 175 , "CT" : 200}
stock = {}
totalinvestment = 0

for i in range(1,6):
    print("Stock: BR , JS , SC , TN , CT ")
    key=input("Enter stock name from the above mentioned : ").strip().upper()

    # Check if stock was already entered
    if key in stock:
        print("This stock has already been entered. Please choose another stock.")
        continue

    value=int(input("Enter it's quantity : ").strip())
    stock[key]=value

    print("stock = ", stock)

    totalprice=stock[key]*stockprices[key]
    totalinvestment+=totalprice

    print("Current investment = ", totalinvestment)

print("Total Investment = ", totalinvestment)