# Aprendendo a usar o Tkinter #




from tkinter import Tk, Label, PhotoImage

raiz = Tk()
photo = PhotoImage(file=r'C:\bsthe\Desktop\\teste\barbie-diy.gif').subsample(5)
hello = Label(master = raiz, image= photo, width=300, height=100)
hello.pack()
raiz.mainloop()
