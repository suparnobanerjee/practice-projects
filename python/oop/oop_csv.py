class Item:
    all=[]
    def __init__(self,name=str,price=float,quantity=int):
        assert price>=0, f"Price {price} is not greater than or equal to 0!"
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to 0!"
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    def total_amt(self):
        total=self.price*self.quantity
        return total-(total*(Item.discount/100))
    
item=Item("A",20,1)
item=Item("B",33,4)
item=Item("C",4,25)
item=Item("D",150,10)
item=Item("E",999,1)

for instance in item.all:
    print(instance.name)