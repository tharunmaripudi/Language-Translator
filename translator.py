from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
language=googletrans.LANGUAGES
lang_value=list(language.values())
lang1=language.keys()
window=Tk()
window.title("language translator")
window.geometry("600x500")
def translater():
    try:
        txt=txt1.get(1.0,END)
        c1=combo1.get()
        c2=combo2.get()
        for i,j in language.items():
            if(j==c1):
                sr=i
            if(j==c2):
                des=i
        words=Translator().translate(str(txt), src=str(sr), dest=str(des)).text
        txt2.delete(1.0,END)
        txt2.insert(END,words)
    except Exception as e:
        messagebox.showerror("try again")
#combo1
combo1=ttk.Combobox(window,values=lang_value,state='r')
combo1.place(x=100,y=20)
combo1.set("Choose a language")
#Frame1
f1=Frame(window,bg='black',bd=4)
f1.place(x=100,y=100,width=150,height=150)
#text1
txt1=Text(f1,font='Roboto 14',bg='white',relief=GROOVE,wrap=WORD)
txt1.place(x=0,y=0,width=140,height=140)

#combo2
combo2=ttk.Combobox(window,values=lang_value,state='r')
combo2.place(x=300,y=20)
combo2.set("Choose a language")
#Frame2
f2=Frame(window,bg='black',bd=4)
f2.place(x=300,y=100,width=150,height=150)
#text2
txt2=Text(f2,font='Roboto 14',bg='white',relief=GROOVE,wrap=WORD)
txt2.place(x=0,y=0,width=140,height=140)
#button
button=Button(window,text='translate',font=('normal',15),bg='yellow',command=translater)
button.place(x=230,y=300)
window.mainloop()