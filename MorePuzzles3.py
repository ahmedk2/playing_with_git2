
#This is a file for testing out a Puzzle in the Discrete Mathamatics Course

#Puzzle To Solve: Find Perfect Square
#Find Integer n where n^2 starts with 31415……

#Import math
import math

# FINDING FIRST SOLUTION
#n is number to be squared
n = 31415

#Create variable for square root of n
x = math.sqrt(n)

#Print x (Root of n) for debugging
print(x)

#N is string version of n (for comparison later)
N = str(n)

#Round square of n for turning to string later
x = round(x,3)
#Turn rounded square of x into integer (no decimals)
x = int(x*1000)

#Print x (rounded) for debugging
print(x)

#For each number for a power
for y in range(1, 5):
    #Test each power in case of many solutions
    #Where x is rounded number from before
    t = x**y
    #Turn integer t into string for comparison
    t = str(t)
    #If the first characters of the powered number is the number to check
    if t[0:5] == N[0:5]:
        #Return result
        print("{} to the power of {} works.".format(x,y))
        
