from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text, src, dest):
    src1=src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text



def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0,END)
    
    print(s)
    print(d)
    print(msg)
    textget = change(text = msg, src = s, dest = d)
    print(textget)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)




root = Tk()
root.title('Translator')
root.geometry('500x800')



lab_txt = Label(root, text='Translator', font=('Time New Roman', 40, 'bold'))
lab_txt.place(x=100, y=30, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text='Source Text', font=('Time New Roman', 20, 'bold'))
lab_txt.place(x=100, y=100, height=20, width=300)


sor_txt = Text(frame, font=('Time New Roman', 20, 'bold'), wrap=WORD)
sor_txt.place(x=10, y=130, height=200, width=480)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=10,y=350,height=40,width=150)
comb_sor.set('English')


button_change = Button(frame, text='Translate',relief=RAISED, command=data)
button_change.place(x=170,y=350, height=40, width=150)


comb_dest = ttk.Combobox(frame, values=list_text)
comb_dest.place(x=330,y=350,height=40,width=150)
comb_dest.set('English')




lab_txt = Label(root, text='Dest Text', font=('Time New Roman', 20, 'bold'))
lab_txt.place(x=100, y=420, height=20, width=300)

dest_txt = Text(frame, font=('Time New Roman', 20, 'bold'), wrap=WORD)
dest_txt.place(x=10, y=450, height=200, width=480)



root.mainloop()