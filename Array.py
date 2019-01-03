l = [2,"Tres",True,["uno",10]]
print (l)
#Using the Array Index
l2 = l[1]
print (l2)
print (str(l[0]))
print (str(l[3]))
#Accessing Array's index that are in an Array list: [indexInArray][indexInList]
l3 = l[3][0]
print (l3)
print (str(l[3][1]))

#-------------------------------------------------------------------------------------------------------------

#Lists / Arrays / Vectors
#Declare the Array list
#Idx 0 , 1   ,  2   ,    3     ,4, 5
l = [2,"tres", True, ["uno",10],5,'Hi']
print ('Imprimir Lista: ' + str(l))
l[1] = 4
l2 = l[1]
print ('Imprimir cambio de dato Indice: ' + str(l2))
#Slicing: copy some information from an Array towards another one [beginningIndex:QuantityofCopyingElements]:
l3 = l[0:3]
l7 = l[1:3]
print ('Imprimir Slicing de Indice 0, 3 Elementos: ' + str(l3))
print ('Imprimir Slicing de Indice 1, 2 Elementos: ' + str(l7))
#Copy some information from an Array towards another one by skipping some information [beginningIndex:Quantity
#ofCopyingElements:AmountOfSkipsPerIndex]
l4 = l[0:3:2]
print ('Imprimir desde indice 0 , 3 elementos, saltando cada 2 elementos: ' + str(l4))
#Copy some information from an Array towards another one by skipping each we want [beginningIndex:Amount
#OfSkipsPerIndex]
l5 = [2,"tres",True,["uno",10],6]
l6 = l5[0::2]
print ('Imprimir Lista 5: ' + str(l5))
print ('Imprimir la informacion saltando los datos consecutivos: ' + str(l6))

#-------------------------------------------------------------------------------------------------------------

#Changing several elements in the Array-List [FromIndex:QuantityOfElements]:
l5 = [2, "Tres", True, ["uno", 10], 6]
l5 [0:2] = [4, 3]
print ("Printing changes to l5: " + str(l5))
#Modify several elements in the Array-List with just one data [FromIndex:QuantityOfElements]:
l6 = [2, "tres", True, ["uno",10], 6]
l6 [0:2] = [5]
print ("Printing changes to l6: " + str(l6))
#Get data from an array with negative index:
l6 = [2, "tres", True, ["uno", 10], 6]
l7 = l6 [-1]
l8 = l6 [-2]
print ("Printing from l6 -1: " + str(l7))
print ("Printing from l6 -2: " + str(l8))