import tkinter as tk
from functools import partial
voluVal="Litre"
def store_temp(sel_volu):
        global voluVal
        voluVal=sel_volu
def call_result(rL1,rL2,inputn):
        volu=inputn.get()
        if(voluVal=="Litre"):
                ccm=float(float(volu)*1000)
                cm=float(float(volu)/1000)
                rL1.config(text="%f Cubic centimetre"%ccm)
                rL2.config(text="%f Cubic metre"%cm)
        if(voluVal=="Cubic centimetre"):
                l=float(float(volu)/1000)
                cm=float(float(volu)/1000000)
                rL1.config(text="%f Litre"%l)
                rL2.config(text="%f Cubic metre"%cm)

        if(voluVal=="Cubic metre"):
                l=float(float(volu)*1000)
                ccm=float(float(volu)*1000000)
                rL1.config(text="%f Litre"%l)
                rL2.config(text="%f Cubic centimetre"%ccm)
        return
root=tk.Tk()
root.geometry('400x150+100+200')
root.title('Volume Converter')
root.configure(background='#09A3BA')
root.resizable(width=False,height=False)
numberInput=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text="Enter Volume:",background='#09A3BA',foreground='#FFF')
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

dropdownList=["Litre","Cubic centimetre","Cubic metre"]
dropdown=tk.OptionMenu(root,var,*dropdownList,command=store_temp)
var.set(dropdownList[0])
dropdown.grid(row=0,column=2)
root.mainloop()
