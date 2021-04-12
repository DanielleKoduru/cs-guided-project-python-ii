class Animal:
    def __init__(self, kind, color, name):
        # Construct a new instance of animal
        self.kind = kind
        self.color = color
        self.name = name
        self.num_legs = 4
​
    def description(self):
        print(f'{self.name} is a {self.kind} with color {self.color}')
    
    
​
​
cat = Animal('cat', 'orange', 'Tabby')
dog = Animal('dog', 'golden', 'Woffie')
​
dog.description()
​
print(cat.num_legs)