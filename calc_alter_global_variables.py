"""This method should not be used as we are directly updating the global variables.
   Therefor more that one object may create an issue."""

num1 = ""
oper1 = ""
actual_num_1 = ""
number1 = 0
actual_number_1 = 0 

class Calculator():
    """This is the calculator class. It contains all the methods."""
    def __init__(self,x):
        self.x = x

    def readUserInput(self):
        """This method reads the string entered by the user and seperates numbers and operators"""
        global num1, oper1, actual_num_1
        for i in range(len(self.x)):
            if self.x[i].isnumeric():
                num1 += self.x[i]
            else:
                oper1 = self.x[i]
                actual_num_1 = num1
                num1 = ""

    def outputPrinterTwoNumbers(self):
        """This method calculates and prints the output for two numbers"""
        global num1, oper1, actual_num_1
        actual_number_1 = int(actual_num_1)
        number1 = int(num1)

        if oper1 == "+":
            print(actual_number_1 + number1)
        elif oper1 == "-":
            print(actual_number_1 - number1)
        elif oper1 == "*":
            print(actual_number_1 * number1)
        elif oper1 == "/":
            print(actual_number_1 / number1)

if __name__ == "__main__":
    print("Please enter input: ")
    x = input()
    calc = Calculator(x)

    calc.readUserInput()
    calc.outputPrinterTwoNumbers()
    print(num1)
    print(number1)
    print(actual_num_1)
    print(actual_number_1)
    print(oper1)
    print("\n")

    print("Please give input: ")
    y = input()
    calc_2 = Calculator(y)

    calc_2.readUserInput
    calc_2.outputPrinterTwoNumbers()
    print(num1)
    print(number1)
    print(actual_num_1)
    print(actual_number_1)
    print(oper1)
    print("\n")