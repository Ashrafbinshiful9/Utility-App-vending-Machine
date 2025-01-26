# Welcome message with emojis
print('''___ASHRAF'S CUSTOM VENDING MACHINE! 🍕🍫___''')  # Display a welcome message for the vending machine.

# Menu Book with emojis
# This dictionary contains all the items available in the vending machine, including their names, prices, and stock levels.
MENU_BOOK = {
    'D1': {'NAME': '🍿 POPCORN', 'price': 2.50, 'stock': 10},
    'D2': {'NAME': '🍪 OREOS', 'price': 3.00, 'stock': 10},
    'E1': {'NAME': '🌮 NACHOS', 'price': 3.50, 'stock': 10},
    'E2': {'NAME': '🍬 TRAIL MIX', 'price': 4.25, 'stock': 10},
    'F1': {'NAME': '🍭 GUMMY BEARS', 'price': 2.00, 'stock': 10},
    'F2': {'NAME': '🍫 ENERGY BAR', 'price': 5.00, 'stock': 10},
    'A1': {'NAME': '🍋 LEMONADE', 'price': 3.00, 'stock': 10},
    'A2': {'NAME': '🧊 ICED TEA', 'price': 2.50, 'stock': 10},
    'B1': {'NAME': '💧 SPARKLING WATER', 'price': 1.50, 'stock': 10},
    'B2': {'NAME': '☕ COFFEE', 'price': 2.00, 'stock': 10},
    'C1': {'NAME': '🍏 APPLE JUICE', 'price': 2.75, 'stock': 10},
    'C2': {'NAME': '🥤 MILKSHAKE', 'price': 4.00, 'stock': 10}
}

# User points for gamification
user_points = 0  # Initialize user points to zero for tracking purchases.

# Function to display available items
def display_items():
    print("\nItems available to buy:")  # Print a header for available items.
    for key, item in MENU_BOOK.items():  # Loop through each item in the menu.
        print(f"{key}. {item['NAME']} - ${item['price']} (Stock: {item['stock']})")  # Display item details.

# Function to select an item
def select_item():
    item_number = input("\nEnter the item code you want to buy: ")  # Prompt user for the item code.
    if item_number in MENU_BOOK and MENU_BOOK[item_number]['stock'] > 0:  # Check if the item is valid and in stock.
        return MENU_BOOK[item_number], item_number  # Return the item details and its code.
    else:
        print("Item not available or out of stock.")  # Inform the user if their choice isn't available.
        return None, None  # Return None if the selection is invalid.

# Function to process payment
def process_payment(price):
    payment_method = input("Choose payment method (cash/card): ").lower()  # Ask how the user wants to pay.
    while True:  # Keep asking until we get a valid payment.
        try:
            if payment_method == "cash":
                amount_paid = float(input(f"The item costs ${price}. Insert cash: "))  # Get cash amount from the user.
            elif payment_method == "card":
                amount_paid = float(input(f"The item costs ${price}. Enter card amount: "))  # Get card amount from the user.
            else:
                print("Invalid payment method. Please choose 'cash' or 'card'.")  # Handle invalid payment method.
                payment_method = input("Choose payment method (cash/card): ").lower()  # Ask again.
                continue
            
            if amount_paid >= price:  # Check if the user has paid enough.
                return amount_paid  # Return the amount they paid.
            else:
                print("Insufficient funds. Please insert more money.")  # Let them know they need to pay more.
        except ValueError:
            print("Please enter a valid number.")  # Handle cases where the input isn't a number.

# Function to update stock after purchase
def update_stock(item_number):
    MENU_BOOK[item_number]['stock'] -= 1  # Decrease the stock for the purchased item.

# Function to issue a receipt
def issue_receipt(item, amount_paid):
    change = round(amount_paid - item['price'], 2)  # Calculate how much change to give back.
    print("\nReceipt:")  # Start the receipt.
    print(f"Item: {item['NAME']} 😊")  # Show the item name with a smiley.
    print(f"Price: ${item['price']}")  # Show the price of the item.
    print(f"Amount Paid: ${amount_paid}")  # Show how much the user paid.
    print(f"Change: ${change}")  # Show the change.

# Function to simulate automatic dispensing
def dispense_item(item):
    print(f"\nDispensing {item['NAME']}...")  # Let the user know their item is being dispensed.
    print("The vending machine door is opening automatically...")  # Simulate the door opening.
    print("Please ensure no hands are in the way!")  # A friendly safety reminder.
    print("Item dispensed! Enjoy your snack! 🎉")  # Confirm that the item is ready to enjoy.

# Function for refund
def process_refund(item):
    refund_choice = input("Do you want a refund for this item? (yes/no): ").lower()  # Ask if the user wants a refund.
    if refund_choice == "yes":
        print(f"Refund processed for {item['NAME']}.")  # Confirm the refund.
        return True  # Return True to indicate a refund was processed.
    return False  # Return False if no refund was requested.

# Function to suggest a discount on a specific item
def suggest_discount():
    discount_item = MENU_BOOK['B2']  # Let's say COFFEE has a discount.
    discounted_price = round(discount_item['price'] * 0.8, 2)  # Calculate a 20% discount.
    print(f"\n🎉 Special Offer! {discount_item['NAME']} is now only ${discounted_price}!")  # Let the user know about the deal.
    buy_discounted = input(f"Do you want to buy {discount_item['NAME']} at the discounted price? (yes/no): ").lower()  # Ask if they want to buy it.
    if buy_discounted == "yes":
        return discount_item  # Return item if the user wants to buy it.
    return None  # Return None if no item was purchased.

# Main loop to handle purchasing items
def vending_machine():
    global user_points  # Access the global user_points variable to keep track of points.
    while True:  # Keep the vending machine running for multiple purchases.
        display_items()  # Show available items.
        selected_item, item_number = select_item()  # Get user's selection.
        
        if selected_item:  # If a valid item was selected.
            amount_paid = process_payment(selected_item['price'])  # Process payment.
            update_stock(item_number)  # Update stock.
            issue_receipt(selected_item, amount_paid)  # Print receipt.
            
            # Add points for the gamification.
            user_points += 1  # Increment user points.
            print(f"You have earned 1 point! Total points: {user_points}")  # Inform user of points earned.
            
            # Simulate dispensing the item.
            dispense_item(selected_item)
            
            # Suggest a discount on a specific item.
            discounted_item = suggest_discount()
            if discounted_item:  # If the user buys the discounted item, process it.
                amount_paid_discounted = process_payment(discounted_item['price'])  # Process payment for the discounted item.
                update_stock('B2')  # Update stock for the discounted item.
                issue_receipt(discounted_item, amount_paid_discounted)  # Print receipt for the discount item.
            
            # Process refund.
            if process_refund(selected_item):  # Check if refund is requested.
                MENU_BOOK[item_number]['stock'] += 1  # Restore stock for the refunded item.
                user_points -= 1  # Deduct a point for refund.
                print(f"You have lost 1 point. Total points: {user_points}")  # Inform user of points lost.
        
        # Ask if the user wants to buy another item.
        more_items = input("\nDo you want to buy another item? (yes/no): ").lower()  # Prompt for more purchases.
        if more_items != "yes":  # If user does not want to continue.
            print("\nThank you for using the vending machine! 😊")  # Thank the user.
            break  # Exit the loop.

# Run the vending
vending_machine()  # Start the vending machine program.