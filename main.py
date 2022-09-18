# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from tkinter import Canvas, Tk
from random import randint

main = Tk()

main.geometry("1024x768")
can = Canvas(main, background="#96DED1", width=600, height=600)
can.pack()
can.create_text(300, 75, text="HANGMAN", fill="black", font=("Acme 40 "))
# main.mainloop()
# can.itemconfig(1, state='normal')

zoznam_slov = ["strom", "jahoda", "matematika", "zemegula", "traktor", "bager"]

x_zaciatok = 100
y_zaciatok = 450

sirka_obdlznika = 45
vyska_obdlznika = 100
medzera_medzi_obdlznikmi = 5

pocet_slov = len(zoznam_slov)

# program nam vyberie jedno z cisel z intervalu 1 a pocet slov v zozname
por_cis_slova = randint(1, pocet_slov)
dlzka_slova = len(zoznam_slov[por_cis_slova - 1])

for i in range(0, dlzka_slova - 1):
    can.create_rectangle(x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika),
                         y_zaciatok,
                         x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika,
                         y_zaciatok + vyska_obdlznika)

pocet_neuhadnutych = dlzka_slova
# can.create_window(x_zaciatok, y_zaciatok+2*vyska_obdlznika, window=entry1)


for i in range(1, 10):
    p = input("Zadaj pismenko: ")
    # p = entry1.get()
# for j in range (0, dlzka_slova -1):
# if zoznam_slov[por_cis_slova-1][j]==p:
# can.create_text( x_zaciatok+j*(medzera_medzi_obdlznikmi+sirka_obdlznika),
# y_zaciatok,
# text=p , fill="black")
# can.create_text( 100, 100, "Skuska" )


# can.create_rectangle( 100, 200, 300 ,400 )

print("Pocet slov:", str(pocet_slov))
print("Zvolene cislo slova:", str(por_cis_slova))
print("Zvolene slovo je ", zoznam_slov[por_cis_slova - 1])
print("Dlzka slova je ", str(dlzka_slova))

# s = input( "Zadaj daco hnupe !" )

main.mainloop()
