from abc import ABC, abstractmethod

class Pizza(ABC):
    
    @abstractmethod
    def getter(self):
        pass

class Pizza_Hawaii_4(Pizza):
    
    def __init__(self):
        self.number = 1
        self.price = 150
        self.ingredients = ['шинка', 'ананаси', 'цибуля', 'зелений перець', 'халапеньйо', 'сир', 'томатний соус']
        self.name = "Гавайська піца"
        self.weight = 530
     
    @property
    def getter(self):
        return self.number, self.name, self.price, self.ingredients
        
        
class Pizza_Сapricose_5(Pizza):
    
    def __init__(self):
        self.number = 2
        self.price = 155
        self.ingredients = ['кукурудза', 'м\'ясо', 'гриби', 'мариновані помідори', 'оливки', 'сир Рікотта', 'сир пармезан', 'шинка', 'зелень', 'оливкова олія']
        self.name = "Піца «Капрічоза»"
        self.weight = 470
        
    @property
    def getter(self):
        return self.number, self.name, self.price, self.ingredients
        
class Pizza_Neapolitan_7(Pizza):
    
    def __init__(self):
        self.number = 3
        self.price = 150
        self.ingredients = ['сир', 'оливки', 'ковбаса', 'свіжі помідори', 'оливкова олія']
        self.name = "Піца по-неаполітанські"
        self.weight = 730
        
    @property
    def getter(self):
        return self.number, self.name, self.price, self.ingredients
        
class Pizza_with_tuna_12(Pizza):
    
    def __init__(self):
        self.number = 4
        self.price = 160
        self.ingredients = ['тунець', 'томатний соус', 'оливки', 'моцарелла']
        self.name = "Піца з тунцем"
        self.weight = 725
        
    @property
    def getter(self):
        return self.number, self.name, self.price, self.ingredients
        
class Pizza_Hunting_14(Pizza):
    
    def __init__(self):
        self.number = 5
        self.price = 145
        self.ingredients = ['помідори', 'моцарелла', 'соус', 'корнішони', 'мисливські ковбаски', 'цибуля']
        self.name = "«Мисливська» піца"
        self.weight = 750
        
    @property
    def getter(self):
        return self.number, self.name, self.price, self.ingredients
        
