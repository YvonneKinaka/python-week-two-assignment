# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # apply discount only if 20% or higher
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # return original price if discount < 20%

# Main program
try:
    # Get user input
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(price, discount_percent)

    # Display result
    if discount_percent >= 20:
        print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
