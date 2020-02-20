def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3,40,5))

# ----------------------------------------------------
bread = 15 # loafs
juice = 10 #bottles
butter = 20 #containers

def shop(bread, juice, butter):
    if bread >= juice and bread >= butter:
        return bread
    elif juice >= bread and juice >= butter:
        return juice
    else:
        return butter
print("\nThe most bought items in the shop is " + str(max_num(15,10,20)))



