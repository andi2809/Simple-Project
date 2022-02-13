class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def ulang(self, n):
        return n

    def buy(self, req_items, money):
        if self.num_items < req_items:
            print("Not enough items in the machine")
        elif money < req_items * self.item_price:
            print("Not enough coins")
        else:
            return money - req_items * self.item_price


sprit = VendingMachine(100, 2)
for x in range(sprit.ulang(3)):
    print(sprit.buy(10,193))




"""
misalkan ada 3item , 1 item harganya 2
dan user pengen 3 item duitnya 10
jadinya kan harga = 3 * 2 = 6
duitnya 10 - 4 = 6 cukup 
"""
