# Defining first the discounts for each product.

Product_A_Discount = 75
Product_B_Discount = 50
Product_C_Discount = 25
Product_D_Discount = 0
Product_E_Discount = 0

# Defining next the Products' Original Cost.

Product_A_Cost = 1000
Product_B_Cost = 500
Product_C_Cost = 250
Product_D_Cost = 100
Product_E_Cost = 50

# Defining next the Products' Total Cost After Discount.

Product_A_AfterDiscount = Product_A_Cost-((Product_A_Cost*Product_A_Discount)/100)
Product_B_AfterDiscount = Product_B_Cost -((Product_B_Cost*Product_B_Discount)/100)
Product_C_AfterDiscount = Product_C_Cost -((Product_C_Cost*Product_C_Discount)/100)
Product_D_AfterDiscount = Product_D_Cost -((Product_D_Cost*Product_D_Discount)/100)
Product_E_AfterDiscount = Product_E_Cost -((Product_E_Cost*Product_E_Discount)/100)

# Defining Infinite Loop so Clients can continue buying as per the Optional Requirement.

while True:

    # Next greetings and providing instructions to receive from the user, the quantity of products to buy for EACH type as instructed.

    print("Welcome to Store Manager 1.0")
    try:
        Product_A_Amount = (input("Enter, using numbers, the amount of Product A in the order: "))
        Product_A_Amount = (int(Product_A_Amount))
    except:
        print ("Only numbers allowed")
    else:
        try:
            Product_B_Amount = (input("Enter, using numbers, the amount of Product B in the order: "))
            Product_B_Amount = (int(Product_B_Amount))
        except:
            print("Only numbers allowed")
        else:
            try:
                Product_C_Amount = (input("Enter, using numbers, the amount of Product C in the order: "))
                Product_C_Amount = (int(Product_C_Amount))
            except:
                print ("Only numbers allowed")
            else:
                try:
                    Product_D_Amount = (input("Enter, using numbers, the amount of Product D in the order: "))
                    Product_D_Amount = (int(Product_D_Amount))
                except:
                    print ("Only numbers allowed")
                else:
                    try:
                        Product_E_Amount = (input("Enter, using numbers, the amount of Product E in the order: "))
                        Product_E_Amount = (int(Product_E_Amount))
                    except:
                        print ("Only numbers allowed")
                    else:
                        # Next calculating the discount to all products that need it and summarizing all to share final amount to pay.
                        print ('THE TOTAL TO PAY FOR THIS ORDER IS ',
                        (Product_A_Amount* Product_A_AfterDiscount)+
                        (Product_B_Amount* Product_B_AfterDiscount)+
                        (Product_C_Amount* Product_C_AfterDiscount)+
                        (Product_D_Amount* Product_D_AfterDiscount)+
                        (Product_E_Amount* Product_E_AfterDiscount)
                        )







