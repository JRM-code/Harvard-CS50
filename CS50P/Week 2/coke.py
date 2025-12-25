# --- LIST OF COINS AND AMOUNT INITIALISATION --- #
coin_list = [5, 10, 25, 50]
amount_paid = 0
amount_due = 50

# --- GET COIN FROM USER AND CHECK THE TOTAL AMOUNT PAID --- #
while amount_paid < 50:
    coin = int(input("Insert a coin: "))
    if coin in coin_list:
        amount_paid += coin
    print("Amount Due:", amount_due - amount_paid)
else:
    print("Change Owed:", amount_paid - amount_due)

