class Order:
    
    
    def __init__(self):
        
        self.order_list = list()
        self.total_price = 0
        
    def add_order(self, new_order):
        
        self.order_list.append(new_order)
        new_order.price = self.price(new_order)
        self.total_price = round(self.total_price, 2)
        
    def price(self, i):
        if i.type == 1:
            price = i.pizza.price
            self.total_price += price
            
        elif i.type == 2:
            price = round(i.pizza.price * 0.6 * 1.05, 2)
            self.total_price += price
                
        elif i.type == 3:
            price = round(i.pizza.price * 1.4 * 0.95, 2)
            self.total_price += price
        return price
        
    def check(self):
        all_type = ['стандартна', 'мала', 'велика']
        
        print('Ваше замовленя:')
        for i in self.order_list:
            print(i.pizza.number, i.pizza.name, all_type[i.type-1], i.price)
        print('Загальна вартість замовленя:', self.total_price)
        
class my_order:
    
    def __init__(self, pizza, type):
        
        self.pizza = pizza
        self.type = type
        self.price = 0