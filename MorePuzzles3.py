
#This is a file for testing out a Puzzle in the Discrete Mathamatics Course

#Puzzle To Solve: Find Perfect Square
#Find integer n where n^2 = 31415…

#Import math
import math

# FINDING FIRST SOLUTION
#n is number to be squared
n = 31415

#Create variable for square root of n
x = math.sqrt(n)

#N is string version of n (for comparison later)
N = str(n)

#Round square of n for turning to string later
x = round(x,3)
#Turn rounded square of x into integer (no decimals)
x = int(x*1000)