

#Nawa Project : Currency Conversion
#GUI Based Project

import tkinter as tk
from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

root = tk.Tk() 

root.title("GUI : Currency Conversion")

Tops = Frame(root,bg = '#00504E',pady = 2, width =1850, height = 100, relief = "ridge")
Tops.grid(row=0,column=0)

headlabel = tk.Label(Tops,font=('times', 24,'bold'), text = '      Nawa Project   :    Currency Converter  ', bg= '#FFF7E2',fg='black') 
headlabel.grid(row=1, column=0,sticky=W)

variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 

variable1.set("currency") 
variable2.set("currency") 

image = None

def RealTimeCurrencyConversion():
    global image
    from forex_python.converter import CurrencyRates     
    c = CurrencyRates()

    from_currency = variable1.get() 
    to_currency = variable2.get()

    if (Amount1_field.get()==""):
        tkinter.messagebox.showinfo("Error !!","Amount Not Entered.\n Please a valid amount.")

    elif (from_currency=="currency" or to_currency=="currency"):
        tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = c.convert(from_currency,to_currency,float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))
        sel = c.convert(from_currency, to_currency, 1)
        x = [x+1 for x in range(10)]
        y = [(x+1)*sel for x in range(10)]
        plt.bar(x, y)
        plt.xlabel(from_currency)
        plt.ylabel(to_currency)
        plt.title(f"Current Rates From {from_currency} to {to_currency}")
        plt.show()
        plt.savefig("image.jpg")
        if image:
            image.destroy()
        img = ImageTk.PhotoImage(Image.open("image.jpg"))
        image = Label(root, image = img)
        image.grid(row=11, column=0)

def clear_all() : 
	Amount1_field.delete(0, tk.END) 
	Amount2_field.delete(0, tk.END)


CurrenyCode_list = ["IDR", "USD","BGN", "ILS","GBP","DKK","CAD","JPY","HUF","RON","MYR","SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "EUR", "NOK", "RUB", "INR", "MXN", "CZK", "BRR", "PLN"]


root.configure(background = '#00504E') 
root.geometry("700x400") 

Label_1 =Label(root, font=('lato black', 27,'bold'), text="",padx=2,pady=2, bg="#00504E",fg ="black")
Label_1.grid(row=1, column=0,sticky=W)


label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    Amount  :  ", bg="#00504E",fg = "white") 
label1.grid(row=2, column=0,sticky=W)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    From Currency  :  ", bg="#00504E",fg = "white") 
label1.grid(row=3, column=0,sticky=W)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    To Currency  :  ", bg="#00504E",fg = "white") 
label1.grid(row=4, column=0,sticky=W)

label1 = tk.Label(root,font=('lato black', 15,'bold'), text = "\t    Converted Amount  :  ", bg="#00504E",fg = "white") 
label1.grid(row=8, column=0,sticky=W)


Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#00504E",fg ="black")
Label_1.grid(row=5, column=0,sticky=W)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#00504E",fg ="black")
Label_1.grid(row=7, column=0,sticky=W)



FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list) 
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list) 

FromCurrency_option.grid(row = 3, column = 0, ipadx = 45,sticky=E) 
ToCurrency_option.grid(row = 4, column = 0, ipadx = 45,sticky=E) 




Amount1_field = tk.Entry(root) 
Amount1_field.grid(row=2,column=0,ipadx =28,sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8,column=0,ipadx =31,sticky=E) 




Label_9 =Button(root, font=('consolas', 15,'bold'), text="   Convert  ",padx=2,pady=2, bg="lightblue",fg = "blue",command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#00504E",fg ="black")
Label_1.grid(row=9, column=0,sticky=W)

Label_9 =Button(root, font=('consolas', 15,'bold'), text="   Clear All  ",padx=2,pady=2, bg="lightblue",fg = "red",command=clear_all)
Label_9.grid(row=10, column=0)


root.mainloop()