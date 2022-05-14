from Recursion_Gui import *
from PyQt5.QtWidgets import *
import easygui as e

class Recursion_Controls(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.btnCalculate1.clicked.connect(lambda: self.mastercontrol(str(one), self.txtHighest.text(), self.txtLowest.text()))
        self.btnCalculate2.clicked.connect(lambda: self.mastercontrol(str(two), self.txtBase.text(), self.txtN.text()))
        self.btnDisplay.clicked.connect(lambda: self.mastercontrol(str(three), self.txtTop.text(), self.txtBottom.text()))

    def mastercontrol(self, method_checker, first_value, second_value):
        if method_checker == "one":
            self.lblresult1.setText("Total sum: " + one(int(first_value), int(second_value)))
            self.txtHighest.setText("")
            self.txtLowest.setText("")
        elif method_checker == "two":
            self.lblResult2.setText("Final result: " + two(int(first_value), int(second_value)))
            self.txtBase.setText("")
            self.txtN.setText("")
        else:
            self.lblResult3.setText("Counting: " + three(int(first_value), int(second_value)))
            self.txtTop.setText("")
            self.txtBottom.setText("")

    def one(self, n, stop):
        if type(n) != int or type(stop) != int:
            self.txtHighest.setText("")
            self.txtLowest.setText("")
            e.msgbox("Error: please ensure both values are integers", "TypeError")
            #ensures it's not any type of value besides int
            #raises TypeError("Both values must be integers")
        if n < stop:
            self.txtHighest.setText("")
            self.txtLowest.setText("")
            e.msgbox("Error: please ensure the Highest value is bigger than the Lowest value", "ValueError")
            #ensures it doesn't loop infinitely
            #raise ValueError("Only positive distances are allowed between Highest and Lowest")
        else:
            if n == 1:
                return 1 #stops the recursion before n becomes 0 or negative
            else:
                return n + one(n-1) #adds the current value of n to all values lower that it recursively


    def two(self, num, pow):
        if type(num) != int or type(pow) != int:
            self.txtBase.setText("")
            self.txtN.setText("")
            e.msgbox("Error: please ensure all values being input into the formula are integers", "TypeError")
            #ensures it's not any type of value besides int for either value
            #raise ValueError("Exponent must not be a negative number")
        elif pow <= 0:
            self.txtBase.setText("")
            self.txtN.setText("")
            e.msgbox("Error: please ensure the exponent is not a negative value", "ValueError")
            #ensures it's not any negative or 0 value for pow (so long as num is an int, all outputs are safe for the code
            #raise ValueError("Positive inputs only for power")
        else:
            if pow == 1:
                return num #stops the recursion before pow becomes 0 or negative
            else:
                return num * two(num, pow - 1) #multiplies num by itself power times


    def three(self, n, stop):
        if type(n) != int or type(stop) != int:
            self.txtTop.setText("")
            self.txtBottom.setText("")
            e.msgbox("Error: Please input only integer values for both the Top and Bottom values", "TypeError")
            # ensures it's not any type of value besides int
            #raise TypeError("Integer inputs only, both the starting and stopping point")
        if n < stop:
            self.txtTop.setText("")
            self.txtBottom.setText("")
            e.msgbox("Error: Please keep a positive distance between Top and Bottom (Top > Bottom)", "ValueError")
            # ensures it doesn't loop infinitely
            #raise ValueError("Top value must be larger than the bottom")
        else:
            if n > stop:
                return str(n) + " " + three(n-1) #puts the largest number infront and recursively gets the next smallest number after
            else:
                return str(stop) #stops the program from going infinitely
