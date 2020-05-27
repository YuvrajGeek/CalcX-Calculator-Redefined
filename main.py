from tkinter import *
from PIL import ImageTk, Image
from winsound import *

root = Tk()
root.title("CalcX - Calculator Redefined")
root.resizable(height = 0, width = 0)
root.iconbitmap('images/icon.ico')
PlaySound('sounds/equaltoclick.wav', SND_FILENAME)


root.configure(bg = 'Light Cyan')
ent = Entry(root, width = 35, borderwidth = 5)
ent.grid(row = 1, column = 0, columnspan = 8 ,pady = 5, padx = 4)

#operation addition - successfully accomplished

one = ImageTk.PhotoImage(Image.open('images/one.png'))
two = ImageTk.PhotoImage(Image.open('images/two.png'))
three = ImageTk.PhotoImage(Image.open('images/three.png'))
four = ImageTk.PhotoImage(Image.open('images/four.png'))
five = ImageTk.PhotoImage(Image.open('images/five.png'))
six = ImageTk.PhotoImage(Image.open('images/six.png'))
seven = ImageTk.PhotoImage(Image.open('images/seven.png'))
eight = ImageTk.PhotoImage(Image.open('images/eight.png'))
nine = ImageTk.PhotoImage(Image.open('images/nine.png'))
zero = ImageTk.PhotoImage(Image.open('images/zero.png'))
equaltosign = ImageTk.PhotoImage(Image.open('images/=.png'))
clear = ImageTk.PhotoImage(Image.open('images/clear.png'))
plus = ImageTk.PhotoImage(Image.open('images/plus.png'))
subtract = ImageTk.PhotoImage(Image.open('images/subtract.png'))
multiply = ImageTk.PhotoImage(Image.open('images/multiply.png'))
divide = ImageTk.PhotoImage(Image.open('images/divide.png'))
symbol = ImageTk.PhotoImage(Image.open('images/symbol.png'))
logo = Label(image = symbol)
logo.grid(row = 0, column = 0, columnspan = 8)

def button_click(number):
	current  = ent.get()
	ent.delete(0, END)
	ent.insert(0, str(current) + str(number))
	PlaySound('sounds/buttonclick.wav', SND_FILENAME)

def button_clear():
	PlaySound('sounds/equaltoclick.wav', SND_FILENAME)

	ent.delete(0, END)

def button_add():
	PlaySound('sounds/signclick.wav', SND_FILENAME)
	first_number = ent.get()
	global f_num
	global math
	math = 'addition'
	f_num = int(first_number)
	ent.delete(0, END)


def button_subtract():
	PlaySound('sounds/signclick.wav', SND_FILENAME)
	first_number = ent.get()
	global f_num
	global math
	math = 'subtraction'
	f_num = int(first_number)
	ent.delete(0, END)

def button_multiply():
	PlaySound('sounds/signclick.wav', SND_FILENAME)
	first_number = ent.get()
	global f_num
	global math
	math = 'multiply'
	f_num = int(first_number)
	ent.delete(0, END)

def button_divide():
	PlaySound('sounds/signclick.wav', SND_FILENAME)	
	first_number = ent.get()
	global f_num
	global math
	math = 'divide'
	f_num = int(first_number)
	ent.delete(0, END)


def button_equal():
	PlaySound('sounds/equaltoclick.wav', SND_FILENAME)
	second_number = ent.get()
	ent.delete(0, END)
	if math == 'addition':
		ent.insert(0, f_num + int(second_number))
	if math == 'subtraction':
		ent.insert(0, f_num - int(second_number))
	if math == 'multiply':
		ent.insert(0, f_num * int(second_number))
	if math == 'divide':
		ent.insert(0, f_num / int(second_number))


#making buttons

button1 = Button(padx = 40, pady = 20,command = lambda: button_click(1), image = one)
button2 = Button(padx = 40, pady = 20,command = lambda: button_click(2), image = two)
button3 = Button(padx = 40, pady = 20,command = lambda: button_click(3), image = three)
button4 = Button(padx = 40, pady = 20,command = lambda: button_click(4), image = four)
button5 = Button(padx = 40, pady = 20,command = lambda: button_click(5), image = five)
button6 = Button(padx = 40, pady = 20,command = lambda: button_click(6), image = six)
button7 = Button(padx = 40, pady = 20,command = lambda: button_click(7), image = seven)
button8 = Button(padx = 40, pady = 20,command  =lambda: button_click(8), image = eight)
button9 = Button(padx = 40, pady = 20,command = lambda: button_click(9), image = nine)
button0 = Button(padx = 40, pady = 20,command = lambda: button_click(0), image = zero)
button_add = Button(padx = 38, pady = 20, command= button_add, fg = 'Red', image = plus)
button_equal = Button(padx = 300, pady = 20, command = button_equal, image = equaltosign)
button_clear= Button(padx =80, pady = 20, command= button_clear, image = clear)
button_subtract =  Button( padx = 40 , pady = 20, command = button_subtract, fg = 'Red', image = subtract)
button_multiply =  Button( padx = 40, pady = 20, command = button_multiply, fg = 'Red', image = multiply)
button_divide =  Button( padx = 40, pady = 20, command = button_divide, fg = 'Red', image = divide)

#getting them on the screen
button7.grid(row =2, column = 0 )
button8.grid(row =2, column = 1)
button9.grid(row =2, column = 2)

button4.grid(row =3, column =0 )
button5.grid(row =3, column = 1)
button6.grid(row =3, column = 2)

button1.grid(row =4, column = 0)
button2.grid(row =4, column = 1)
button3.grid(row =4, column =2 )

button0.grid(row =5, column =0 )
button_clear.grid(row = 5, column = 1, columnspan = 2)

button_add.grid(row = 2, column = 4)
button_subtract.grid(row = 3, column = 4)
button_multiply.grid(row = 4, column = 4)
button_divide.grid(row = 5, column = 4)

button_equal.grid(row =6, column = 0, columnspan = 6)


root.mainloop()
