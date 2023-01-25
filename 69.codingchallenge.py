def discount(price):
    price = price-(price/100)*10
    return price

price = [100,200,300,400]
new_price = list(map(discount,price))
print(new_price)