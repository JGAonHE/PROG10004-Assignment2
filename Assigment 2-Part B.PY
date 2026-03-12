"""
PROG10004 Programming Principles
Assigment 2-Part B
Name:Jinfeng He(komi)
This program to create and print rectangles made of a specific character
"""

class RectangleMaker:

    def __init__(self, w, h, ch):
        self.width = w 
        self.height = h
        self.character = ch
    
    def print(self):
#self.height is rows,and self.width is cols.
        for i in range(self.height):
            for j in range(self.width):
                print(self.character, end="")
            print()

#main code creates three objects
rectangle1 = RectangleMaker(5, 3, 'O') #• A 5 x 3 rectangle made of the letter ‘O’ 

rectangle2 = RectangleMaker(16, 6, 'T')#• A 16 x 6 rectangle made of the letter ‘T’ 

rectangle3 = RectangleMaker(2, 4, '%')#• A 2 x 4 rectangle made of the left square bracket ‘%’ 

#use the print method(print())
rectangle1.print()
print()

rectangle2.print() 
print()

rectangle3.print() 
print()


    




