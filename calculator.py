from math import sqrt
from math import pow



class CalcProcessor(object):
    def __init__(self, expression="", lastExpression=""):
        self.expression = expression
        self.lastExpression = lastExpression

    def typeSymbol(self, value):
        self.expression += value
        self.lastExpression = ""

    def typeDigitOrPoint(self, value):
        self.expression += value

        if self.lastExpression == "":
            self.lastExpression = value
        else:
            self.lastExpression += value

    def calculate(self):
        value = str(eval(self.expression))
        self.expression = ""
        self.expression += value
        self.lastExpression = value
        return value

    def clear(self):
        self.expression = ""
        self.lastExpression = ""

    def sqr(self):
        if self.lastExpression == "":
            return ""

        length = len(self.lastExpression)
        self.expression = self.expression[:-1*length]
        self.lastExpression = self.expression + ("(" + self.lastExpression + "*" + self.lastExpression + ")")
        self.expression = self.lastExpression
        return self.expression






