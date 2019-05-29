__author__ = '_aiben.stunner'

""" GUI """

from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Number to Text Converter")
root.minsize(width=500, height=100)


#WordFill_

oneTeens = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "sixteen", "seventeen", "eighteen", "nineteen")
tens = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
googolChunk = ("hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion", "octodecillion", "novemdecillion", "vigintillion", "unvigintillion", "duovigintillion", "trevigintillion", "quattuorvigintillion", "quinvigintillion", "sexvigintillion", "septenvigintillion", "octovigintillion", "novemvigintillion", "trigintillion", "untrigintillion", "duotrigintillion")

"""___playGround"""
def start(event=None):
    global enterEntry
    number = enterEntry.get()
    global text
    try:
        clear = "                                                                                                                                                                                                                                     "
        text = number + " : " + convert_toText(number)
        textLabel = Label(frame, text=" ")
        textLabel.grid(row=7, column=1)


        textLabel = Label(frame, text=clear)
        textLabel.grid(row=6, column=1)
        textLabel = Label(frame, text=text)
        textLabel.grid(row=6, column=1)
    except:
        error = "-------:(-------\n" + "Invalid Input!!!\n" + "-------:(-------\n" + "Enter a decimal number. For example 12345\n" + "\nMaximum number is 10^100(googol)\n"
        tkinter.messagebox.showinfo("Number to Text Converter", error)



def convert_toText(number):
    if int(number) == 0:
        return "zero"
    elif int(number) == 10 ** 100:
        return "googol"
    text = ""
    flag = number.startswith("-")
    if flag == 1:
        text += "negative "
        number = number.strip("-")

    i = 0
    while i < len(number):
        n = (len(number) - i) % 3
        if n == 0:
            n = 3

        #forHundreds
        if n == 3:
            if int(number[i]) != 0:
                text += oneTeens[int(number[i])] + " " + googolChunk[0] + " "

                n -= 1
                i += 1

        #forTens
        if n == 2:
            if int(number[i]) == 1:
                if int(number[i]) != 0:
                    text += oneTeens[int(number[i] + number[i + 1])] + " "

                n -= 2
                i += 2
            else:
                if int(number[i]) != 0:
                    text += tens[int(number[i]) - 2] + " "

                n -= 1
                i += 1

        #forOnes
        if n == 1:
            if int(number[i]) != 0:
                text += oneTeens[int(number[i])] + " "

            i += 1

        #for_googolChunk
        if len(number) - i != 0:
            if int(number[i]) != 0 or i <= 3:
                text += googolChunk[int((len(number) - i) / 3)] + " "

    return text


"""___main."""

frame = Frame(root, height=300, width=500)
frame.pack()

enterLabel = Label(frame, text="Enter your number:")
enterEntry = Entry(frame)

enterLabel.grid(row=1, column=1)
enterEntry.grid(row=2, column=1)
enterEntry.focus_set()


convertButton = Button(frame, text="Convert", command=start)
convertButton.grid(row=4, column=1)


menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=frame.quit)
helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="@_aiben.stunner")

root.bind('<Return>', start)

root.mainloop()
