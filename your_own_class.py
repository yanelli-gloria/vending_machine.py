'''
Name: Yanelli Gloria
Assignment: 9.1 Shapes

Assignment Description: You will be required to submit a script that includes your implementation of 
a custom class that is based on a real-world object. The script should include your class and a main 
function that contains a demo program. You are also required to submit a README that includes 
documentation of your class and instructions to run the demo program.
'''

class Vending_Machine():
    # Class Variable 
    maximum_cash_amount = 20
    def __init__(self, dollar, snack, drink):
        # Public Data Variable
        self.dollar = dollar
        # Private Data Variable
        self.__snack = snack
        # Private Data Variable
        self.__drink = drink

    # METHOD 1
    def Highest_Amount(self):
        return (f"The highest bill you can use is a ${self.maximum_cash_amount}")
        # Stating the highest bill the vending machine can take

    # METHOD 2
    def Purchasing(self):
        return (f"You are purchasing {self.__snack} and {self.__drink}.")
        # Stating what is being purchased from the vending machine - serves as a receipt


class Update(Vending_Machine):
    def __init__(self, snack, drink):
        # Super() calls the parent function
        super().__init__(self, snack, drink)
        self.__snack = snack
        self.__drink = drink

    # SETTER METHOD
    def set_snack(self, snack):
        if snack == "Goldfish":
            # Vending Machine no longer has goldfish
            print("Sorry, we are out of Goldfish")
        else: 
            # Default to the buyer's requested snack
            self.__snack = snack

    # SETTER METHOD
    def set_drink(self, drink):
        if drink == "Sprite":
            # Vending Machine no longer has Sprite
            print("Sorry, we are out of Sprite.")
        else:
            # Default to the buyer's requested drink
            self.__drink = drink

    # GETTER METHOD
    def get_snack(self):
        return self.__snack

    # GETTER METHOD
    def get_drink(self):
        return self.__drink


# MAIN FUNCTION
def main():
    a = Vending_Machine("$1", "Pretzels", "Pepsi")
    print(a.Highest_Amount())
    print(a.Purchasing())

    '''The buyer is purchasing Pretzels and Pepsi -that are a dollar each- from a vending machine.
    The function Highest Amount states the highest bill the buyer can use. The function Purchasing 
    will provide a receipt of what the buyer has purchased from the vending machine. In the main, 
    the values dollar, snack, and drink are listed. '''

    b = Update("Goldfish", "Sprite")
    print(b.set_snack("Goldfish"))
    print(b.set_drink("Sprite"))
    print(b.get_snack())
    print(b.get_drink())

    '''The buyer is seeking to purchase Goldfish and Sprite from the vending machine. Unfortunatly,
    there is no more. Both Setter and Getter are used within the class Update. The snack is set to 
    Goldfish and the drink is set to Sprite. By using Getter, what the buyer asked for is repeated.'''

if __name__ == "__main__":
    main()