import tkinter as tk 
from time import strftime

## DESIGNING THE CLOCK

#root is used to design the framework of the clock we are making 
root=tk.Tk()
root.title("Digital Clock")

# Now comes the labeling part of the clock where each labeling is used to design the clock effectively 
# We are Going to do that by making a function time 

def time() :
    full_label=strftime('%H : %M : %S %p \n %D')
    label.config(text=full_label)
    label.after(1000,time)



# LABELING THE INTERFACE 

label=tk.Label(root,font=('calibri',50,'bold'),background='yellow',foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
