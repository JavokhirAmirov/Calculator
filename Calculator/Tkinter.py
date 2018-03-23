from tkinter import *
from calculator import CalcProcessor

isNewOperation = True

calcProcessor = CalcProcessor("")

top = Tk()
top.geometry("350x350")
top.title('Calculator')

top.resizable(False, False)

resultText = Text(top, height=13, width=50)

resultText.pack()


def clear():
    calcProcessor.clear()
    resultText.delete('1.0', END)


def addDigit(value):
    global isNewOperation
    if not isNewOperation:
        clear()
        isNewOperation = True

    calcProcessor.typeDigitOrPoint(value)
    resultText.insert(END, value)


def addSymbol(value):
    global isNewOperation
    if not isNewOperation:
        isNewOperation = True

    calcProcessor.typeSymbol(value)
    resultText.insert(END, value)


def addPoint():
    global isNewOperation
    if not isNewOperation:
        isNewOperation = True

    value = "."
    calcProcessor.typeDigitOrPoint(value)
    resultText.insert(END, value)


def createButton(textValue, commandName, xValue, yValue, widthValue="3", heightValue="1"):
    button = Button(top, text=textValue, command=commandName, width=widthValue, height=heightValue)
    button.place(x=xValue, y=yValue)


def createStyleButton(textValue, commandName, xValue, yValue, background, foreground, widthValue="3", heightValue="1"):
    button = Button(top, text=textValue, command=commandName, width=widthValue, height=heightValue, bg=background, fg=foreground)
    button.place(x=xValue, y=yValue)


def TypeEqual():
    global isNewOperation
    value = calcProcessor.calculate()
    resultText.delete('1.0', END)
    resultText.insert(END, value)
    isNewOperation = False


def TypeSqr():
    value = calcProcessor.sqr()
    if value != "":
        resultText.insert(END, "²")


createButton("0", lambda: addDigit("0"), 10, 315, "10", "1")

createButton("1", lambda: addDigit("1"), 10, 285)

createButton("2", lambda: addDigit("2"), 65, 285)

createButton("3", lambda: addDigit("3"), 120, 285)

createButton("4", lambda: addDigit("4"), 10, 255)

createButton("5", lambda: addDigit("5"), 65, 255)

createButton("6", lambda: addDigit("6"), 120, 255)

createButton("7", lambda: addDigit("7"), 10, 225)

createButton("8", lambda: addDigit("8"), 65, 225)

createButton("9", lambda: addDigit("9"), 120, 225)

createButton(".", lambda: addPoint(), 120, 315)

createButton("x²", TypeSqr, 295, 285)

createButton("√", lambda: addSymbol("sqrt("), 240, 285)

createButton("!", lambda: addSymbol("fact("), 240, 225)

createButton("*", lambda: addSymbol("*"), 180, 225)

createButton("/", lambda: addSymbol("/"), 180, 255)

createButton("-", lambda: addSymbol("-"), 180, 285)

createButton("+", lambda: addSymbol("+"), 180, 315)

createButton("(", lambda: addSymbol("("), 240, 255)

createButton(")", lambda: addSymbol(")"), 295, 255)

createButton("C", lambda: clear(), 295, 225)

createStyleButton("=", TypeEqual, 240, 315, "blue", "white", "10", "1")

createButton("π", lambda: addSymbol("π"), 10, 195)

createButton("e", lambda: addSymbol("e"), 65, 195)

createButton("sin", lambda: addSymbol("sin("), 120, 195)

createButton("cos", lambda: addSymbol("cos("), 180, 195)

createButton("ln", lambda: addSymbol("ln("), 240, 195)

createButton("log", lambda: addSymbol("log("), 295, 195)

top.mainloop()
