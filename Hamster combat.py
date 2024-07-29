from PIL import Image
from customtkinter import*
import customtkinter as ctk
from random import*
ct=ctk.CTk()
ct.title("Hamster Combat")
ctk.set_appearance_mode('dark')
bw=0
bw1=str(bw)
bw3=0
bw2=str(bw3)
bw4=0
bw5=str(bw4)
vb4=0
vb5=str(vb4)
n=0
n1=str(n)
n2=0
n3=str(n2)
l=ctk.CTkLabel(master=ct,text="0",text_color="white",font=(ct,30))
l1=ctk.CTkLabel(master=ct,text="$:"+bw1,text_color="green",font=(ct,30))
l2=ctk.CTkLabel(master=ct,text="Br:"+bw2,text_color="green",font=(ct,30))
l3=ctk.CTkLabel(master=ct,text="₽:"+bw5,text_color="green",font=(ct,30))
l4=ctk.CTkLabel(master=ct,text="€:"+vb5,text_color="green",font=(ct,30))
l5=ctk.CTkLabel(master=ct,text="di:"+n1,text_color="blue",font=(ct,30))
l6=ctk.CTkLabel(master=ct,text="¥:"+n3,text_color="red",font=(ct,30))
b=0
b1=0
z=1
def asc():
    global b
    b+=z
    b1=str(b)
    l.configure(text=b1)
def asc1():
    global bw3
    global b3
    global b
    b3 = b / 1656
    bw3 += b3
    b-=b
    l.configure(text=b)

    bw1=str(bw3)
    l1.configure(text="$:"+bw1)
def c():
    global bw4
    global b3
    global b
    b4= b / 45
    bw4 += b4
    b-=b
    l.configure(text=b)
    bw1=str(bw4)
    l2.configure(text="Br:"+bw1)

def c1():
    global bw
    global bw4
    global b
    b4= b / 2
    bw += b4
    b-=b
    l.configure(text=b)
    bw1=str(bw)
    l3.configure(text="₽:"+bw1)
def c2():
    global bw
    global vb4
    global b
    b4= b / 10
    vb4 += b4
    b-=b
    l.configure(text=b)
    bw1=str(vb4)
    l4.configure(text="€:"+bw1)
def c12():
    global bw
    global n
    global b
    b4= b / 500
    n += b4
    b-=b
    l.configure(text=b)
    bw1=str(n)
    l5.configure(text="di:"+bw1)
def c13():
    global bw
    global n2
    global b
    b4= b / 5
    n2 += b4
    b-=b
    l.configure(text=b)
    bw1=str(n2)
    l6.configure(text="¥:"+bw1)
def we():
    global b
    r=randint(1,2)
    if r==1:
        b/=2
    if r==2:
        b= b*2
def we2():
    global z
    global n
    if  n>=1:
        n -= 1
        z+=1
    if n>=0:
        pass

image6=CTkImage(light_image=Image.open('D:\Seaborn\yan.jfif'),size=(50,50))
image_open=CTkImage(light_image=Image.open('D:\Seaborn\Hamster.jpg'),size=(400,400))
image2=CTkImage(light_image=Image.open('D:\Seaborn\dollor.jfif'),size=(50,50))
image1=CTkImage(light_image=Image.open('D:\Seaborn\oi.jfif'),size=(50,50))
image3=CTkImage(light_image=Image.open('D:\Seaborn\images.jfif'),size=(50,50))
image4=CTkImage(light_image=Image.open('D:\Seaborn\eura.jfif'),size=(50,50))
image5=CTkImage(light_image=Image.open('D:\Seaborn\Без названия.jfif'),size=(50,50))
v=CTkButton(master=ct,text="",image=image_open,fg_color='green',hover_color='green',hover=True,command=asc)
v1=CTkButton(master=ct,text="",fg_color="green",image=image2,hover=True,command=asc1)
v2=CTkButton(master=ct,text="",fg_color="blue",image=image1,hover=True,command=c)
v3=CTkButton(master=ct,text="",fg_color="red",image=image3,hover=True,command=c1)
v4=CTkButton(master=ct,text="",fg_color="yellow",image=image4,hover=True,command=c2)
v5=CTkButton(master=ct,text="",image=image5,fg_color="blue",hover=True,command=c12)
v6=CTkButton(master=ct,text="",image=image6,fg_color="red",hover=True,command=c13)
v7=CTkButton(master=ct,text="50/50",fg_color="black",hover=True,command=we,font=(ct,50))
v9=CTkButton(master=ct,text="*2=1 алмаз",fg_color="yellow",hover=True,command=we2,font=(ct,50))

v.place(x=450,y=100)
v1.place(x=1220,y=0)
v2.place(x=1220,y=100)
v3.place(x=1220,y=200)
v4.place(x=1220,y=300)
v5.place(x=1220,y=400)
v6.place(x=1220,y=500)
v7.place(x=1220,y=600)
v9.place(x=0,y=600)
l.place(x=660,y=0)
l1.place(x=7,y=0)
l2.place(x=7,y=50)
l3.place(x=7,y=100)
l4.place(x=7,y=150)
l5.place(x=7,y=200)
l6.place(x=7,y=250)
ct.mainloop()