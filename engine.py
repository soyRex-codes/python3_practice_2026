import statistics #for math functionalities

"""
Why this is different from before:
self: You will see self everywhere. In Python, self is how the object refers to its own memory. self.prices means "MY list of prices," not just any list.
No input(): Notice there are no input() or print() statements inside the class? That is intentional. 
The Engine should never talk to the user directly. It only talks to the API."""

class ExpenseTracker:
    #The "constructor": This runs automatically when you create the object.
    # It sets up the empty memory (State)
    # need to put better more convincing/self-explanatory comments
    def __init__(self):
        self.prices = [] #List
        self.total = 0.0 #Our total Variable

    # Function to add a price (State Change)
    def add_price(self, price: float):
        self.prices.append(price)
        self.total += price
        return f"Added ${price} sucessfully."

    # Function to get analytics (Read only)
    def get_summary(self):
        if len(self.prices) == 0:
            return {"total":0, "average":0, "count":0}
        avg = statistics.mean(self.prices)
        return {
            "total":self.total,
            "average": round(avg, 2),
            "count": len(self.prices)
        }

    # Function to save data (Persistence)
    def save_to_disk(self, filename="receipt.txt"):
        with open(filename, "w") as file:
            file.write(f"Total: ${self.total}\n")
            file.write(f"Items: {self.prices}")
        return "File Saved."