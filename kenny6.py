coke_price=50
accepted_coin=[25,10,5]
amount_inserted=0
while amount_inserted<coke_price :
    print(f"your insert amount{amount_inserted}")
    coin=int(input("enter the coin:"))
    if coin in accepted_coin:
        amount_inserted+=coin
    else:
        print("please enter the acceptable coin")
change=amount_inserted-coke_price
if change>0:
    print(f"you change {change}")
else:
    print("no change mr")