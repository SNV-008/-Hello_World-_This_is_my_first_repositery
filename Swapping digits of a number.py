#taking x as input; it will default in string
x = input("Enter a three digit number from 001-999")
#taking two variable and listing them x
y = list(x)
z = list(x)
k = int(x)
if int(k) <= 0 or int(k) >= 999:
    print("Hey idiot! You were told to type a three digit number from 001-999")
    exit(1)
#changing the characters
y[0]=x[2]
y[1]=x[1]
y[2]=x[0]
#taking two variable for sentences to join them
ori = "Original Value ="
rev = ":) Reversed value ="
#taking two variables to map and remove brackets & commas of the listed numbers
m = ''. join(map(str, z))
n = ''. join(map(str, y))
#printing both sentences and values
print(ori, m)
print(rev, n)
