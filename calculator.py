import customtkinter
import customtkinter as ctk
import numpy as np

z=0
app = ctk.CTk( )
app.title("New calculator 6.0 beta test")
app.iconbitmap('$RGWODJ2.ico')
ctk.set_appearance_mode('dark')

m=float
def q1():
    p1=int(v.get())
v= ctk.CTkEntry(master=app,width=450,height=2)
v1=ctk.CTkLabel(master=app,width=450,text_color="green",text="сдесь будет выводится ровное",font=(app,20))
var=int()



def w12():
    app1=complex(v.get())
    app2=np.log(app1)
    v1.configure(text=app2)

def b():
    v.insert(ctk.END,0)
def b1():
    v.insert(ctk.END,1)
def b2():
    v.insert(ctk.END,2)
def b3():
    v.insert(ctk.END,3)
def b4():
    v.insert(ctk.END,4)
def b5():
    v.insert(ctk.END,5)
def b6():
    v.insert(ctk.END,6)
def b7():
    v.insert(ctk.END,7)
def b8():
    v.insert(ctk.END,8)
def b9():
    v.insert(ctk.END,9)
def b10():
    v.insert(ctk.END,"/")
def b11():
    v.insert(ctk.END,"*")
def b12():
    v.insert(ctk.END,"+")
def b13():
    v.insert(ctk.END,"-")
def b14():
    p=(v.get())
    pass1=(eval(p))
    v1.configure(text=str(pass1))

def b15():
    v.delete(0,ctk.END)

def b16():

    p1=complex(v.get())
    pass2=(np.sqrt(p1))
    v1.configure(text=pass2)
def w13():
    w14=complex(v.get())
    w15=np.exp(w14)
    v1.configure(text=w15)
def w14():
    w15=complex(v.get())
    w16=np.tan(w15)
    v1.configure(text=w16)
def w15():
    w16=complex(v.get())
    w17=np.sin(w16)
    v1.configure(text=w17)
def w16():
    w18=complex(v.get())
    w19=np.cos(w18)
    v1.configure(text=w19)
def w17():
    w20=complex(v.get())
    w21=np.arctan(w20)
    v1.configure(text=w21)
def w18():
    w22=complex(v.get())
    w23=np.arcsin(w22)
    v1.configure(text=w23)
def w19():
    w24=complex(v.get())
    w25=np.arccos(w24)
    v1.configure(text=w25)
def w20():
    w26=complex(v.get())
    w27=np.atan(w26)
    v1.configure(text=w27)
def w21():
    w28=complex(v.get())
    w29=np.asin(w28)
    v1.configure(text=w29)
def w22():
    w30=complex(v.get())
    w31=np.acos(w30)
    v1.configure(text=w31)
def w23():
    w32=complex(v.get())
    w33=np.atan(v.get())
    v1.configure(text=w33)
def w24():
    w34=complex(v.get())
    w35=np.tanh(w34)
    v1.configure(text=w35)
def w25():
    w36=complex(v.get())
    w37=np.sinh(w36)
    v1.configure(text=w37)
def w26():
    w38=complex(v.get())
    w39=np.cosh(w38)
    v1.configure(text=w39)
def w27():
    w40=float(v.get())
    w42=[w40]
    w41=np.i0(w42)
    v1.configure(text=w41)
def w28():
    w43=float(v.get())
    w43_d=[w43]
    w44=np.radians(w43_d)
    v1.configure(text=w44)
def w29():
    w45=complex(v.get())
    w46=np.sinc(w45)
    v1.configure(text=w46)
def w30():
    w47=complex(v.get())
    w48=np.arctanh(w47)
    v1.configure(text=w48)
def w31():
    w49=complex(v.get())
    w50=np.arccosh(w49)
    v1.configure(text=w50)
def w32():
    w51 = complex(v.get())
    w52 = np.arcsinh(w51)
    v1.configure(text=w52)
def des():
    bxxcv=float
    w53=bxxcv(v.get())
    w54=np.floor(w53)
    v1.configure(text=w54)
def vbb():
    w53 = m(v.get())
    w54 = np.degrees(w53)
    v1.configure(text=w54)
def vbb1():
    w53 = m(v.get())
    w34=np.array([w53])
    w54 = np.cbrt(w34)
    v1.configure(text=w54)
def vbb2():
    w34 = m(v.get())
    w54 = np.expm1(w34)
    v1.configure(text=w54)
def vbb3():
    w34 = m(v.get())
    w35=np.array(w34)
    w54 = np.hypot(w35,w35)
    v1.configure(text=w54)
def vbb5():
    w34 = m(v.get())
    w35 = np.array(w34)
    w54 = np.angle(w35, w35)
    v1.configure(text=w54)
def vbb6():
    w34 = m(v.get())
    w35 = np.array(w34)
    w54 = np.unwrap([w35, w35,w35,w35,w35],period=4)
    v1.configure(text=w54)
def vbb7():
    w34 = m(v.get())
    w35 = np.array(w34)
    w54 = np.gradient(w35)
    v1.configure(text=w54)
def vbb8():
    w34 = m(v.get())
    w35 = np.array(w34)
    w54 = np.convolve(w35,w35)
    v1.configure(text=w54)
def vbb9():
    w34 = m(v.get())
    w35 = np.array(w34)
    w54 = np.conj(w35)
    v1.configure(text=w54)
def q222():
    c1=ctk.CTkToplevel(app)
    c1.iconbitmap('$RGWODJ2.ico')
    c=ctk.CTkButton(master=c1,text="floor",command=des)
    c11 = ctk.CTkButton(master=c1, text="radians to corners", command=vbb)
    c12 = ctk.CTkButton(master=c1, text="cbrt", command=vbb1)
    c13=ctk.CTkButton(master=c1, text="exp(a)-1", command=vbb2)
    c14 = ctk.CTkButton(master=c1, text="hypot", command=vbb3)
    c15 = ctk.CTkButton(master=c1, text="angle", command=vbb5)
    c16 = ctk.CTkButton(master=c1, text="unwrap", command=vbb6)
    c17 = ctk.CTkButton(master=c1, text="gradient", command=vbb7)
    c18=ctk.CTkButton(master=c1, text="convolve", command=vbb8)
    c19 = ctk.CTkButton(master=c1, text="conj", command=vbb9)
    e2=ctk.CTkLabel(master=c1,text="Function 12")
    e3 = ctk.CTkLabel(master=c1, text="func")
    c.grid(row=4,column=5)
    e2.grid(row=1,column=6)
    e3.grid(row=3,column=5)
    c11.grid(row=5,column=5,pady=5)
    c12.grid(row=7,column=5,pady=5)
    c13.grid(row=9,column=5,pady=5)
    c14.grid(row=12,column=5,pady=5)
    c15.grid(row=14,column=5,pady=5)
    c16.grid(row=16,column=5,pady=5)
    c17.grid(row=18,column=5,pady=5)
    c18.grid(row=20,column=5,pady=5)
    c19.grid(row=22,column=5,pady=5)
    c1.mainloop()
def f1():


    xz=ctk.CTkToplevel()
    xz.title("Настройки calculator 6.0 alfa")
    xz.iconbitmap('$RGWODJ2.ico')
    xz2=ctk.CTkLabel(master=xz,text="function dlls 1",text_color="lightblue",font=(app,30))
    xz1=ctk.CTkCheckBox(master=xz,text="dlls",font=(app,30),command=q222)

    xz2.grid(row=1,column=1)
    xz1.grid(row=3,column=1)



x = ctk.CTkButton(master=app,text='Настройки',hover=True,height=10,font=(app,30),command=f1)
v2=ctk.CTkLabel(master=app,text='math numbers',width=160,font=(app,20))
v3=ctk.CTkLabel(master=app,text='math function',width=160,font=(app,20))
v4=ctk.CTkLabel(master=app,text='math symbols',width=160,font=(app,20))
v14=ctk.CTkButton(master=app,text='0',width=360,hover=True,height=10,font=(app,30),command=(b))
v5=ctk.CTkButton(master=app,text='1',width=360,hover=True,height=10,font=(app,30),command=b1)
v6=ctk.CTkButton(master=app,text='2',width=360,hover=True,height=10,font=(app,30),command=b2)
v7=ctk.CTkButton(master=app,text='3',width=360,hover=True,height=10,font=(app,30),command=b3)
v8=ctk.CTkButton(master=app,text='4',width=360,hover=True,height=10,font=(app,30),command=b4)
v9=ctk.CTkButton(master=app,text='5',width=360,hover=True,height=10,font=(app,30),command=b5)
v10=ctk.CTkButton(master=app,text='6',width=360,hover=True,height=10,font=(app,30),command=b6)
v11=ctk.CTkButton(master=app,text='7',width=360,hover=True,height=10,font=(app,30),command=b7)
v12=ctk.CTkButton(master=app,text='8',width=360,hover=True,height=10,font=(app,30),command=b8)
v13=ctk.CTkButton(master=app,text='9',width=360,hover=True,height=10,font=(app,30),command=b9)
v15=ctk.CTkButton(master=app,text='/',width=360,hover=True,height=10,font=(app,30),command=b10)
v16=ctk.CTkButton(master=app,text='*',width=360,hover=True,height=10,font=(app,30),command=b11)
v17=ctk.CTkButton(master=app,text='+',width=360,hover=True,height=10,font=(app,30),command=b12)
v18=ctk.CTkButton(master=app,text='-',width=360,hover=True,height=10,font=(app,30),command=b13)
v19=ctk.CTkButton(master=app,text='=',width=360,hover=True,height=10,font=(app,30),command=b14)
v21=ctk.CTkButton(master=app,text='delete',width=120,hover=True,command=b15)
v22=ctk.CTkButton(master=app,text='корень',hover=True,command=b16,height=10,font=(app,30))
r4=ctk.CTkButton(master=app,text='логорифм',hover=True,command=w12,height=10,width=100,font=(app,30))
r5=ctk.CTkButton(master=app,text="преоброзовать в е",command=w13,height=10,font=(app,30))
r6=ctk.CTkButton(master=app,text="тангельс",command=w14,height=10,width=100,font=(app,30))
r7=ctk.CTkButton(master=app,text="синус",command=w15,height=10,width=100,font=(app,30))
r8=ctk.CTkButton(master=app,text='косинус',command=w16,height=10,width=100,font=(app,30))
r10=ctk.CTkButton(master=app,text="обратный тангельс",command=w17,height=10,width=100,font=(app,30))
r11=ctk.CTkButton(master=app,text="обратный синус",command=w18,height=10,width=10,font=(app,30))
r12=ctk.CTkButton(master=app,text="обратный косинус",command=w19,height=10,width=10,font=(app,30))
r13=ctk.CTkButton(master=app,text="арктангенс",command=w20,height=10,width=10,font=(app,30))
r14=ctk.CTkButton(master=app,text="арксинус",command=w21,height=10,width=10,font=(app,30))
r15=ctk.CTkButton(master=app,text="арккосинус",command=w22,height=10,width=10,font=(app,30))
r16=ctk.CTkButton(master=app,text="арктангельс",command=w23,height=10,width=10,font=(app,30))
r17=ctk.CTkButton(master=app,text="гиперболический тангельс",command=w24,height=10,width=10,font=(app,30))
r18=ctk.CTkButton(master=app,text="гиперболический синус",command=w25,height=10,width=10,font=(app,30))
r19=ctk.CTkButton(master=app,text="гиперболический косинус",command=w26,height=10,width=10,font=(app,30))
r20=ctk.CTkButton(master=app,text="функция Бесселя",command=w27,height=10,width=10,font=(app,30))
r21=ctk.CTkButton(master=app,text="радианы",command=w28,height=10,width=10,font=(app,30))
r22=ctk.CTkButton(master=app,text="y ( т )",command=w29,height=10,width=10,font=(app,30))
r23=ctk.CTkButton(master=app,text="arctanh ",command=w30,height=10,width=10,font=(app,30))
r24=ctk.CTkButton(master=app,text="arccosh",command=w31,height=10,width=10,font=(app,30))
r25=ctk.CTkButton(master=app,text="arcsinh",command=w32,height=10,width=10,font=(app,30))

v1.grid(row=1,column=6)
v21.grid(row=1,column=7)
x.grid(row=1, column=1)
v2.grid(row=3,column=5)
v14.grid(row=4,column=5,pady=5)
v5.grid(row=5,column=5,pady=5)
v6.grid(row=6,column=5,pady=5)
v7.grid(row=7,column=5,pady=5)
v8.grid(row=8,column=5,pady=5)
v9.grid(row=9,column=5,pady=5)
v10.grid(row=10,column=5,pady=5)
v11.grid(row=11,column=5,pady=5)
v12.grid(row=12,column=5,pady=5)
v13.grid(row=13,column=5,pady=5)
r24.grid(row=14,column=5)
r25.grid(row=15,column=5)
v3.grid(row=3,column=6)
v19.grid(row=4,column=6)
v17.grid(row=5,column=6)
v18.grid(row=6,column=6)
v16.grid(row=8,column=6)
v15.grid(row=7,column=6)
v.grid(row=2,column=6,padx=50)
v4.grid(row=3,column=7)
v22.grid(row=4,column=7)
r4.grid(row=5,column=7)
r5.grid(row=6,column=7)
r6.grid(row=7,column=7)
r7.grid(row=8,column=7)
r8.grid(row=9,column=7)
r10.grid(row=10,column=7)
r11.grid(row=11,column=7)
r12.grid(row=12,column=7)
r13.grid(row=13,column=7)
r14.grid(row=14,column=7)
r15.grid(row=15,column=7)
r17.grid(row=9,column=6)
r18.grid(row=10,column=6)
r19.grid(row=11,column=6)
r20.grid(row=12,column=6)
r21.grid(row=13,column=6)
r22.grid(row=14,column=6)
r23.grid(row=15,column=6)


app.mainloop ()