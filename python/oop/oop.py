class Item:
    all=[]
    def __init__(self,name,price,quantity):
        assert price>=0, f"Price {price} is not greater than or equal to 0!"
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to 0!"
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    def total_amt(self):
        total=self.price*self.quantity
        return total-(total*(Item.discount/100))
    
try:
    item_no=int(input("How many item(s) you would like to purchase ? "))
    Item.discount=float(input("Enter the discount percentage : "))
    net_total=0
    for i in range(1,item_no+1):
        item_name=input(f"Enter name of item[{i}] : ")
        item_price=int(input(f"Enter price of each {item_name}: "))
        item_quantity=int(input(f"Enter total quantity of {item_name}: "))
        item=Item(item_name,item_price,item_quantity)
        total=item.total_amt()
        print(f"Total amount to be paid for {item_name} : {total}")
        net_total+=total
    print(f"\nNet total for all items = {net_total:.2f}")
    # for instance in Item.all:
    #     print(instance.name)
except:
    print("Please enter a valid input!")

