# https://coderslegacy.com/python/tkinter-key-binding/?fbclid=IwAR0jREXtn2AYeKjqjhFOH7_6hn9PPwmiNoQLnchINuCluLLA6v20ZtI3leI


from tkinter import *
from tkinter import messagebox
from random import randint

main = Tk()

main.geometry("1024x768")
#frame - Frame( main )
can = Canvas( main, background="#96DED1", width=600, height=600)
can.create_text(300, 75, text="HANGMAN", fill="black", font=("Acme 40 "))
can.pack()

# main.mainloop()
# can.itemconfig(1, state='normal')

zoznam_slov = ["strom", "jahoda", "matematika", "zemegula", "traktor", "bager"]

x_zaciatok = 100
y_zaciatok = 450

sirka_obdlznika = 45
vyska_obdlznika = 100
medzera_medzi_obdlznikmi = 5

pocet_slov = len(zoznam_slov)
por_cis_slova = randint(1, pocet_slov)
zvolene_slovo = zoznam_slov[por_cis_slova - 1]
dlzka_slova = len(zvolene_slovo)
pocet_neuhadnutych = dlzka_slova

# program nam vyberie jedno z cisel z intervalu 1 a pocet slov v zozname

print("Pocet slov:", str(pocet_slov))
print("Zvolene cislo slova:", str(por_cis_slova))
print("Zvolene slovo je ", zvolene_slovo)
print("Dlzka slova je ", str(dlzka_slova))

for i in range(0, dlzka_slova ):
    can.create_rectangle(x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika),
                             y_zaciatok,
                             x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika,
                             y_zaciatok + vyska_obdlznika)
    can.create_text( x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika / 2,
                             y_zaciatok + vyska_obdlznika / 2.25,  text=".", fill="blue", font=("Acme 28 "))
can.pack()
# p = input("Zadaj pismenko: ")
## L1 = Label(main, text="Hádaj písmenko:")
## L1.pack(side=LEFT)
## E1 = Entry(main, bd=1)
## E1.insert(0, '?')

## def welcomeMessage():
##    name = name_Tf.get()
##    return messagebox.showinfo('message', f'Hi! {name}, Welcome to python guides.')


## Label( main, text="Enter Name" ).pack()
## name_Tf = Entry( main )
## name_Tf.pack()
## Button( main, text="Click Here", command=welcomeMessage).pack()

def OkMessage():
    pismenko = pism_Tf.get()
    return messagebox.showinfo('message', f'Ok, zadal si {pismenko}.')

Label( main, text="Enter Name" ).pack()
pism_Tf = Entry( main )
pism_Tf.pack()
Button( main, text="Ok", command=OkMessage()).pack()

i = 0
while i<10 and pocet_neuhadnutych > 0:
    E1.pack( )
    #E1.pack(side=RIGHT)
    p = E1.get()
    for j in range(0, dlzka_slova ):
        if zvolene_slovo[j] == p:
            pocet_neuhadnutych -= 1
            can.create_text(x_zaciatok + j * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika / 2,
                            y_zaciatok + vyska_obdlznika / 2, text=p, fill="green", font=("Acme 28 "))
            can.pack()
    i += 1
main.mainloop()