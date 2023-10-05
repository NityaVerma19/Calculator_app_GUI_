from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)   #to fix the size
root.configure(background='#744972')

#geometry manager
result_label = Label(root,
                     text = 0,
                     bg = '#744972',
                     fg = 'black',
                     width=47)
result_label.grid(row=0,column = 0,pady = (10,25))
result_label.configure(font=('young serif',15))
root.mainloop()