import tkinter as tk
from functools import partial
currVal="INR"
def store_temp(sel_curr):
        global currVal
        currVal=sel_curr
def call_result(rL1,rL2,inputn):
        curr=inputn.get()
        if(currVal=="INR"):
                u=float(float(curr)*0.014)
                e=float(float(curr)*0.0122)
                rL1.config(text="%f USD"%u)
                rL2.config(text="%f EURO"%e)
        if(currVal=="USD"):
                r=float(float(curr)*71.61)
                e=float(float(curr)*0.873)
                rL1.config(text="%f INR"%r)
                rL2.config(text="%f EURO"%e)

        if(currVal=="EURO"):
                r=float(float(curr)*81.735)
                u=float(float(curr)*1.1455)
                rL1.config(text="%f INR"%r)
                rL2.config(text="%f USD"%u)
        
        return
root=tk.Tk()
root.geometry('400x150+100+200')
root.title('Currency Converter')
root.configure(background='#09A3BA')
root.resizable(width=False,height=False)
numberInput=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text="Enter Currency:",background='#09A3BA',foreground='#FFF')
input_entry=tk.Entry(root,textvariable=numberInput)
input_label.grid(row=0)
input_entry.grid(row=0,column=1)


rLabel=tk.Label(root,text='Result1',background='#09A3BA',foreground='#FFF')
rLabel.grid(row=2,columnspan=4)
rLabe2=tk.Label(root,text='Result2',background='#09A3BA',foreground='#FFF')
rLabe2.grid(row=3,columnspan=4)
call_result=partial(call_result,rLabel,rLabe2,numberInput)
result_button=tk.Button(root,text="Convert",command=call_result,background='#09A3BA',foreground='#FFF')
result_button.grid(row=1,columnspan=4)

dropdownList=["INR","USD","EURO"]
dropdown=tk.OptionMenu(root,var,*dropdownList,command=store_temp)
var.set(dropdownList[0])
dropdown.grid(row=0,column=2)
root.mainloop()
