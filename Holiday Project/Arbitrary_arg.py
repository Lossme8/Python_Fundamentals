def farm(*vegetables):
    """This code attempts to demonstrate the products we have at our farms"""

    for vegetable in vegetables:
        """
        This would ask the customer a question
        and a response would be printed adjecent to it
        """
        print("\nGood day!\n What would you like us to supply you with today?", vegetable)
farm("onions", "carrots", "tomatoes", "cabbage", "beetroot")
