from currency_converter import CurrencyConverter
import tkinter as tk
c=CurrencyConverter()


window=tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    amount=int(entry.get())
    currency1=entry1.get()
    currency2=entry2.get()
    data=c.convert(amount,currency1,currency2)
    
    label4=tk.Label(window,text=data,font="Times 16 bold").place(x=200,y=300)

label=tk.Label(window,text="Currency Converter",font="Times 20 bold").place(x=120,y=30)
label1=tk.Label(window,text="Enter amount here: ",font ="Times 16 bold").place(x=73,y=100)
entry=tk.Entry(window)
label2=tk.Label(window,text="Enter your currency here: ",font ="Times 16 bold").place(x=27,y=150)
entry1=tk.Entry(window)
label3=tk.Label(window,text="Enter your desired currency: ",font ="Times 16 bold").place(x=10,y=200)
entry2=tk.Entry(window)

button=tk.Button(window,text="Click",font="Times 16 bold",command=clicked).place(x=200,y=250)
entry.place(x=260,y=105)
entry1.place(x=260,y=155)
entry2.place(x=260,y=205)


window.mainloop()

