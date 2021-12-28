"""Since we are directly updating the class variables throught the class method
   we can use ONLY ONE Object ONLY ONCE. Therefore, it is not recommended to use."""

class Calculator():
    """This is the calculator class. It contains all the methods."""
    num1 = ""
    oper1 = ""
    actual_num_1 = ""
    number1 = 0
    actual_number_1 = 0 

    def __init__(self,x):
        self.x = x

    def readUserInput(self):
        """This method reads the string entered by the user and seperates numbers and operators"""
        
        for i in range(len(self.x)):
            if self.x[i].isnumeric():
                Calculator.num1 += self.x[i]
            else:
                Calculator.oper1 = self.x[i]
                Calculator.actual_num_1 = Calculator.num1
                Calculator.num1 = ""

    def outputPrinterTwoNumbers(self):
        """This method calculates and prints the output for two numbers"""
        
        Calculator.actual_number_1 = int(Calculator.actual_num_1)
        Calculator.number1 = int(Calculator.num1)

        if Calculator.oper1 == "+":
            print(Calculator.actual_number_1 + Calculator.number1)
        elif Calculator.oper1 == "-":
            print(Calculator.actual_number_1 - Calculator.number1)
        elif Calculator.oper1 == "*":
            print(Calculator.actual_number_1 * Calculator.number1)
        elif Calculator.oper1 == "/":
            print(Calculator.actual_number_1 / Calculator.number1)

if __name__ == "__main__":
    print("Please enter input: ")
    x = input()
    calc = Calculator(x)

    # y = input()
    # calc_2 = Calculator(y)

    calc.readUserInput()
    calc.outputPrinterTwoNumbers()

    print("Printing class variables through object calc")
    print(calc.num1)
    print(calc.number1)
    print(calc.actual_num_1)
    print(calc.actual_number_1)
    print(calc.oper1)
    print("\n")

    print("Printing class variables through class name")
    print(Calculator.num1)
    print(Calculator.number1)
    print(Calculator.actual_num_1)
    print(Calculator.actual_number_1)
    print(Calculator.oper1)
    print("\n")

    # calc_2.readUserInput()
    # calc_2.outputPrinterTwoNumbers()

    # print("Printing class variables through object calc_2")
    # print(calc_2.num1)
    # print(calc_2.number1)
    # print(calc_2.actual_num_1)
    # print(calc_2.actual_number_1)
    # print(calc_2.oper1)
    # print("\n")

    # print("Printing class variables through class name once again")
    # print(Calculator.num1)
    # print(Calculator.number1)
    # print(Calculator.actual_num_1)
    # print(Calculator.actual_number_1)
    # print(Calculator.oper1)
    # print("\n")