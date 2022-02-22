from tkinter import*
from MSE import mse_cipher,mse_decipher
from keylib_generator import gen_file

app = Tk()
app.title("Genesis Key")
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w, h))
#app.iconbitmap('icone.ico')
app.config(bg="#192D46")

larg_cons = 400
larg_entry = w-larg_cons
font_size = 20

entree = StringVar()
entree = Text(app, width=w, height=20,bg="#1990A4",fg='#fff', font=("Monospace", font_size))
entree.config(insertbackground="#fff")
entree.pack(side='top')
entree.focus()

def get_user_entry():
    return entree.get("1.0",'end-1c').split('\n')

def cip():
	msgs = get_user_entry()
	entree.delete('1.0', END)

	for msg in msgs:
		entree.insert(1.0, mse_cipher(msg))
		entree.insert(1.0, "\n")


def dec():
	msgs = get_user_entry()
	entree.delete('1.0', END)

	for msg in msgs:
		entree.insert(1.0, mse_decipher(msg))
		entree.insert(1.0, "\n")


cip_btn = Button(app,text="Cipher",bg="#19D1A4",fg="#fff",relief=FLAT,font=("Monospace", font_size),command=cip)
cip_btn.pack(side='left',padx=20,pady=20)

dec_btn = Button(app,text="Decipher",bg="#C9787D",fg="#fff",relief=FLAT,font=("Monospace", font_size),command=dec)
dec_btn.pack(side='left',padx=20,pady=20)

gen_btn = Button(app,text="Generate keys",bg="#C9F47E",fg="#fff",relief=FLAT,font=("Monospace", font_size),command=gen_file)
gen_btn.pack(side='left',padx=20,pady=20)

app.mainloop()






