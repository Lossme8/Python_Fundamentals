is_male = False #Change this to true or false to check the print out statements
is_tall = True

if is_male:
      print("You are a male")
else:
    print("You are not a male")
#OR operator to drive the if statement, this normally is called logic OR
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

  #AND operator to drive the if statement,this normally is called logic OR
if is_male and is_tall: #all the conditions must be true
    print("You are a tall male ")
elif is_male and not(is_tall):
      print("You are a short male")
elif not(is_male) and is_tall:
                             print("You are not male but are tall")
else:
    print("You  not a male and not tall")
