import tkinter as tk
from functools import partial
tempVal="Celsius"
def store_temp(sel_temp):
        global tempVal
        tempVal=sel_temp
        
def call_result(rL1,rL2,inputn):
        temp=inputn.get()
        if(tempVal=="Celsius"):
                f=float((float(temp)*9/5)+32)
                k=float(float(temp)+273.15)
                rL1.config(text="%f Fahrenheit"%f)
                rL2.config(text="%f Kelvin"%k)
        if(tempVal=="Fahrenheit"):
                c=float((float(temp)-32)*5/9)
                k=c+273.15
                rL1.config(text="%f Celsius"%c)
                rL2.config(text="%f Kelvin"%k)

        if(tempVal=="Kelvin"):
                c=float(float(temp)-273.15)
                f=float((float(temp)-273.15)*1.8000+32.000)
                rL1.config(text="%f Celsius"%c)
                rL2.config(text="%f Fahrenheit"%f)
        return
root=tk.Tk()
root.geometry('400x150+100+200')
root.title('Temperature Converter')
root.configure(background='#09A3BA')
root.resizable(width=False,height=False)
numberInput=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text="Enter Temperature:",background='#09A3BA',foreground='#FFF')
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

dropdownList=["Celsius","Fahrenheit","Kelvin"]
dropdown=tk.OptionMenu(root,var,*dropdownList,command=store_temp)
var.set(dropdownList[0])
dropdown.grid(row=0,column=2)
root.mainloop()
