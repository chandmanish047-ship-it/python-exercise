class Animal():
    def __init__(self,bark,meow):
        self.bark=bark
        self.meow=meow
    def dog(self):
        return self.bark
    def cat(self):
        return self.meow
animal=Animal()
print(animal.dog())
print(animal.cat())