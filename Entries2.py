#To avoid values issues when expecting an integer and receiving a letter, we just create a try-catch exception
# +While Loop for user to try again
valor = 0
while True:
# +While Loop for user to try again
    try:
      valor = input("Write a Number: ")
      valor = int(valor)
    except:
      print ("That isn’t a number")
    else:
      print (valor)



