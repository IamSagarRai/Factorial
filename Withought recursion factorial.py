number = int(input("Enter any number you cn imageine: "))
fac = 1

if number < 0:
    print("The number must be greater than 0 !!")
elif number == 0:
    print("1")

for i in range (1 , number+1):
    fac = fac * i
    print("The factorial of" , number , "is" , fac)

#  You can also create an if statement which throws an error when a value less than zero has been given by the user! 