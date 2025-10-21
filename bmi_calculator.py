from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image,ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

try:
    image_icon=PhotoImage(file="Images/icon.png")
    root.iconphoto(False,image_icon)
except:
    pass

