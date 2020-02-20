class Vegetables:
    """this attempts tho demostrate list of vegetables in store"""

    def __init__(self, product, total, year):
        """Initialize attributes to represent an item"""
        self.product = product
        self.total = total
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        vegetable_name = f"{self.product} {self.total} {self.year}"
        return vegetable_name.title()


my_favourite_vegetable = Vegetables('cabbage', '20', 2020)
print("The most bought item is: " + self.product + "and was bought mainly in the year ".get_descriptive_name())
