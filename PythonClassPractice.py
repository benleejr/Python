class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w
        
    def calculateRectArea(self):
        print("Area is:", self.length*self.width)
        
def main():
    area = Rectangle(10,5)
    area2 = Rectangle(25,20)
    area.calculateRectArea()
    area2.calculateRectArea()
    
if __name__ == "__main__":
    main()