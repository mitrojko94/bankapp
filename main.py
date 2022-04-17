from tkinter import *

from mysqlx import Row
from klase import *

root=Tk()
def nista():
    pass

def podigni():
    if r.blok:
            print('Racun je blokiran')
            return
    t=Toplevel(root)
    l_iznos=Label(t,text='Unesite iznos')
    l_iznos.pack()
    e_iznos=Entry(t)
    e_iznos.pack()
    b_submit=Button(t,text='Potvrdi',command=lambda:[r.podigni_novac(int(e_iznos.get())),t.destroy()])
    b_submit.pack()
    mainloop()

def uplati():
    if r.blok:
            print('Racun je blokiran')
            return
    t=Toplevel(root)
    l_iznos=Label(t,text='Unesite iznos')
    l_iznos.pack()
    e_iznos=Entry(t)
    e_iznos.pack()
    b_submit=Button(t,text='Potvrdi',command=lambda:[r.uplati_novac(int(e_iznos.get())),t.destroy()])
    b_submit.pack()
    mainloop()

def blok():
    t=Toplevel(root)
    l_iznos=Label(t,text='Da li ste sigurni')
    b_submit=Button(t,text='Potvrdi',command=lambda:[r.blokiraj_racun(),t.destroy()])
    b_submit.pack()
    mainloop()

root.geometry('200x200')
menubar = Menu(root)
root.config(menu=menubar)
radnje = Menu(menubar)
radnje.add_command(label='Podigni novac',command=lambda:podigni())
radnje.add_command(label='Uplati novac',command=lambda:uplati())
radnje.add_command(label='Upit stanja',command=lambda:r.upit_stanja())
radnje.add_command(label='Izvestaj',command=lambda:r.izvestaj())
radnje.add_command(label='Blokiraj racun',command=lambda:blok())
menubar.add_cascade(label="Bankomat",menu=radnje)
Exit_menu = Menu(menubar)
Exit_menu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label="Exit",menu=Exit_menu)

l_racun=Label(root,text='BANKOMAT')
l_racun.place(x=50,y=100)




mainloop()