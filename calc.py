from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('270x410')
root.resizable(0,0)   #to fix the size
root.configure(background='#282828')

#geometry manager
result_label = Label(root,
                     text = 0,
                     bg ='#282828',
                     fg = '#FBEAEB',
                     )
result_label.grid(row=0,column = 0,pady = (30,35))
result_label.configure(font=('young serif',15))

btnC= Button(root, text = 'C', bg = '#D47970', fg= 'white', width = 4,height = 2)
btnC.grid(row = 1, column = 0)
btnC.config(font=('young serif',15))

btnbrac =  Button(root, text = '()', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnbrac.grid(row =1, column =1 )
btnbrac.config(font=('young serif',15))

btnroot =  Button(root, text = '√', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnroot.grid(row = 2, column = 0)
btnroot.config(font=('young serif',15))

btn7= Button(root, text = '7', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn7.grid(row = 2, column = 1)
btn7.config(font=('young serif',15))


btn8 = Button(root, text = '8', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn8.grid(row = 2, column = 2)
btn8.config(font=('young serif',15))

btn9 = Button(root, text = '9', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn9.grid(row = 2, column = 3)
btn9.config(font=('young serif',15))

btnsum = Button(root, text = '+', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnsum.grid(row = 2, column = 4)
btnsum.config(font=('young serif',15))

btnsq =  Button(root, text = 'x²', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnsq.grid(row = 3, column = 0)
btnsq.config(font=('young serif',15))

btn4 = Button(root, text = '4', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn4.grid(row = 3, column =1 )
btn4.config(font=('young serif',15))

btn5 = Button(root, text = '5', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn5.grid(row = 3, column = 2)
btn5.config(font=('young serif',15))

btn6 = Button(root, text = '6', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn6.grid(row = 3, column = 3)
btn6.config(font=('young serif',15))

btnmin = Button(root, text = '-', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnmin.grid(row =3, column = 4)
btnmin.config(font=('young serif',15))

btnfact =  Button(root, text = '!', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnfact.grid(row = 4, column = 0)
btnfact.config(font=('young serif',15))

btn1 = Button(root, text = '1', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn1.grid(row = 4, column = 1)
btn1.config(font=('young serif',15))

btn2 = Button(root, text = '2', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn2.grid(row = 4, column = 2)
btn2.config(font=('young serif',15))

btn3 = Button(root, text = '3', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn3.grid(row = 4, column = 3)
btn3.config(font=('young serif',15))

btndiv = Button(root, text = '÷', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btndiv.grid(row =4, column =4 )
btndiv.config(font=('young serif',15))

btn0 =  Button(root, text = '0', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btn0.grid(row =5, column =0 )
btn0.config(font=('young serif',15))

btndec =  Button(root, text = '.', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btndec.grid(row =5, column =1 )
btndec.config(font=('young serif',15))

btnln =  Button(root, text = 'ln', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnln.grid(row =5, column = 2)
btnln.config(font=('young serif',15))

btnexp =  Button(root, text = 'e', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btnexp.grid(row =5, column = 3)
btnexp.config(font=('young serif',15))

btneq =  Button(root, text = '=', bg = '#D47970', fg= 'white', width = 4,height = 2,justify = 'center')
btneq.grid(row =5, column = 4)
btneq.config(font=('young serif',15))
root.mainloop()

