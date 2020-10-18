import tkinter as tk
from functools import partial
massVal="Kilogram"
def store_temp(sel_mass):
        global massVal
        massVal=sel_mass
def call_result(rL1,rL2,inputn):
        mass=inputn.get()
        if(massVal=="Kilogram"):
                g=float(float(mass)*1000)
                p=float(float(mass)*2.20462262)
                rL1.config(text="%f Gram"%g)
                rL2.config(text="%f Pound"%p)
        if(massVal=="Gram"):
                kg=float(float(mass)/1000)
                p=float((float(mass)*0.00220462262))
                rL1.config(text="%f Kilogram"%kg)
                rL2.config(text="%f Pound"%p)

        if(massVal=="Pound"):
                kg=float(float(mass)*0.45359237)
                g=float(float(mass)*453.59237)
                rL1.config(text="%f Kilogram"%kg)
                rL2.config(text="%f Gram"%g)
        return
root=tk.Tk()
root.geometry('400x150+100+200')
root.title('Mass Converter')
root.configure(background='#09A3BA')
root.resizable(width=False,height=False)
numberInput=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text="Enter Mass:",background='#09A3BA',foreground='#FFF')
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

dropdownList=["Kilogram","Gram","Pound"]
dropdown=tk.OptionMenu(root,var,*dropdownList,command=store_temp)
var.set(dropdownList[0])
dropdown.grid(row=0,column=2)
root.mainloop()
