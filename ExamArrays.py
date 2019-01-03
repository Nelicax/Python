# Creating Array List (readyList1)
readyList1 = [8,"I am a Double Quotation String",True,["one", 2, 3], 3.16, 'I am a Single Quotation String']

# Printing readyList1
print("readyList1: " + str(readyList1))

# Changing Index 3 into a number 5
readyList1[3] = 5

# Reprinting the array with the new data on Index 3
print("New readyList1: " + str(readyList1))

# Slicing beginning from the index 1 and copying 3 elements on the array readyList1,
# by doing it on the readyList2 variable.
readyList2 = readyList1[1:4]

# Then print both lists.
print("readyList1: " + str(readyList1))
print("readyList2: " + str(readyList2))

# Creating a readyList3 variable, and filling it with the same information on the original readyList1
readyList3 = [8,"I am a Double Quotation String",True,["one", 2, 3], 3.16, 'I am a Single Quotation String']

# Then printing the list.
print("readyList3: " + str(readyList3))

# Copying information into readyList4 from readyList3 Index 0 skipping every two elements
readyList4 = readyList3[0::2]

# Printing readyList4.
print("readyList4: " + str(readyList4))



