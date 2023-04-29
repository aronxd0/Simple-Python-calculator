from tkinter import *

calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ''
        text_result.delete(1.0,'end')
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0,'Error')

def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0,'end')

root = Tk()
root.geometry('300x275')

text_result = Text(root,height=2,width=16,font=('Arial',24))
text_result.grid(columnspan=5)

#lambda nélkül egyből meghívná
gomb1 = Button(root,text='1',command=lambda:add_to_calculation(1),width=5,font=('Arial',15))
gomb1.grid(row=2,column=1) 

gomb2 = Button(root,text='2',command=lambda:add_to_calculation(2),width=5,font=('Arial',15))
gomb2.grid(row=2,column=2)

gomb3 = Button(root,text='3',command=lambda:add_to_calculation(3),width=5,font=('Arial',15))
gomb3.grid(row=2,column=3)

gomb4 = Button(root,text='4',command=lambda:add_to_calculation(4),width=5,font=('Arial',15))
gomb4.grid(row=3,column=1)

gomb5 = Button(root,text='5',command=lambda:add_to_calculation(5),width=5,font=('Arial',15))
gomb5.grid(row=3,column=2)

gomb6 = Button(root,text='6',command=lambda:add_to_calculation(6),width=5,font=('Arial',15))
gomb6.grid(row=3,column=3)

gomb7 = Button(root,text='7',command=lambda:add_to_calculation(7),width=5,font=('Arial',15))
gomb7.grid(row=4,column=1)

gomb8 = Button(root,text='8',command=lambda:add_to_calculation(8),width=5,font=('Arial',15))
gomb8.grid(row=4,column=2)

gomb9 = Button(root,text='9',command=lambda:add_to_calculation(9),width=5,font=('Arial',15))
gomb9.grid(row=4,column=3)

gomb0 = Button(root,text='0',command=lambda:add_to_calculation(0),width=5,font=('Arial',15))
gomb0.grid(row=5,column=2)

gomb_plusz = Button(root,text='+',command=lambda:add_to_calculation('+'),width=5,font=('Arial',15))
gomb_plusz.grid(row=2,column=4)

gomb_kiv = Button(root,text='-',command=lambda:add_to_calculation('-'),width=5,font=('Arial',15))
gomb_kiv.grid(row=3,column=4)

gomb_szor = Button(root,text='*',command=lambda:add_to_calculation('*'),width=5,font=('Arial',15))
gomb_szor.grid(row=4,column=4)

gomb_oszt = Button(root,text='/',command=lambda:add_to_calculation('/'),width=5,font=('Arial',15))
gomb_oszt.grid(row=5,column=4)

gomb_zaro1 = Button(root,text='(',command=lambda:add_to_calculation('('),width=5,font=('Arial',15))
gomb_zaro1.grid(row=5,column=1)

gomb_zaro2 = Button(root,text=')',command=lambda:add_to_calculation(')'),width=5,font=('Arial',15))
gomb_zaro2.grid(row=5,column=3)

gomb_egyenlo = Button(root,text='=',command=evaluate_calculation,width=11,font=('Arial',15))
gomb_egyenlo.grid(row=6,column=3,columnspan=2)

gomb_torol = Button(root,text='C',command=clear_field,width=11,font=('Arial',15))
gomb_torol.grid(row=6,column=1,columnspan=2)






root.mainloop()