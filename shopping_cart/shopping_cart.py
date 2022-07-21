'''
Created on 5 jun. 2020

@author: RSSpe
'''

class NotExistItemError(Exception):
    pass

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def code(self):
        return f"{self.name}-123456789" 
        
    def __str__(self):
        return self.name


class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        
    def contains_item(self):
        return len(self.items)>0
    
    def total(self):
        return sum([ item.price for item in self.items])
    
    def remove_item(self, item):
        self.items.remove(item)
        
    def get_item(self, item):
        if item not in self.items:
            raise NotExistItemError("Item does not exists")
        else:
            return self.items[ self.items.index(item) - 1 ]
