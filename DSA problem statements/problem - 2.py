import re
from datetime import datetime

class CreditCardValidator:
    
    @staticmethod
    def validate_credit_card(card_number):
        remove_dash = re.sub(r"[-\s]", "", card_number)
        
        if not remove_dash.isdigit() or len(remove_dash) != 16:
            return "Invalid: Card must be 16 digits and numeric."
        
        f_character = remove_dash[0]
        has_different_digit = any(c != f_character for c in remove_dash)
        if not has_different_digit:
            return "Invalid: Card must contain at least two different digits."
        
        l_digit = int(remove_dash[15])
        if l_digit % 2 != 0:
            return "Invalid: Last digit must be even."
        
        total_value = sum(int(c) for c in remove_dash)
        if total_value <= 16:
            return "Invalid: Sum of digits must be greater than 16."
        
        return "Valid: Card is valid!"
    
    @staticmethod
    def validate_expiry_date(expiry_date):
        try:
            # Ensure expiration date is in MM/YY format
            expiry = datetime.strptime(expiry_date, "%m/%y")
            
            # Check if the expiration date is in the future
            if expiry < datetime.now():
                return "Invalid: Card has expired."
            
            return "Valid: Expiration date is valid."
        
        except ValueError:
            return "Invalid: Expiration date must be in MM/YY format."


def main():
    testing_cards = [
        ("9999-9999-8888-0000", "12/25"),
        ("6666-6666-6666-1666", "05/22"),
        ("a923-3211-9c01-1112", "08/23"),
        ("4444-4444-4444-4444", "10/20"),
        ("1111-1111-1111-1110", "01/23"),
        ("6666-6666-6666-6661", "09/19"),
        ("2345-7776-1230-7762", "11/24")
    ]
    
    for card, expiry in testing_cards:
        print(f"Validating card: {card}")
        card_result = CreditCardValidator.validate_credit_card(card)
        print(f"{card} -> {card_result}")
        
        expiry_result = CreditCardValidator.validate_expiry_date(expiry)
        print(f"Expiry Date: {expiry} -> {expiry_result}")
        print('-' * 50)


if __name__ == "__main__":
    main()
