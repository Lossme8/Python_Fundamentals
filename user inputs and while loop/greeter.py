name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "if you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your last name? "
last_name = input(prompt)
age = input("How old are you? ")
print("\nHello, " + name + " " + last_name + ", you are " + str(age) + " years old !")

