


def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount_percent)
    print(f"Final price after discount: R{final_price:.2f}") 

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

main()

