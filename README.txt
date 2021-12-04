The README file:

Class Documentation
    Description of class Vending Machine: 
    This class is in charge of setting up the basis of a vending machine. It necessitates user-inputted values 
    such as dollar, snack, and drink. This is because a typical vending machine asks for this information. 
    This class has 2 private variables that are called upon within its following methods. The main contains the
    values this class asks for when initialized (dollar, snack, drink).

    Description of Data Variables:
    Both "maximum_bill_amount" and "self.dollar" are not private variables like "self.__snack" or "self.__drink".
    The user-inputted values asked for are dollar, snack, and drink; which are identified during initialization

    Decription of Each Method:
    Method 1: def Highest_Amount(self)
    This method is responsible for deriving the value of "maximum_bill_amount" from class Vending Machine. 
    It states the highest bill the vending machine can take, which is a $20.

    Method 2: def Purchasing(self)
    This method is responsible for acting like a receipt - reminding the user what they ordered from the 
    vending machine. It states which snack and drink were purchased. These two values are identified 
    because they call upon call Vending Machine.

Demo Program Documentation:
    A decription of the demo program:
    In the main, an example is utilized to test the code. Here, the buyer purchases Goldfish and Sprite, which
    are a dollar each. The buyer is reminded that a $20 is the highest bill that the vending machine can take. The
    buyer is also told what they are purchasing, ergo acting as a receipt. When the buyer intends to purchase a 
    snack or drink that is no longer in stock, they are informed of the circumstance - "Sorry, we are out of ___".
    Lastly, they are reminded of which snacks and drinks are no longer available. 
    
    Instruction on how to run the demo program:
    By using the terminal that is already implemented within VS Code, the correct responses will be successfully 
    returned or printed out.
