from fastapi import FastAPI
from engine import ExpenseTracker # Importing class ExpenseTracker from backend file
"""
Critical Concept: "Separation of Concerns"
Look at line 2: from engine import ExpenseTracker. This api.py file knows nothing about how to calculate averages or store lists.
It just knows how to receive a web request and pass it to the tracker object. This is how Google, Amazon, and Netflix structure their code.
"""


# 1. Initialize the API(The "storefront")
app = FastAPI()
# 2. initialize my class (The "Back Office")
# we create ONE instance of our tracker to keep in memory
tracker = ExpenseTracker()

# --- The ENDPOINTS (The "Menu") ---

# A simple health check to see if server is alive
@app.get("/")
def home():
    return {"message": "API is Online and ready."}

# Endpoint to add a price
# Notice I pass 'amount' in the URL (e.g. /add/50)
@app.post("/add/{amount}")
def add_expense(amount: float):
    #Calling my class function
    message = tracker.add_price(amount)
    return {"status": "success", "info": message}

# Endpoint to get the final calculations
@app.get("/receipt")
def receipt():
    # Calling my class function to get the dictionary
    data = tracker.get_summary()
    return data

