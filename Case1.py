#While loop example
#Declare the variable
AmountDesired = 0
#Define the variable condition
while True:
    #Get the input from the user and modify the variable at the same time
    AmountDesired = (input("Enter the amount desired: "))
    #Turn the input from str to int
    AmountDesired = (int(AmountDesired))
    #Define action based on input
    AmountGranted = (AmountDesired * 2)
    print(AmountGranted)
    #Condition to break loop
    if AmountGranted >= 1000:
        break
