"""
PROG10004 Programming Principles
Assigment 2-Part A
Name:Jinfeng He(komi)
This program inputs a number of integers displays several statistics.
"""

#Input
count = int(input("How many integers would you like to enter? "))
while count <= 0:
   print("Please enter a positive number that bigger than 0")
   count = int(input("How many integers would you like to enter? "))

#processing
total = 0
positive = 0
negative = 0

for i in range(count):
    num = int(input("Please Enter the integer: "))
    print("You entered the number", num)

#For the total number(total=0+num to get the new total than + new num)
    total = total + num

#Starting from the first number entered(Set the number to the highest and lowest)
    if i == 0:
        highest = num  
        lowest = num
    else:  #if the following number is bigher or smaller than the prev number
        if num >highest:
            highest = num
        if num < lowest:
            lowest = num
#find the number is postive or negative (p/n is 0) 
    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1

#Calculate the Average
average = total / count 

#Output
print("Results")
print("The total number is", total)
print("The average number is", average)
print("The number of positive is", positive)
print("The number of negatives is", negative)
print("The highest is", highest)
print("The lowest is", lowest)







