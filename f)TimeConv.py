import tkinter as tk
from functools import partial
timeVal="Hours"
def store_temp(sel_time):
        global timeVal
        timeVal=sel_time
def call_result(rL1,rL2,inputn):
        time=inputn.get()
        if(timeVal=="Hours"):
                m=float(float(time)*60)
                s=float(float(time)*3600)
                
                rL1.config(text="%f Minutes"%m)
                rL2.config(text="%f Seconds"%s)
        if(timeVal=="Minutes"):
                h=float(float(time)/60)
                s=float(float(time)*60)
                rL1.config(text="%f Hours"%h)
                rL2.config(text="%f Seconds"%s)

        if(timeVal=="Seconds"):
                m=float(float(time)/60)
                h=float(float(time)/3600)
                rL1.config(text="%f Minutes"%m)
                rL2.config(text="%f Hours"%h)
        return
root=tk.Tk()
root.geometry('400x150+100+200')
root.title('Time Converter')
root.configure(background='#09A3BA')
root.resizable(width=False,height=False)
numberInput=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text="Enter Time:",background='#09A3BA',foreground='#FFF')
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

dropdownList=["Hours","Minutes","Seconds"]
dropdown=tk.OptionMenu(root,var,*dropdownList,command=store_temp)
var.set(dropdownList[0])
dropdown.grid(row=0,column=2)
root.mainloop()
