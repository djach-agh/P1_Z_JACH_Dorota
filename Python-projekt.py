#-------------------------------------------------------------------------------
# Name:        Modul 1
# Purpose:
#
# Author:      Dorota Jach
#
# Created:     05.04.2022
# Copyright:   (c) dorota 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
from datetime import date
import tkinter as tk
from tkinter import*
import os.path
#FUNKCJE UZYWANE W GRZE
def zakończ1():
    sGui.quit()
    sGui.destroy()
    quit()
def zakończ2():
    root.quit()
    root.destroy()
    sGui.quit()
    sGui.destroy()
    quit()
def gracz1():
    global g
    g=1
    sGui.quit()
    sGui.destroy()

def gracz2():
    global g
    g=2
    sGui.quit()
    sGui.destroy()

#DANE PIERWOTNE

alfabet=['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n',
'o','ó','p','r','s','ś','t','u','w','y','z','ź','ż']
samogłoski=['a','ą','e','ę','i','o','ó','u','y']

#LISTY SŁOW Z PODZIAŁEM NA KATEGORIE
ASTRONOMIA=['ciało niebieskie','gromada gwiazd','planeta karłowata','pas planetoid','układ planetarny','droga mleczna','mars','wenus','saturn','pluton']
FILM=['film familijny','dramat społeczny','dramat sensacyjny','dramat obyczajowy','film katastroficzny','scenariusz','rola','kino','recenzja','kaskader']
OWOCE=['biała porzeczka','borówka amerykańska','czarna porzeczka','czarny bez','dzika róża','jabłko','pomidor','gruszka']
MATEMATYKA=['oś odciętych','pochodna','analiza matematyczna','algebra','całka','potęga','pierwiastek']
FOTOGRAFIA=['aparat analogowy','aparat cyfrowy','rybie oko','filtr polaryzacyjny','balans bieli','żabia perspektywa','klisza','obiektyw','statyw']
ZAWODY=['dyrektor szkoły','nauczyciel akademicki','pracownik biurowy' ,'realizator dźwięku','lekarz','policjant','urzędnik']
CYTATY=['marian tu jest jakby luksusowo','nie wiem nie znam się nie orientuję się zarobiony jestem','bo to zła kobieta była','podejdź no do płota jako i ja podchodzę']
PRZYSŁOWIA=['prawda jak oliwa zawsze na wierzch wypływa','przyganiał kocioł garnkowi, a sam smoli','szczęśliwi czasu nie liczą','szewc bez butów chodzi','szlachcic na zagrodzie równy wojewodzie']
Cytaty={'krokodyla daj mi luby':' utworu Zemsta ','co ci powiem to ci powiem ale ci powiem':' serialu Janosik','niech moc będzie z tobą' :' filmu Gwiezdne wojny','jak jest zima to musi być zimno':' filmu Miś','życie jest jak pudełko czekoladek ':' filmu Forrest Gump','mój mąż z zawodu jest dyrektorem':' filmu Poszukiwany, poszukiwana','być albo nie być oto jest pytanie':' utworu Hamlet','przybyłem zobaczyłem zwyciężyłem':' sentencji Juliusza Cezara','historia nauczycielką życia':' sentencji Cycerona','dobrze widzi się tylko sercem':'książki Mały Książe','kto czyta książki żyje podwójnie':' słowa Umberto Eco','życie jest śmiechu warte więc się śmieję':' z utworu  Quo Vadis','ty będziesz duszą mojej duszy':'z utworu Quo Vadis','koniec i bomba a kto czytał ten trąba':' z utworu Ferdydurke','aby oszukać świat naśladuj świat':'z dramatu Makbet','marian tu jest jakby luksusowo':' z filmu Kogel Mogel'
,'bo to zła kobieta była':' filmu Psy','podejdź no do płota jako i ja podchodzę':' filmu Sami Swoi' }
TYTUŁY=['teoria wielkiego podrywu','żona podróżnika w czasie', 'alicja w krainie czarów','ania z zielonego wzgórza','rozważna i romantyczna']

#POBIERANIE  DANYCH Z PLIKU TEKSTOWEGO Z UWZGLĘDNIENIEMM POLSKICH ZNAKOW
#TEST CZY PLIK ISTNIEJE
file_exist = os.path.exists("ASTRONOMIA.txt")
if file_exist==True:
    plik=open("ASTRONOMIA.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        ASTRONOMIA+=tekst.splitlines()
file_exist = os.path.exists("FILM.txt")
if file_exist==True:
    plik=open("FILM.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        FILM+=tekst.splitlines()

if file_exist==True:
    plik=open("FILM.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        FILM+=tekst.splitlines()

file_exist = os.path.exists("FOTOGRAFIA.txt")
if file_exist==True:
    plik=open("FOTOGRAFIA.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        FOTOGRAFIA+=tekst.splitlines()

file_exist = os.path.exists("MATEMATYKA.txt")
if file_exist==True:
    plik=open("MATEMATYKA.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        MATEMATYKA+=tekst.splitlines()
file_exist = os.path.exists("OWOCE.txt")
if file_exist==True:
    plik=open("OWOCE.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        OWOCE+=tekst.splitlines()
file_exist = os.path.exists("ZAWODY.txt")
if file_exist==True:
    plik=open("ZAWODY.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        ZAWODY+=tekst.splitlines()

file_exist = os.path.exists("CYTATY.txt")
if file_exist==True:
    plik=open("CYTATY.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        CYTATY+=tekst.splitlines()
file_exist = os.path.exists("PRZYSŁOWIA.txt")
if file_exist==True:
    plik=open("PRZYSŁOWIA.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        PRZYSŁOWIA+=tekst.splitlines()
file_exist = os.path.exists("TYTUŁY.txt")
if file_exist==True:
    plik=open("TYTUŁY.txt",encoding="utf-8")
    if plik.readable():
        tekst=plik.read()
        TYTUŁY+=tekst.splitlines()


# Wartosci
runda=1
punkty=0
p=0
punkty_komputer1=0
pk=0

#FUNKCJA ZAMYKAJĄCA OKIENKO
def zamknij():
    sGui.quit()
    sGui.destroy()


#OKIENKO GUI
sGui=tk.Tk()
sGui.geometry('800x800+1+1')
sGui.title('Koło Fortuny')
start_image=tk.PhotoImage(file='Start.png')
background_label=tk.Label(sGui,image=start_image)
background_label.place(relwidth=1,relheight=1)
sbutton=tk.Button(text='START',command=zamknij,width=14,height=2,font=('Courier',21,'bold'),background='orange',foreground='white',borderwidth=6).place(x=270,y=370)
sGui.mainloop()
sGui=tk.Tk()
sGui.geometry('800x800+1+1')
sGui.title('Koło Fortuny')
sLabel=tk.Label(text='WITAJ W UPROSZCZONEJ WERSJI GRY KOŁO FORTUNY',font=('Courier',15,'bold')).place(x=130,y=140)
Label=tk.Label(text='ZASADY GRY',font=('Courier',15,'bold')).place(x=345,y=240)
sLabel=tk.Label(text='1.Zgadujesz jakie litery są ukryte w haśle, wpisuj je małymi literami!!!\n2.Jeśli znasz już hasło wpisz je ze małymi literami ze spacją i polskimi znakami.\n3.Za samogłoski jeśli znajdują się w haśle odejmuje się 200 punktow,\nza społgłoski dostaje się wylosowaną przez koło premię z puli(0,1000).\n4.Jesli wylosujesz z puli zero tracisz wszystkie punkty.\n5.Jeśli twoja premia wyniesie 600 dostajesz dodatkowe 600 punktow.\n6.Jeśli wpiszesz poprawnie całe hasło Twoj przeciwnik traci wszystkie punkty.\n7.Gra składa się z 5 rund i finału dla najlepszego gracza.',font=('Courier',11,'bold')).place(x=40,y=280)
sbutton=tk.Button(text='DALEJ',command=zamknij,width=20,height=3,font=('Courier',15,'bold'),background='orange').place(x=280,y=500)
sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
sGui.mainloop()

sGui=tk.Tk()
sGui.geometry('800x800+1+1')
sGui.title('Koło Fortuny')
background_image=tk.PhotoImage(file='Tlo.png')
background_label=tk.Label(sGui,image=background_image)
background_label.place(relwidth=1,relheight=1)
sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
sLabel=tk.Label(text='Ilu graczy 1 czy 2?',font=('Courier',20,'bold'),background='white').place(x=230,y=400)
def gracz1():
    global j
    j=1
    sGui.quit()
    sGui.destroy()

def gracz2():
    global j
    j=2
    sGui.quit()
    sGui.destroy()
sbutton=tk.Button(text='1',command=gracz1,width=12,height=3,font=('Courier',18,'bold'),background='orange').place(x=200,y=500)
sbutton=tk.Button(text='2',command=gracz2,width=12,height=3,font=('Courier',18,'bold'),background='orange').place(x=400,y=500)
sGui.mainloop()
def imie ():
    global gracz1
    gracz1=str(gracz.get())
    sGui.quit()
    sGui.destroy()
def imie2 ():
    global gracz2
    gracz2=str(gracz.get())
    sGui.quit()
    sGui.destroy()
if j==1:
    sGui=Tk()
    sGui.geometry('800x100+1+400')
    sGui.title('GRACZ1 -   PODAJ SWOJE IMIĘ LUB NICK')
    gracz=Entry(sGui,background='orange',width=40)
    gracz.pack(anchor='center')
    przycisk=Button(sGui,text="ROZPOCZNIJ GRĘ",command=imie,background='yellow',width=15,height=2).pack(side='bottom')
    sGui.mainloop()

if j==2:
    sGui=Tk()
    sGui.geometry('800x100+1+400')
    sGui.title('GRACZ1 -   PODAJ SWOJE IMIĘ LUB NICK')
    gracz=Entry(sGui,background='orange',width=40)
    gracz.pack(anchor='center')
    Button(sGui,text="DALEJ",command=imie,background='yellow',width=15,height=2).pack(side='bottom')
    sGui.mainloop()
    sGui=Tk()
    sGui.geometry('800x100+1+400')
    sGui.title('GRACZ2 -   PODAJ SWOJE IMIĘ LUB NICK')
    gracz=Entry(sGui,background='orange',width=40)
    gracz.pack(anchor='center')
    Button(sGui,text="ROZPOCZNIJ GRĘ",command=imie2,background='yellow',width=15,height=2).pack(side='bottom')
    sGui.mainloop()

def literaz ():
    global litera
    litera=str(litera_zgaduje.get())
    root.quit()
    root.destroy()
    sGui.quit()
    sGui.destroy()

def literakz ():
    global literak
    literak=str(literak_zgaduje.get())
    root.quit()
    root.destroy()
    sGui.quit()
    sGui.destroy()


#Początek gry
while runda<5:
    rundatekst=(f'\nRUNDA {runda}\n')

    #Kolejna runda
    runda+=1

    #Inicjowanie pustych list
    słowa=[]
    łatwe=[]
    trudne=[]
    kategoria=[]

    #Wybor kategorii
    kategoria_gry=random.randrange(1,7)
    if int(kategoria_gry)==1:
        kategoria=ASTRONOMIA
        kat='KATEGORIA: ASTRONOMIA'
    if int(kategoria_gry)==2:
        kategoria=FILM
        kat='KATEGORIA: FILM'
    if int(kategoria_gry)==3:
        kategoria=FOTOGRAFIA
        kat='KATEGORIA: FOTOGRAFIA'
    if int(kategoria_gry)==4:
        kategoria=OWOCE
        kat='KATEGORIA: OWOCE'
    if int(kategoria_gry)==5:
        kategoria=MATEMATYKA
        kat='KATEGORIA: MATEMATYKA'
    if int(kategoria_gry)==6:
        kategoria=ZAWODY
        kat='KATEGORIA: ZAWODY'


    #Przypisywanie hasel do poziomow trudnosci
    for i in range(0,len(kategoria)):
        c=kategoria[i]
        if len(c)<=6:
            łatwe.append(c)
        elif 6<len(c)<10:
            trudne.append(c)


    # Wybor poziomu trudnosci gry
    if runda<3:
        słowa=łatwe
    if runda>=3:
        słowa=trudne


    b=słowa[random.randrange(0,len(słowa))]
    print(b)
    #losowanie słowa i ukrycie jego liter za znakiem '_'
    lista=[]
    for l in range(0,len(b)):
            if b[l]==" ":
                lista.insert(l," ")
            else:
                lista.insert(l,"_")

    ukryteslowo=(f'{lista}\n')
    sGui=Tk()
    sGui.geometry('800x800+1+1')
    sGui.title('Koło Fortuny')
    background_image=tk.PhotoImage(file='Tlo.png')
    background_label=tk.Label(sGui,image=background_image)
    background_label.place(relwidth=1,relheight=1)
    sLabel=tk.Label(text=rundatekst,font=('Courier',21,'bold'),background='white').place(x=350,y=200)
    sLabel=tk.Label(sGui,text=kat,font=('Courier',21,'bold'),background='white').place(x=200,y=300)
    sLabel=tk.Label(text=ukryteslowo,font=('Courier',17,'bold'),background='white').pack(anchor='center',side='bottom',expand=YES)
    sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
    sbutton=tk.Button(text='Zaczynamy',command=zamknij,width=20,height=4,font=('Courier',15,'bold'),background='orange').place(x=280,y=550)
    sGui.mainloop()
 #Początek zgadywania liter
    while "_" in lista :
        komunikat=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p')
        sGui=Tk()
        sGui.geometry('800x800+1+1')
        sGui.title('Koło Fortuny')
        sLabel=tk.Label(text=kat,font=('Courier',15,'bold')).place(x=270,y=100)
        sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
        sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ2,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
        sLabel=tk.Label(text=(f'{lista}\n'),font=('Courier',17,'bold')).pack(anchor='center',side='bottom',expand=YES)
        root=Tk()
        root.geometry('600x100+860+550')
        root.title('GRACZ1 -   PODAJ LITERĘ   (CAŁE HASŁO  LUB q PRZERYWAJĄ RUNDĘ)')
        litera_zgaduje=Entry(root,background='orange',width=40)
        litera_zgaduje.pack()
        Button(root,text="DALEJ",command=literaz,width=15,height=2,background='yellow').pack(side='bottom')
        root.mainloop()
        sGui.mainloop()

        #Wpisanie całego hasla przerywa rundę i pozbawia przeciwnika punktow
        if litera==b:
            punkty+=1000
            punkty_komputer1=0
            sGui=Tk()
            sGui.geometry('800x800+1+1')
            sGui.title('Koło Fortuny')
            sLabel=tk.Label(text=('HASŁO:',b.upper()),font=('Courier',22,'bold')).pack(anchor='center',side='bottom',expand=YES)
            sLabel=tk.Label(text=(f'GRACZ 1 masz 1000 punktow za poprawne hasło'),font=('Courier',15,'bold')).place(x=170,y=500)
            sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
            sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
            sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
            sGui.mainloop()
            break

        if  litera=='q':
            sGui=Tk()
            sGui.geometry('800x800+1+1')
            sGui.title('Koło Fortuny')
            sLabel=tk.Label(text=('HASŁO:',b.upper()),font=('Courier',22,'bold')).pack(anchor='center',side='bottom',expand=YES)
            sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
            sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
            sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
            sGui.mainloop()
            break

        else:
            if litera  in b and litera!="":
                if litera not in lista:
                    for i in range(0,len(b)):
                        if b[i]==litera:
                            del lista[i]
                            lista.insert(i,litera.upper())
                    sGui=Tk()
                    sGui.geometry('800x800+1+1')
                    sGui.title('Koło Fortuny')
                    sLabel=tk.Label(text=kat,font=('Courier',15,'bold')).place(x=270,y=100)
                    sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                    sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ2,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                    sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                    sLabel=tk.Label(text=(f'{lista}\n'),font=('Courier',17,'bold')).pack(anchor='center',side='bottom',expand=YES)
                    if litera in samogłoski:
                        sLabel=tk.Label(text=(f'GRACZ 1 Twoja premia za samogłoskę wynosi wynosi -200'),font=('Courier',12,'bold')).place(x=150,y=550)
                        punkty-=200
                    else:
                        premia=random.randrange(0,1001,150)
                        if premia==0:
                            punkty=0
                            sLabel=tk.Label(text=(f'BANKRUT'),font=('Courier',25,'bold')).place(x=350,y=500)
                        if premia==600:
                            punkty+=600
                        sLabel=tk.Label(text=(f'GRACZ 1 Twoja premia za każdą literę wynosi  {premia}'),font=('Courier',11,'bold')).place(x=200,y=550)
                        lwl=b.count(litera)
                        sLabel=tk.Label(text=(f'Litera GRACZA 1 wystąpiła {lwl} razy\n'),font=('Courier',12,'bold')).place(x=250,y=500)
                        p=lwl*premia
                        punkty+=p
                    sLabel=tk.Label(text=komunikat,font=('Courier',17,'bold')).place(x=70,y=700)
                    sGui.mainloop()
            else:
                sGui=Tk()
                sGui.geometry('800x800+1+1')
                sGui.title('Koło Fortuny')
                sLabel=tk.Label(text=kat,font=('Courier',15,'bold')).place(x=270,y=100)
                sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                sLabel=tk.Label(text=(f'{lista}\n'),font=('Courier',17,'bold')).pack(anchor='center',side='bottom',expand=YES)
                sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ2,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                if j==1:
                    literak=alfabet[random.randrange(0,len(alfabet))]
                    sLabel=tk.Label(text=(f'Komputer zgaduje :{literak}'),font=('Courier',16,'bold')).place(x=270,y=450)
                    sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                if j==2:
                    root=Tk()
                    root.geometry('600x100+860+550')
                    root.title('GRACZ2-   PODAJ LITERĘ   (CAŁE HASŁO  LUB q PRZERYWAJĄ RUNDĘ)')
                    literak_zgaduje=Entry(root,background='orange',width=40)
                    literak_zgaduje.pack()
                    Button(root,text="DALEJ",command=literakz,width=15,height=2,background='yellow').pack(side='bottom')
                    root.mainloop()
                if literak not in b:
                    sLabel=tk.Label(text='Tej litery nie ma w haśle',font=('Courier',15,'bold')).place(x=250,y=500)
                sGui.mainloop()


                if literak==b:
                    punkty_komputer1+=1000
                    punkty=0
                    sGui=Tk()
                    sGui.geometry('800x800+1+1')
                    sGui.title('Koło Fortuny')
                    sLabel=tk.Label(text=('HASŁO:',b.upper()),font=('Courier',22,'bold')).pack(anchor='center',side='bottom',expand=YES)
                    sLabel=tk.Label(text=(f'GRACZ 1 masz 1000 punktow za poprawne hasło'),font=('Courier',15,'bold')).place(x=170,y=500)
                    sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                    sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                    sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                    sGui.mainloop()
                    break



                if literak=='q':

                    sGui=Tk()
                    sGui.geometry('800x800+1+1')
                    sGui.title('Koło Fortuny')
                    sLabel=tk.Label(text=('HASŁO:',b.upper()),font=('Courier',22,'bold')).pack(anchor='center',side='bottom',expand=YES)
                    sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                    sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                    sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                    sGui.mainloop()
                    break


                while literak in b and literak!="" and literak not in lista:
                    sGui=Tk()
                    sGui.geometry('800x800+1+1')
                    sGui.title('Koło Fortuny')
                    sLabel=tk.Label(text=kat,font=('Courier',15,'bold')).place(x=270,y=100)
                    sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                    sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                    sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ2,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                    sLabel=tk.Label(text=(f'{lista}\n'),font=('Courier',17,'bold')).pack(anchor='center',side='bottom',expand=YES)

                    if literak not in lista:
                        for i in range(0,len(b)):
                            if b[i]==literak:
                                del lista[i]
                                lista.insert(i,literak.upper())
                        if literak in samogłoski:
                            sLabel=tk.Label(text=(f'GRACZ 2 Twoja premia za samogłoskę wynosi wynosi -200'),font=('Courier',12,'bold')).place(x=150,y=450)
                            punkty_komputer1-=200


                        else:
                            premia=random.randrange(0,1001,150)
                            if premia==0:
                                punkty_komputer1=0
                                sLabel=tk.Label(text=(f'BANKRUT'),font=('Courier',25,'bold')).place(x=350,y=500)
                            if premia==600:
                                punkty_komputer1+=600
                            sLabel=tk.Label(text=(f'GRACZ 2 Twoja premia za każdą literę wynosi  {premia}'),font=('Courier',14,'bold')).place(x=200,y=550)
                            lwlk=b.count(literak)
                            pk=lwlk*premia
                            sLabel=tk.Label(text=(f'Litera GRACZA 2 wystąpiła {lwlk} razy\n'),font=('Courier',14,'bold')).place(x=250,y=500)
                            punkty_komputer1+=pk
                            sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                    sGui.mainloop()

                    if '_' not in lista:
                        break


                    else:
                        sGui=Tk()
                        sGui.geometry('800x800+1+1')
                        sGui.title('Koło Fortuny')
                        sLabel=tk.Label(text=kat,font=('Courier',15,'bold')).place(x=270,y=100)
                        sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                        sLabel=tk.Label(text=(f'{lista}\n'),font=('Courier',17,'bold')).pack(anchor='center',side='bottom',expand=YES)
                        sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ2,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                        if j==1:
                            literak=alfabet[random.randrange(0,len(alfabet))]
                            sLabel=tk.Label(text=(f'Komputer zgaduje :{literak}'),font=('Courier',16,'bold')).place(x=270,y=450)
                            sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                        if j==2:
                            root=Tk()
                            root.geometry('600x100+860+550')
                            root.title('GRACZ2 -   PODAJ LITERĘ   (CAŁE HASŁO  LUB q PRZERYWAJĄ RUNDĘ)')
                            literak_zgaduje=Entry(root,background='orange',width=40)
                            literak_zgaduje.pack()
                            Button(root,text="DALEJ",command=literakz,width=15,height=2,background='yellow').pack(side='bottom')
                            root.mainloop()
                        sGui.mainloop()

                        if literak==b:
                            punkty_komputer1+=1000
                            punkty=0
                            sGui=Tk()
                            sGui.geometry('800x800+1+1')
                            sGui.title('Koło Fortuny')
                            sLabel=tk.Label(text=('HASŁO:',b.upper()),font=('Courier',22,'bold')).pack(anchor='center',side='bottom',expand=YES)
                            sLabel=tk.Label(text=(f'GRACZ 2 masz 1000 punktow za poprawne hasło'),font=('Courier',15,'bold')).place(x=170,y=500)
                            sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                            sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                            sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                            sGui.mainloop()
                            break


                        if literak=='q':
                            sGui=Tk()
                            sGui.geometry('800x800+1+1')
                            sGui.title('Koło Fortuny')
                            sLabel=tk.Label(text=('HASŁO:',b.upper()),font=('Courier',22,'bold')).pack(anchor='center',side='bottom',expand=YES)
                            sLabel=tk.Label(text=(f'Gracz1: {punkty} p                     Gracz2: {punkty_komputer1} p'),font=('Courier',17,'bold')).place(x=70,y=700)
                            sbutton=tk.Button(text='DALEJ',command=zamknij,width=19,height=3,font=('Courier',12,'bold'),background='orange',borderwidth=4).place(x=300,y=650)
                            sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
                            sGui.mainloop()
                            break
                if j==2 and (literak=='q'or literak==b or '_' not in lista):
                    break


if punkty<punkty_komputer1 and j==1:
    sGui=Tk()
    sGui.geometry('800x800+1+1')
    sGui.title('Koło Fortuny')
    background_image=tk.PhotoImage(file='Tlo.png')
    background_label=tk.Label(sGui,image=background_image)
    background_label.place(relwidth=1,relheight=1)
    sLabel=tk.Label(text=(f'GRACZ1 ma {punkty} punktów.\nGRACZ 2 ma {punkty_komputer1}. Wygrał GRACZ 2'),font=('Courier',14,'bold'),background='white').place(x=270,y=400)
    sLabel=tk.Label(text='KONIEC GRY :(',font=('Courier',29,'bold'),background='white').place(x=300,y=200)
    sbutton=tk.Button(text='KONIEC',command=zamknij,width=20,height=4,font=('Courier',15,'bold'),background='white').place(x=300,y=550)
    sGui.mainloop()


else:
    if punkty>=punkty_komputer1 and j==1:
        wygrana=punkty
        zwyciezca=gracz1
        sGui=Tk()
        sGui.geometry('800x800+1+1')
        sGui.title('Koło Fortuny')
        background_image=tk.PhotoImage(file='Tlo.png')
        background_label=tk.Label(sGui,image=background_image)
        background_label.place(relwidth=1,relheight=1)
        sLabel=tk.Label(text=(f'GRACZ 1 ma {punkty} punktów.\nGRACZ 2 ma {punkty_komputer1}.'),font=('Courier',14,'bold'),background='white').place(x=270,y=400)
        sLabel=tk.Label(text=(f'   ****** Finał ******\n   *****dla {gracz1}*****'),font=('Courier',25,'bold'),background='white').place(x=140,y=200)
        sbutton=tk.Button(text='FINAŁ',command=zamknij,width=18,height=3,font=('Courier',12,'bold'),background='orange').place(x=300,y=500)
        sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
        sGui.mainloop()


    if j==2:
        if punkty<punkty_komputer1:
            wygrana=punkty_komputer1
            zwyciezca=gracz2
            sGui=Tk()
            sGui.geometry('800x800+1+1')
            sGui.title('Koło Fortuny')
            background_image=tk.PhotoImage(file='Tlo.png')
            background_label=tk.Label(sGui,image=background_image)
            background_label.place(relwidth=1,relheight=1)
            sLabel=tk.Label(text=(f'**** Finał ****\n  *****dla {gracz2}****'),font=('Courier',25,'bold'),background='white').place(x=140,y=200)
            sbutton=tk.Button(text='FINAŁ',command=zamknij,width=18,height=3,font=('Courier',12,'bold'),background='orange').place(x=300,y=500)
            sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
            sGui.mainloop()


        else:
            wygrana=punkty
            zwyciezca=gracz1
            sGui=Tk()
            sGui.geometry('800x800+1+1')
            sGui.title('Koło Fortuny')
            background_image=tk.PhotoImage(file='Tlo.png')
            background_label=tk.Label(sGui,image=background_image)
            background_label.place(relwidth=1,relheight=1)
            sLabel=tk.Label(text=(f'GRACZ 1 ma {punkty} punktów.\nGRACZ 2 ma {punkty_komputer1}.'),font=('Courier',14,'bold'),background='white').place(x=270,y=400)
            sLabel=tk.Label(text=(f'   ****** Finał ******\n   *****dla {gracz1}*****'),font=('Courier',25,'bold'),background='white').place(x=140,y=200)
            sbutton=tk.Button(text='FINAŁ',command=zamknij,width=18,height=3,font=('Courier',12,'bold'),background='orange').place(x=300,y=500)
            sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
            sGui.mainloop()


    słowa.clear()
    kategoria.clear()

    #Wybor kategorii

    kategoria_gry=random.randrange(1,4)
    if int(kategoria_gry)==1:
        kategoria=CYTATY
    if int(kategoria_gry)==2:
        kategoria=PRZYSŁOWIA
    if int(kategoria_gry)==3:
        kategoria=TYTUŁY
    słowa=kategoria


    b=słowa[random.randrange(0,len(słowa))]
    print(b)

    lista=[]
    for l in range(0,len(b)):
        if b[l]==" ":
            lista.insert(l,"   ")
        else:
            lista.insert(l,"_")

    sGui.mainloop()
    k=0
    while k<4:
        sGui=Tk()
        sGui.geometry('1400x600+1+1')
        sGui.title('Koło Fortuny-FINAŁ')
        sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ2,width=12,height=2,font=('Courier',8,'bold'),background='pink').place(x=1300,y=10)
        sLabel=tk.Label(text='Podaj cztery rożne litery.Komputer również wylosuje litery',font=('Courier',15,'bold')).pack(anchor='center',side='top',expand=YES)
        literak=b[random.randrange(0,len(b))]

        if int(kategoria_gry)==1:
            sLabel=tk.Label(text='KATEGORIA: CYTATY',font=('Courier',15,'bold')).pack(anchor='center',side='top',expand=YES)
        if int(kategoria_gry)==2:
            sLabel=tk.Label(text='KATEGORIA: PRZYSŁOWIA',font=('Courier',15,'bold')).pack(anchor='center',side='top',expand=YES)
        if int(kategoria_gry)==3:
            sLabel=tk.Label(text='KATEGORIA: TYTUŁY',font=('Courier',15,'bold')).pack(anchor='center',side='top',expand=YES)
        if kategoria_gry==1:
            for cytat, autor in Cytaty.items():
                if cytat==b:
                    sLabel=tk.Label(text=(f'Cytat pochodzi z :{autor}'),font=('Courier',14,'bold')).pack(anchor='center',side='top',expand=YES)
        if literak in b:
            if literak not in lista:
                for i in range(0,len(b)):
                    if b[i]==literak:
                        del lista[i]
                        lista.insert(i,literak.upper())
        sLabel=tk.Label(text=(f'{lista}'),font=('Courier',10,'bold')).pack(anchor='center',side='top',expand=YES)
        sLabel=tk.Label(text=(f'Komputer wylosował literę: {literak.upper()}'),font=('Courier',12,'bold')).pack(anchor='center',side='top',expand=YES)
        def litery_finał ():
            global litera
            litera=str(litera.get())
            root.quit()
            root.destroy()
            sGui.quit()
            sGui.destroy()
        root=Tk()
        root.geometry('1400x100+1+630')
        root.title('PODAJ LITERĘ LUB CAŁE HASŁO')
        litera=Entry(root,background='orange',width=80)
        litera.pack()
        Button(root,text="DALEJ",command=litery_finał,width=15,height=2,background='yellow').pack()
        root.mainloop()
        if litera==b:
            global finał
            finał=b
            break
        if litera in b:
            if litera not in lista:
                for i in range(0,len(b)):
                    if b[i]==litera:
                        del lista[i]
                        lista.insert(i,litera.upper())
        k+=1
        sGui.mainloop()
    def finałowe():
        global finał
        finał=str(finał.get())
        root.quit()
        root.destroy()
        sGui.quit()
        sGui.destroy()
    if litera!=b:
        sGui=Tk()
        sGui.geometry('1400x600+1+1')
        sGui.title('Koło Fortuny-FINAŁ')
        sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ2,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
        sLabel=tk.Label(text=(f'{lista}'),font=('Courier',10,'bold')).pack(anchor='center',side='top',expand=YES)
        root=Tk()
        root.geometry('1400x100+1+630')
        root.title('PODAJ HASŁO FINAŁOWE')
        finał=Entry(root,background='orange',width=80)
        finał.pack()

        Button(root,text="DALEJ",command=finałowe,width=15,height=2,background='yellow').pack()
        root.mainloop()
        sGui.mainloop()



   #11.Jesli haslo jest poprawne to komputer losuje premię finałową
    if finał==b:
        sGui=tk.Tk()
        sGui.geometry('800x800+1+1')
        sGui.title('BRAWO JESTEŚ ZWYCIĘZCĄ')
        background_image=tk.PhotoImage(file='Tlo.png')
        background_label=tk.Label(sGui,image=background_image)
        background_label.place(relwidth=1,relheight=1)
        nagroda=random.randrange(10000,80001,5000)
        sLabel=tk.Label(text=(f'W finale zdobyłes {nagroda} punktow'),font=('Courier',15,'bold'),background='white').place(x=210,y=250)
        sLabel=tk.Label(text=(f'**Brawo wygrałes**\nKończysz grę z {wygrana+nagroda} punktów'),font=('Courier',16,'bold'),background='white').pack(anchor='center',side='bottom',expand=YES)
        sbutton=tk.Button(text='DALEJ',command=zamknij,width=18,height=3,font=('Courier',18,'bold'),background='orange').place(x=290,y=650)
        sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
        sGui.mainloop()
        WYNIKI=[]
        sGui=tk.Tk()
        sGui.geometry('800x800+1+1')
        sGui.title('LISTA WYNIKOW')
        sbutton=tk.Button(text='ZAKOŃCZ GRĘ',command=zakończ1,width=12,height=2,font=('Courier',8,'bold'),background='pink').pack(side='right',anchor='n')
        sLabel=tk.Label(text='GRACZ			WYNIK			  DATA',font=('Courier',11,'bold')).pack(side='top',anchor='center',expand=YES)
        sbutton=tk.Button(text='DALEJ',command=zamknij,width=15,height=2,font=('Courier',12,'bold'),background='orange').place(x=290,y=750)
        data=date.today()
        file_exist = os.path.exists("WYNIKI.txt")
        if file_exist==True:
            plik = open("WYNIKI.txt",'a+')
            tekst=plik.write(f'{zwyciezca.upper()}                       {nagroda+wygrana}p                        {data}\n')
            plik=open("WYNIKI.txt")
            if plik.readable():
                tekst=plik.read()
                WYNIKI+=tekst.splitlines()
            for wynik in WYNIKI:
                if WYNIKI.index(wynik)>=(len(WYNIKI)-6):
                    sLabel=tk.Label(text=(wynik),font=('Courier',10,'bold')).pack(side='bottom',anchor='center',expand=YES)

        sGui.mainloop()
        sGui=tk.Tk()
        sGui.geometry('800x800+1+1')
        sGui.title('BRAWO JESTEŚ ZWYCIĘZCĄ')
        background_image=tk.PhotoImage(file='TloZ.png')
        background_label=tk.Label(sGui,image=background_image)
        background_label.place(relwidth=1,relheight=1)
        sbutton=tk.Button(text='POŻEGNANIE MISTRZA',command=zamknij,width=18,height=3,font=('Courier',18,'bold'),background='white').place(x=270,y=570)
        sGui.mainloop()
        sGui=tk.Tk()
        sGui.geometry('800x800+1+1')
        sGui.title('BRAWO JESTEŚ ZWYCIĘZCĄ')
        background_image=tk.PhotoImage(file='Start.png')
        background_label=tk.Label(sGui,image=background_image)
        background_label.place(relwidth=1,relheight=1)
        sbutton=tk.Button(text='KONIEC',command=zamknij,width=18,height=3,font=('Courier',18,'bold'),background='white').place(x=270,y=370)
        sGui.mainloop()

    #12.Jesli hasŁo jest niepoprawne to gracz otrzymuje punkty zgromadzone w czasie gry
    else:
        sGui=tk.Tk()
        sGui.geometry('800x800+1+1')
        sGui.title('PRZEGRAŁES')
        background_image=tk.PhotoImage(file='Koniec.png')
        background_label=tk.Label(sGui,image=background_image)
        background_label.place(relwidth=1,relheight=1)
        sLabel=tk.Label(text=(f'HASŁO FINAŁOWE: {b.upper()}'),font=('Courier',10,'bold'),background='white').pack(anchor='center',side='top')
        sLabel=tk.Label(text=(f'Niestety, twoje hasło było niepoprawne,\nPrzynajmniej masz {wygrana} punktow'),font=('Courier',20,'bold'),background='white').place(x=70,y=250)
        sbutton=tk.Button(text='KONIEC',command=zamknij,width=18,height=3,font=('Courier',18,'bold'),background='grey').place(x=270,y=370)
        sGui.mainloop()
