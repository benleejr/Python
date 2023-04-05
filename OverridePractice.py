class Fruit:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        if (self.name == other.name):
            print("Fruits are the same\n")
        else:
            print(self.name, "and", other.name, "are different fruits\n")
        
def main():
    fruit1 = Fruit("apple")
    
    fruit2 = Fruit("orange")
    
    fruit3 = Fruit("apple")
    
    fruit1 == fruit2
    
    fruit1 == fruit3    
    
main()