from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image,ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

def BMI():
    try:
        h=float(Height.get())
        w=float(Weight.get())

        #convert height into meter
        m=h/100
        bmi=round(float(w/m**2),1)
        label1.config(text=bmi)

        if bmi <= 18.5:
            label2.config(text="Underweight!")
            label3.config(text="You have lower weight than normal body!")
        elif bmi > 18.5 and bmi <= 25:
            label2.config(text="Normal!")
            label3.config(text="You are healthy!")
        elif bmi >= 25 and bmi <=30:
            label2.config(text="Overweight!")
            label3.config(text="You are slightly overweight! \n A doctor may advise to lose some \n weight for health reason")
        else:
            label2.config(text="Obese!")
            label3.config(text="Your health my be at risk! \n If you do not lose weight")
    except ValueError:
        messagebox.showerror("Invalid Input", "Insert a valid number!")
        # Reset values
        Height.set("0.00")
        Weight.set("0.00")
        current_value.set(0)
        current_value2.set(0)
        label1.config(text="")
        label2.config(text="")
        label3.config(text="")
        # Reset man image
        secondimage.config(image="")
        secondimage.place(x=70,y=530)