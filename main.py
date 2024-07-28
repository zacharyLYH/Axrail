"""
Functional requirements:
- Vending machine logic
- A few drinks as your items with any price (no coin). 
- Insert any notes to buy drinks. 
- Release the least amount of notes back to the customer.
"""

class VendingMachine:
    def __init__(self):
        self.drinks = {
            'Coke': 12,
            'Sprite': 15,
            'Water': 1,
            'Juice': 10
        }
        self.stock = {
            'Coke': 10,
            'Sprite': 10,
            'Water': 1,
            'Juice': 0
        }
        self.notes = {
            100: 0,
            50: 2,
            20: 3,
            10: 2,
            5: 1,
            1: 3
        }
        self.notesAvailable = [100,50,20,10,5,1]

    def show_drinks(self):
        print("Vending machine")
        print("Enter 'X' to exit at any time.\n")
        print("Catalog:")
        for drink, price in self.drinks.items():
            if self.stock[drink] > 0:
                print(f"{drink}: ${price}")
        print("\n")

    def calculate_change(self, amount_paid, cost):
        change = amount_paid - cost
        change_notes = []
        notes_copy = self.notes.copy()
        for note in self.notesAvailable:
            while notes_copy[note] > 0 and change >= note:
                notes_copy[note] -= 1
                change_notes.append(note)
                change -= note
        if change > 0:
            return -1
        else:
            self.notes = notes_copy
        return change_notes

    def main(self):
        self.show_drinks()
        choice = ""

        while choice == "" :
            choice = input("Enter the name of the drink you want to buy (or 'X' to cancel): ")
            if choice not in self.drinks:
                if choice == 'X' :
                    return
                choice = ""
                print("Invalid choice.")
        
        cost = self.drinks[choice]
        print(f"The cost of {choice} is {cost} units.\n")
        amount_paid = 0
        while amount_paid < cost:
            amount_input = input("Enter the amount you are paying (or 'X' to cancel): ")
            if amount_input.upper() == 'X':
                print("Transaction canceled.")
                return
            try:
                amount_paid = int(amount_input)
                if amount_paid < cost:
                    print("Insufficient funds.")
            except ValueError:
                print("Invalid input. Please enter a valid amount or 'X' to cancel.")
        
        #User inputs validated up till this point
        self.stock[choice] -= 1
        change_notes = self.calculate_change(amount_paid, cost)
        if change_notes == -1:
            print(f"Transaction failed! Vending machine doesn't have enough change... Issuing refund.")
            return
        
        print(f"Transaction successful! Dispensing {choice}")
        print(f"Change returned: {change_notes}")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.main()
