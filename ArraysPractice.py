# Creating Array List (arrayList1)
arrayList1 = [8,"I am a Double Quotation String",True,["one",2,3,"four","Five"],3.16,'I am a Single Quotation String']

# Printing arrayList1
print("arrayList1: " + str(arrayList1))

# Changing Index 3 into a number 10
arrayList1[3] = 10

# Reprinting the array with the new data on Index 3
print("New arrayList1: " + str(arrayList1))

# Slicing beginning from the second index and copying 4 elements on the array arrayList1,
# by doing it on the arrayList2 variable.
arrayList2 = arrayList1[2:6]

# Then print both lists.
print("arrayList1: " + str(arrayList1))
print("arrayList2: " + str(arrayList2))

# Creating a arrayList3 variable, and filling it with the same information on the original arrayList1
arrayList3 = [8,"I am a Double Quotation String",True,["one",2,3,"four","Five"],3.16,'I am a Single Quotation String']

# Then printing the list.
print("arrayList3: " + str(arrayList3))

# Copying information into arrayList4 from arrayList3 Index Zero skipping every two elements
arrayList4=arrayList3[0::2]

# Printing arrayList4.
print("arrayList4: " + str(arrayList4))






