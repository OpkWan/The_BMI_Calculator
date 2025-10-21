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
        
try:
    image_icon=PhotoImage(file="Images/icon.png")
    root.iconphoto(False,image_icon)
except:
    pass

#top
try:
    top=PhotoImage(file="Images/top.png")
    top_image=Label(root,image=top,background="#f0f1f5")
    top_image.place(x=-10,y=-10)
except:
    pass

#bottom box
Label(root,width=72,height=18,bg="lightblue").pack(side=BOTTOM)


#two boxes
try:
    box=PhotoImage(file="Images/box.png")
    Label(root,image=box).place(x=20,y=100)
    Label(root,image=box).place(x=240,y=100)
except:
    pass


#scale
try:
    scale=PhotoImage(file="Images/scale.png")
    Label(root,image=scale,bg="lightblue").place(x=20,y=310)
except:
    pass

################Slider 1 - HEIGHT#####################
# Add label for Height slider
Label(root, text="HEIGHT (cm)", font="arial 14 bold", bg="white", fg="#1f6e68").place(x=55, y=130)

current_value = tk.DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    update_man_image()

def slider_changed2(event):
    Weight.set(get_current_value2())
    update_man_image()

def update_man_image():
    height_val = int(float(get_current_value()))
    weight_val = int(float(get_current_value2()))
    
    # Calculate width based on weight (min 30, max 150)
    width = 30 + int(weight_val * 0.6)  # scales from 30 to 150 as weight goes 0-200
    
    # Calculate height based on height value
    img_height = 10 + height_val
    
    try:
        img = Image.open("Images/man.png")
        resized_image = img.resize((width, img_height))
        photo2 = ImageTk.PhotoImage(resized_image)
        secondimage.config(image=photo2)
        # Adjust x position to keep centered as width changes
        x_pos = 95 - (width // 2)
        secondimage.place(x=x_pos, y=550-height_val)
        secondimage.image = photo2
    except:
        pass

#command to change background color of scale
style = ttk.Style()
style.configure("TScale",background="white")

slider = ttk.Scale(root,from_=0, to=220, orient="horizontal",style="TScale",command=slider_changed, variable=current_value)
slider.place(x=80,y=250)


###########################################



##@@@@@@@@@@@@@@@Slider 2 - WEIGHT@@@@@@@@@@@@@@@@@@
# Add label for Weight slider
Label(root, text="WEIGHT (kg)", font="arial 14 bold", bg="white", fg="#1f6e68").place(x=270, y=130)

current_value2 = tk.DoubleVar()

def get_current_value2():
    return "{: .2f}".format(current_value2.get())

#command to change background color of scale
style2 = ttk.Style()
style2.configure("TScale",background="white")

slider2 = ttk.Scale(root,from_=0, to=200, orient="horizontal",style="TScale",command=slider_changed2, variable=current_value2)
slider2.place(x=300,y=250)



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




#entry box
Height=StringVar()
Weight=StringVar()

def on_height_change(*args):
    try:
        val = float(Height.get())
        if 0 <= val <= 220:
            current_value.set(val)
            update_man_image()
    except ValueError:
        pass

def on_weight_change(*args):
    try:
        val = float(Weight.get())
        if 0 <= val <= 200:
            current_value2.set(val)
            update_man_image()
    except ValueError:
        pass


Height.trace('w', on_height_change)
Weight.trace('w', on_weight_change)

height=Entry(root,textvariable=Height,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=255,y=160)
Weight.set(get_current_value2())


#man image
secondimage=Label(root,bg="lightblue")
secondimage.place(x=70,y=530)

Button(root,text="View Report",width=15,height=2,font="arial 10 bold", bg="#1f6e68",fg="white",command=BMI).place(x=280,y=340)

label1=Label(root,font="arial 60 bold",bg="lightblue",fg="#fff")
label1.place(x=125,y=305)

label2=Label(root,font="arial 20 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=280,y=430)

label3=Label(root,font="arial 10",bg="lightblue")
label3.place(x=200,y=500)

root.mainloop()