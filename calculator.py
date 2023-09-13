import tkinter as tk
import math as math

root =tk.Tk()
root.title("Calculator")
root.geometry("600x500")

text_area=tk.Text(root, font="55", height=5, width=65 , state="disabled")
text_area.place(x=10 , y=10)

frame=tk.Frame(root, width=400 , height=300 , bg="#F0F0F0")
frame.place(x=10 , y=110)

value=['7', '8' , '9', 'c' , '<-','4', '5' , '6', '-','+' ,'1', '2', '3','*', '=', '0','/', 'sqrt' ]


def write_to_text_area(value):
    if value == "=":
        try:
            expression = text_area.get("1.0" , "end-1c")
            result = eval(expression)
            text_area.configure(state="normal")
            text_area.delete("1.0" , tk.END)
            text_area.insert("end" , result)
            text_area.configure(state='disabled')
        except Exception as e:
            text_area.configure(state="normal")
            text_area.delete("1.0",tk.END)
            text_area.insert("end" , "Error")
            text_area.configure(state="disabled")
        
    elif value == "<-":
        text_area.configure(state="normal")
        text_area.delete("end-2c" , tk.END)
        text_area.configure(state="disabled")
    
    elif value == "c":
        text_area.configure(state="normal")
        text_area.delete("1.0" , tk.END)
        text_area.configure(state="disabled")
    
    elif value == "sqrt":
        try:
            num = text_area.get("1.0", "end-1c")
            num =float(num)
            result=math.sqrt(num)
            text_area.configure(state="normal")
            text_area.delete("1.0" , tk.END)
            text_area.insert("end" , result)
            text_area.configure(state="disabled")
        except ValueError:
            text_area.configure(state="normal")
            text_area.delete("1.0" , tk.END)
            text_area.insert("end" , "Invalid Input")
            text_area.configure(state="disabled")
        
    else:
        text_area.configure(state="normal")
        text_area.insert("end" , value)
        text_area.configure(state="disabled")

for i in range(len(value)):
    button=tk.Button(frame, font='20', text=value[i], height=5, width=12, command=lambda index=i: write_to_text_area(value[index]))
    button.grid(row=i // 5 , column=i % 5)

root.mainloop()
