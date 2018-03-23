from math import sqrt
from math import factorial as fact
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
        self.lastExpression = ""
        self.lastExpression += value
        return value

    def clear(self):
        self.expression = ""
        self.lastExpression = ""

    def sqr(self):
        length = len(self.expression)

        if length == 0:
            return ""

        lastSymbol = self.expression[length - 1:]
        if self.lastExpression == "" and lastSymbol != ")":
            return ""

        if lastSymbol == ")":
            valueWithBrackets = self.searchStringWithBrackets(self.expression)
            if valueWithBrackets == "":
                return ""
            self.lastExpression = valueWithBrackets

        lastLength = len(self.lastExpression)
        self.expression = self.expression[:-1*lastLength]
        self.lastExpression = self.expression + ("(" + self.lastExpression + "*" + self.lastExpression + ")")
        self.expression = self.lastExpression

        return self.expression


    def searchStringWithBrackets(self, value):
        result = ""
        openedBracket = 0
        closedBracket = 0
        for item in value[::-1]:
            if item == ")":
                closedBracket += 1
            elif item == "(":
                openedBracket += 1

            result = item + result

            if closedBracket == openedBracket and closedBracket > 0:
                return result

        return ""