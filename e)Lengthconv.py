import tkinter as tk
from functools import partial
lengVal="Kilometre"
def store_temp(sel_leng):
        global lengVal
        lengVal=sel_leng
def call_result(rL1,rL2,inputn):
        leng=inputn.get()
        if(lengVal=="Kilometre"):
                m=float(float(leng)*1000)
                f=float(float(leng)*3280.8399)
                rL1.config(text="%f Metre"%m)
                rL2.config(text="%f Foot"%f)
        if(lengVal=="Metre"):
                km=float(float(leng)/1000)
                f=float((float(leng)*3.2808399))
                rL1.config(text="%f Kilometre"%km)
                rL2.config(text="%f Foot"%f)

        if(lengVal=="Foot"):
                m=float(float(leng)*0.3048)
                km=float(float(leng)*0.0003048)
                rL1.config(text="%f Metre"%m)
                rL2.config(text="%f Kilometre"%km)
        return
root=tk.Tk()
root.geometry('400x150+100+200')
root.title('Length Converter')
root.configure(background='#09A3BA')
root.resizable(width=False,height=False)
numberInput=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text="Enter Length:",background='#09A3BA',foreground='#FFF')
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

dropdownList=["Kilometre","Metre","Foot"]
dropdown=tk.OptionMenu(root,var,*dropdownList,command=store_temp)
var.set(dropdownList[0])
dropdown.grid(row=0,column=2)
root.mainloop()
