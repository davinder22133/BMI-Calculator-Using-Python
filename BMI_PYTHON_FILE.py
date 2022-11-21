from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("430x600+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")


#icon  
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)



#top image
top=PhotoImage(file="top.png")
top_image=Label(root,image=top,background="#f0f1f5",width=500)
top_image.place(x=-30,y=-10)


#bottom box
Label(root,width=72,height=19,bg="lightblue").pack(side=BOTTOM)


#two boxes
box=PhotoImage(file="box.png")
Label(root,image=box,width=180).place(x=20,y=75)
Label(root,image=box,width=180).place(x=230,y=75)



#scale
scale=PhotoImage(file="scale.png")
Label(root,image=scale,bg="lightblue").place(x=20,y=325)






style=ttk.Style()
style.configure("TScale",background="White")


# SLIDER 1
current_value=tk.DoubleVar()



def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())
    size=int(float(get_current_value()))
    img=Image.open('man.png')
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2
slider=ttk.Scale(root,from_=0,style="TScale",to=220,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=50,y=230)



# SLIDER 2

current_value2=tk.DoubleVar()



def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())

slider2=ttk.Scale(root,from_=0,style="TScale",to=220,orient='horizontal',command=slider_changed2,variable=current_value2)
slider2.place(x=280,y=230)

#entry box 
Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=LEFT)
height.place(x=18,y=145)

weight=Entry(root,textvariable=Weight,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=230,y=145)




secondimage=Label(root,bg="lightblue")
secondimage.place(x=70,y=530)


def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    
    #convert height into metre
    m=h/100
    bmi=round(float(w/m**2))
    label1.config(text=bmi)
    
    if(bmi<=18):
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight than normal body!")
        
    elif bmi<=18 and bmi<=25:
        label2.config(text="Normal!")
        label3.config(text="It indicates that you are healthy!")
    
    elif bmi>=25 and bmi<=30:
        label2.config(text="OverWeight!")
        label3.config(text="It indicates that you a person is \n slightly overweight! \n A doctor may advise to lose some weight!")
    
    else:
        
        label2.config(text="Obes!")
        label3.config(text="Health may be at risk, if you do not \n lose weight!")
        
    print(bmi)
Button(root,text="View Report",command=BMI,width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white").place(x=280,y=340)


label1=Label(root,font="arial 60 bold",bg="lightblue",fg="#fff")
label1.place(x=125,y=310)


label2=Label(root,font="arial 30 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=140,y=430)

label3=Label(root,font="arial 10 bold",bg="lightblue")
label3.place(x=140,y=500)
root.mainloop()



