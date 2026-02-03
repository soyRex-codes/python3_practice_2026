import requests
import time

# This is the address where your API is living
BASE_URL = "http://127.0.0.1:8000"

print("--- STARTING SHOPPING SIMULATION ---")

# 1. Check if API is alive
response = requests.get(f"{BASE_URL}/")
print(f"Server says: {response.json()}")

# 2. Add some items (Simulating a user clicking 'Add to Cart')
items_to_buy = [10.50, 5.00, 99.99, 4.25]

for price in items_to_buy:
    print(f"Buying item for ${price}...")
    # We use POST here because we are CREATING data
    response = requests.post(f"{BASE_URL}/add/{price}")

    # Check if the server accepted it (Status Code 200 means OK)
    if response.status_code == 200:
        print(" -> Success!")
    else:
        print(" -> Failed!")

    # specific delay to make it look like a real human typing
    time.sleep(1)

print("--- SHOPPING COMPLETE ---")

# 3. Ask for the Receipt
print("Fetching Receipt from Server...")
receipt_response = requests.get(f"{BASE_URL}/receipt")
receipt_data = receipt_response.json()

print("\n--- FINAL RECEIPT ---")
print(f"Total Spent: ${receipt_data['total']}")
print(f"Average Item Cost: ${receipt_data['average']}")
print(f"Total Items: {receipt_data['count']}")