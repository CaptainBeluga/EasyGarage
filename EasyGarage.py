import sys
import sqlite3
import time

try:
    time.sleep(0.5)
    developer="App Developed by Cap Beluga\n"
    developer_colore=sys.stdout.shell
    developer_colore.write(developer,"COMMENT")
    print()
    time.sleep(0.5)
    logo="Audi Super Garage\n"
    colore_logo=sys.stdout.shell
    colore_logo.write(logo,"BUILTIN")
    print()
    time.sleep(1)
    opzione="Digita 1 per CREARE una SCHEDA del CLIENTE\n"
    opzione1="Digita 2 per LEGGERE una SCHEDA del CLIENTE già esistente\n"
    opzioni_colore=sys.stdout.shell
    opzioni_colore.write(opzione,"console")
    opzioni_colore.write(opzione1,"console")
    print()
    scegli=int(input("Scegli : "))      
    print()

    if scegli==1:
        
        database=input("Inserisci NOME DELLA SCHEDA del CLIENTE: ")
        conn=sqlite3.connect(database+".db")
        print()
        creazione="Creazione Scheda......\n"
        colore_creazione=sys.stdout.shell
        colore_creazione.write(creazione,"BUILTIN")
        time.sleep(2)
        print()
        success_scheda="SCHEDA CREATA CON SUCCESSO!\n"
        colore_success_scheda=sys.stdout.shell
        colore_success_scheda.write(success_scheda,"BUILTIN")
        print()
        info="Inserisci INFO\n"
        colore_info=sys.stdout.shell
        colore_info.write(info,"TODO")
        
        nome_auto=input("Scrivi MARCA dell'AUTO: ")
        nome=input("Scrivi NOME del PROPRIETARIO dell'AUTO: ")
        contatto=input("Scrivi EMAIL/TELEFONO del CLIENTE: ")
        modello=input("Scrivi MODELLO AUTO: ")
        city=input("Scrivi il PAESE e la Città di PROVENIENZA AUTO -- NOME COMPLETO PAESE --USA SIGLA della Città --SEPARA CON LA VIRGOLA: ")
        targa=input("Scrivi TARGA AUTO --Ricorda le LETTERE MAUSCOLE: ")
        riparo=input("Scrivi lo STATO --Riparato --Non Riparato:  ")

        schema="CREATE TABLE cliente (id int,nome_auto text,nome text,contatto text,modello text,city text,targa text,riparo text)"
        f="INSERT INTO cliente (nome_auto,nome,contatto,modello,city,targa,riparo) VALUES (?,?,?,?,?,?,?)"
        y=[nome_auto,nome,contatto,modello,city,targa,riparo]
        cur=conn.cursor()
        cur.execute(schema)
        cur.execute(f,y)
        conn.commit()
        conn.close()
        print()
        memorizzazione="Memorizzazione in corso......\n"
        colore_memorizzazione=sys.stdout.shell
        colore_memorizzazione.write(memorizzazione,"BUILTIN")
        print()
        time.sleep(2)
        success_memo="Dati Memorizzati Correttamente\n"
        colore_success_memo=sys.stdout.shell
        colore_success_memo.write(success_memo,"BUILTIN")

    if scegli==2:
        nome_scheda=input("Inserisci il NOME della SCHEDA del CLIENTE: ")
        print()
        time.sleep(2)
        leggi="SELECT * FROM cliente"
        conn=sqlite3.connect(nome_scheda+".db")
        cur=conn.cursor()
        cur.execute(leggi)
        leggi_stampa=cur.fetchall()
        print()
        print(leggi_stampa)
        conn.commit()
        conn.close()

        

except ValueError:
    print()
    errore="Ricorda di INSERIRE solo NUMERI!!!\n"
    colore_errore=sys.stdout.shell
    colore_errore.write(errore,"stderr")
    


#App Developed by Simone Patacchini       //FIRST UPDATE = Automatic Extension //  ::::::::::::::::::::::. Credits to SP27                        by Simone♥


