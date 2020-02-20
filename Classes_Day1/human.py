class Human:
    """This is a human class"""

    def ___init__(self, human_gender="human", age=0):
        self.human_gender = human_gender
        self.age = age

    def speak(self):
        print("Hi I am a: ", self.human_gender)


class Man(Human):
    """This is a Man class"""

    def __init__(self, hair_colour, age):
        super().___init__(human_gender="male", age=age)
        self.hair_colour = hair_colour
        print("Hi, I am a ", self.human_gender, "my hair is",
              self.hair_colour, "I am", self.age, "years old, so there you go!")


A_man = Man("black", 30)
print("The human is a: ", A_man.human_gender)
print("The human is: ", A_man.age)
print("The human's hair is: ", A_man.hair_colour)
A_man.speak()
