dict = {"apple": "20", "mango": "30", "banana": "10", "grapes":"15", "orange":"12"}
product = input("What do you wanna buy?")
if(product in dict):
    print(dict.get(product))
else:
    print("Item not found.")