from tkinter import *
from calculator import CalcProcessor

isNewOperation = True

calcProcessor = CalcProcessor("")

top = Tk()
top.geometry("350x350")
top.title('Calculate')

top.resizable(False, False)

resultText = Text(top, height=15, width=50)
#resultText.config(state=DISABLED)
resultText.pack()
#T.insert(END, "")

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

def addPoint(value):
    global isNewOperation
    if not isNewOperation:
        isNewOperation = True

    calcProcessor.typeDigitOrPoint(value)
    resultText.insert(END, value)

def Type0():
    addDigit("0")

button_0 = Button(top, text = "         0         ", command = Type0)
button_0.place(x = 10, y = 315)


def Type1():
    addDigit("1")

button_1 = Button(top, text = "  1  ", command = Type1)
button_1.place(x = 10, y = 285)


def Type2():
    addDigit("2")

button_2 = Button(top, text = "  2  ", command = Type2)
button_2.place(x = 65, y = 285)

def Type3():
    addDigit("3")

button_3 = Button(top, text = "  3  ", command = Type3)
button_3.place(x = 120, y = 285)

def Type4():
    addDigit("4")

button_4 = Button(top, text = "  4  ", command = Type4)
button_4.place(x = 10, y = 255)

def Type5():
    addDigit("5")

button_5 = Button(top, text = "  5  ", command = Type5)
button_5.place(x = 65, y = 255)

def Type6():
    addDigit("6")

button_6 = Button(top, text = "  6  ", command = Type6)
button_6.place(x = 120, y = 255)

def Type7():
    addDigit("7")

button_7 = Button(top, text = "  7  ", command = Type7)
button_7.place(x = 10, y = 225)

def Type8():
    addDigit("8")

button_8 = Button(top, text = "  8  ", command = Type8)
button_8.place(x = 65, y = 225)

def Type9():
    addDigit("9")

button_9 = Button(top, text = "  9  ", command = Type9)
button_9.place(x = 120, y = 225)


def TypeDelimeter():
    addPoint(".")

buttonDelimeter = Button(top, text = "   ,  ", command = TypeDelimeter)
buttonDelimeter.place(x = 120, y = 315)


def TypeSqr():
    value = calcProcessor.sqr()
    if value != "":
        resultText.insert(END, "²")

buttonSqr = Button(top, text = "  x² ", command = TypeSqr)
buttonSqr.place(x = 295, y = 285)


def TypeSqrt():
    addSymbol("sqrt(")

buttonSqrt = Button(top, text = "  √  ", command = TypeSqrt)
buttonSqrt.place(x = 240, y = 285)


def TypeMultipy():
    addSymbol("*")

buttonMultiply = Button(top, text = "  *  ", command = TypeMultipy)
buttonMultiply.place(x = 180, y = 225)


def TypeDivision():
    addSymbol("/")

buttonDivision = Button(top, text = "   /  ", command = TypeDivision)
buttonDivision.place(x = 180, y = 255)


def TypeMinus():
    addSymbol("-")

buttonMinus = Button(top, text = "   -  ", command = TypeMinus)
buttonMinus.place(x = 180, y = 285)


def TypePlus():
    addSymbol("+")


def TypeOpen():
    addSymbol("(")

buttonOpen = Button(top, text = "  (  ", command = TypeOpen)
buttonOpen.place(x = 240, y = 255)


def TypeClose():
    addSymbol(")")

buttonClose = Button(top, text = "  )  ", command = TypeClose)
buttonClose.place(x = 295, y = 255)



buttonPlus = Button(top, text = "  +  ", command = TypePlus)
buttonPlus.place(x = 180, y = 315)


def TypeClear():
    clear()


buttonClear = Button(top, text = "  C  ", command = TypeClear)
buttonClear.place(x = 295, y = 225)


def TypeEqual():
    global isNewOperation
    value = calcProcessor.calculate()
    resultText.delete('1.0', END)
    resultText.insert(END, value)
    isNewOperation = False

buttonEqual = Button(top, text = "         =        ", command = TypeEqual, bg = "blue", fg = "white")
buttonEqual.place(x = 240, y = 315)


top.mainloop()