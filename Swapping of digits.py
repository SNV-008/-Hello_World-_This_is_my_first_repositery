#first we will take x variable as input entered
x = input("Enter a digit from 001-999, but while typing single digit then type two 0\'s before the number, and while typing double digit number type only one 0 behind them.")
#Now i have taken 2 variables for listing as one will be changed,b ut one will not be changed as well when printed both should look like one another
y = list(x)
z = list(x)
#changing the characters of both variable
y[0] = x[2]
y[1] = x[1]
y[2] = x[0]
#printing the both
print("Original value =", z)
print("Reversed value =", y)
