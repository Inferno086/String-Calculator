"""********** CALCULATOR IN PYTHON BY ARJUN SHUKLA **********"""
"""This calculator is designed to take user input as a string, find the different numbers and operators
   in the string and then do the calculation to better the user interface. My main purpose is to practise
   Object Oriented Programming in Python and the working of loop on strings throught this project"""

class Calculator():
    """This is the calculator class. It contains all the methods."""
    def __init__(self,x):
        self.x = x
        self.num1 = ""
        self.oper1 = ""
        self.oper2 = ""
        self.actual_num_1 = ""
        self.actual_num_2 = ""
        self.number1 = 0
        self.actual_number_1 = 0 
        self.actual_number_2 = 0

    def readUserInput(self):
        """This method reads the string entered by the user and seperates numbers and operators"""
        for i in range(len(self.x)):
            if self.x[i].isnumeric():
                self.num1 += self.x[i]
            else:
                if len(self.oper1) == 0:
                    self.oper1 = self.x[i]
                    self.actual_num_1 = self.num1
                elif len(self.oper2) == 0:
                    self.oper2 = self.x[i]
                    self.actual_num_2 = self.num1
                self.num1 = ""

    def outputPrinterTwoNumbers(self):
        """This method calculates and prints the output for two numbers"""
        self.actual_number_1 = int(self.actual_num_1)
        self.number1 = int(self.num1)

        if self.oper1 == "+":
            print(self.actual_number_1 + self.number1)
        elif self.oper1 == "-":
            print(self.actual_number_1 - self.number1)
        elif self.oper1 == "*":
            print(self.actual_number_1 * self.number1)
        elif self.oper1 == "/":
            print(self.actual_number_1 / self.number1)

    def outputPrinterThreeNumbers(self):
        """This method calculates and prints the output for three numbers"""
        self.number1 = int(self.num1)
        self.actual_number_1 = int(self.actual_num_1)
        self.actual_number_2 = int(self.actual_num_2)

        if self.oper1 == "+":
            if self.oper2 == "+":
                print(self.actual_number_1 + self.actual_number_2 + self.number1)
            elif self.oper2 == "-":
                print(self.actual_number_1 + self.actual_number_2 - self.number1)
            elif self.oper2 == "*":
                print(self.actual_number_1 + (self.actual_number_2 * self.number1))
            elif self.oper2 == "/":
                print(self.actual_number_1 + (self.actual_number_2 / self.number1))
        elif self.oper1 == "-":
            if self.oper2 == "+":
                print(self.actual_number_1 - self.actual_number_2 + self.number1)
            elif self.oper2 == "-":
                print(self.actual_number_1 - self.actual_number_2 - self.number1)
            elif self.oper2 == "*":
                print(self.actual_number_1 - self.actual_number_2 * self.number1)
            elif self.oper2 == "/":
                print(self.actual_number_1 - (self.actual_number_2 / self.number1))
        elif self.oper1 == "*":
            if self.oper2 == "+":
                print((self.actual_number_1 * self.actual_number_2) + self.number1)
            elif self.oper2 == "-":
                print((self.actual_number_1 * self.actual_number_2) - self.number1)
            elif self.oper2 == "*":
                print((self.actual_number_1 * self.actual_number_2) * self.number1)
            elif self.oper2 == "/":
                print((self.actual_number_1 * (self.actual_number_2) / self.number1))
        elif self.oper1 == "/":
            if self.oper2 == "+":
                print((self.actual_number_1 / self.actual_number_2) + self.number1)
            elif self.oper2 == "-":
                print((self.actual_number_1 / self.actual_number_2) - self.number1)
            elif self.oper2 == "*":
                print((self.actual_number_1 / self.actual_number_2) * self.number1)
            elif self.oper2 == "/":
                print((self.actual_number_1 / (self.actual_number_2) / self.number1))

    def functionDecider(self):
        """This method checks how many operators have been entered and decides which method to use"""
        if len(self.oper2) == 0:
            self.outputPrinterTwoNumbers()
        elif len(self.oper2) != 0:
            self.outputPrinterThreeNumbers()

    def allMethodCaller(self):
        """This method calls all the other methods"""
        self.readUserInput()
        self.functionDecider()


if __name__ == "__main__":
    print("Please enter input: ")
    x = input()
    calc = Calculator(x)

    calc.allMethodCaller()
    


