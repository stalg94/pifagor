from tkinter import * 
from tkinter import ttk
#from my_module import*
from tkinter import scrolledtext
import docx, fileinput

from tkinter.filedialog import *





def save_file():
    s_file = asksaveasfile()
    text=txt.get(0,END)
    s_file.write(text)
    s_file.close()


def rewenie():
    value=kuu.get()
    q=kuud.index(value)
    b=kuud_int[q]
    print(b)
    a = int(paev.get())
    print(a)
    c = int(aasta.get())
    print(c)
    #s=[a//10,a%10,b//10,b%10,c//1000,c%1000//100,c%100//10,c%10]
    e=a//10+a%10+b//10+b%10
    d=c//1000+c%1000//100+c%100//10+c%10
    m=e+d #1 рабочее число
    n=m//10+m%10 #2 рабочее число
    w=m-2*(a//10) #3 рабочее число
    t=w//10+w%10 #4
    s=[a//10,a%10,b//10,b%10,c//1000,c%1000//100,c%100//10,c%10,m//10,m%10,n//10,n%10,w//10,w%10,t//10,t%10]
    s.sort()
    n0=s.count(0)
    print(n0)
    del s[0:n0]
    print(str(s))
    #lopp_list=kvadrat(a,b,c)
    text=(f'1-е рабочее число = {m}\n2-е рабочее число = {n}\n3-е рабочее число = {w}\n4-е рабочее число = {t},\n {kvadrat(a,b,c)}')

    vastus.delete('0.0',END)
    vastus.insert(END,text)
    return
    
def kvadrat(a,b,c):
    e=a//10+a%10+b//10+b%10
    d=c//1000+c%1000//100+c%100//10+c%10
    m=e+d #1 рабочее число
    n=m//10+m%10 #2 рабочее число
    w=m-2*(a//10) #3 рабочее число
    t=w//10+w%10 #4
    r1=str(a)+str(b)+str(c)
    r2=str(m)+str(n)+str(w)+str(t)
    r3=r1+r2
    r_list=list(r3)
    r_list.sort()
    n1=r3.count("0")
    del r_list[0:n1]
    lopp_list=[]
    for i in range(1,10): #1,2,3,...
        if r_list.count(str(i))>=1:
            j=str(i)
            print(j*r_list.count(str(i)),end=" ")
            lopp_list.append(j*r_list.count(str(i)))
        else:
            print("нет",end=" ")
        if i%3==0:
            print()
    return lopp_list

def open_file():
    text_file= open(r"C:\Users\stalg\source\repos\PythonApplication8\pifagor.txt","r", encoding="utf-8-sig")
    stuff= text_file.read()

    txt.insert(END, stuff)
    text_file.close()



win=Tk()
win.title('kvadrat pifagora')
win.geometry('600x400')
win.config(bg='#5BEE50')
tab_control=ttk.Notebook(win)
tab1=Frame(tab_control)
tab2=Frame(tab_control)
tab_control.add(tab1,text='Вычисление')
tab_control.add(tab2,text='Теория')
tab1.configure(bg='#5BEE50')


kuud=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
kuud_int=[1,2,3,4,5,6,7,8,9,10,11,12]
var=IntVar()
var.set(1)
paev=Spinbox(tab1,from_=1,to=31,textvariable=var)
paev.grid(row=1,column=1,padx=(10,0),pady=10)
lbl1=Label(tab1,text='kuupäev',bg='#5BEE50').grid(row=0,column=1,stick='we',padx=10)
kuu = ttk.Combobox(tab1,values=kuud)
kuu.current(0)
kuu.grid(row=1,column=2,padx=10)
lbl2=Label(tab1,text='kuu',bg='#5BEE50').grid(row=0,column=2,stick='we',padx=10)
aasta=Entry(tab1,justify=RIGHT)
aasta.insert(0,'2000')
aasta.grid(row=1,column=3, padx=10)
lbl3=Label(tab1,text='aasta',bg='#5BEE50').grid(row=0,column=3,stick='we',padx=10)

btn1=Button(tab1,text='Uurida!',command=rewenie).grid(row=2,column=1,columnspan=2,stick='we',padx=10,pady=10)

vastus=Text(tab1, font="Arial 12", width=10,height=10)
vastus.grid(row=3,column=0,columnspan=5,stick='we',padx=10, pady=10)

m=Menu(win)
win.config(menu=m)
dialog_m=Menu(m,tearoff=0)
m.add_cascade(label='Menu',menu=dialog_m)
var=StringVar()
dialog_m.add_command(label='Ava',command=open_file)
dialog_m.add_command(label='Salvesta kui',command=save_file)

txt=scrolledtext.ScrolledText(tab2,width=60,height=40)
txt.grid(row=10,column=0,columnspan=4, padx=10,pady=10)
btn2=Button(tab2,text='Avada!',command=open_file).grid(row=2,column=0,columnspan=2,stick='we',padx=10,pady=10)
#doc=docx.Document(r"C:\Users\stalg\source\repos\PythonApplication8\pifagor.docx")
#all_paras = doc.paragraphs
#txt.delete('0.0',END)
#for para in all_paras:
#    txt.insert(END,all_paras)


tab_control.pack(expand=1,fill='both')


win.mainloop()
