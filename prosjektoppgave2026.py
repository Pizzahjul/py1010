#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 26
Updated on Mon Mar 23 26

@author: Lars Magne Orrebakken (orrebakken@gmail.com)
"""

import numpy as np #Legger inn numpy biblioteket
import matplotlib.pyplot as plt # legger inn matplotlib biblioteket
import pandas as pd #legger inn pandas bibliotek

# Oppgave A

filnavn = "support_uke_24.xlsx" #definerer fil

data = pd.read_excel(filnavn) #Leser xlsx fil ved hjelp av pandas

u_dag = data["Ukedag"].values #Lagrer data i kolonne 1 i array

kl_slett = data["Klokkeslett"].values #Lagrer data i kolonne 2 i array

varighet = data["Varighet"].values #Lagrer data i kolonne 3 i array

score = data["Tilfredshet"].values #Lagrer data i kolonne 4 i array



# Oppgave B

mandag = np.count_nonzero(u_dag == 'Mandag') #Teller hvor mange som har ringt mandag
tirsdag = np.count_nonzero(u_dag == 'Tirsdag') #Teller hvor mange som har ringt tirsdag
onsdag = np.count_nonzero(u_dag == 'Onsdag') #Teller hvor mange som har ringt osndag
torsdag = np.count_nonzero(u_dag == 'Torsdag') #Teller hvor mange som har ringt torsdag
fredag = np.count_nonzero(u_dag == 'Fredag') #Teller hvor mange som har ringt fredag

# Legger antall per dag inn i et array
antall_pr_dag = np.array([mandag,tirsdag, onsdag, torsdag, fredag]) 
# Legger inn dagene i et array
dager = np.array(["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"])

# Lager stolpediagram med antall og hvilke dager
plt.figure(1)
plt.bar(dager,antall_pr_dag)
plt.grid()
plt.xlabel("Dager")

#Oppgave C

# Henter ut korteste samtale tid ved hjelp av numpy
kortest_tid = np.min(varighet) 
# Henter ut lengste samtale tid ved hjelp av numpy
lengst_tid = np.max(varighet)
#skriver ut svaret med informativ tekst
print("Den korteste samtalen i uke 24 var:", kortest_tid)
print("Den lengste samtalen i uke 24 var:", lengst_tid)

#Oppgave D
# Gjør om tidene til sekunder
sek = np.array([int(h)*3600 + int(m)*60 + int(s) for h,m,s in (t.split(":") for t in varighet)])
# Regner om til gjennomsnitt ved hjelp av numpy
gjsnitt = np.mean(sek)

# Gjør sekundene av gjennomsnittet om til minutter og sekunder
minutter = int(gjsnitt // 60)
sekunder = int(gjsnitt % 60)

# Skriver ut resultatet med passende tekst
print("Gjennomsnitt for samtaler i uke 24 er:", minutter, "minutter og",sekunder,"sekunder.")

#Oppgave e
# Henter bare ut timene, fjerner minutter og sekunder.
timer = np.array([int(t.split(":")[0]) for t in kl_slett])

#Lager liste med vaktene i de forskjellige tidsrommene timene passer inn i
vakter = [
np.sum((timer >= 8) & (timer < 10)), # 08-10
np.sum((timer >= 10) & (timer < 12)),# 10-12
np.sum((timer >= 12) & (timer < 14)),# 12-14
np.sum((timer >= 14) & (timer < 16)) # 14-16
]
# Label for timene i samme rekkefølge som listen er lagd for vakter
labels = ["08-10", "10-12", "12-14", "14-16"]

# Skriver alt ut på en ny figur som kakediagram.
plt.figure(2)
plt.pie(vakter, labels=labels, autopct='%1.1f%%')
plt.title("Supporthenvendelser uke 24")
plt.show()

#oppgave f
def beregn_nps(score):
    # Filterer bort ugyldige svar og ingen svar
    gyldige = [s for s in score if s is not None and 1 <= s <= 10]

    # Sjekker om listen har gyldige svar, retunerer tekst om det er ingen gyldige svar i listen.
    if len(gyldige) == 0:
        print("Ingen gyldige tilbakemeldinger.")
        return
    # Totale antall gyldige svar i score
    ant = len(gyldige)
    
    #Antall positive svar ut ifra oppgavetekstens parametere
    pos = sum(1 for s in gyldige if s >= 9)
    #Antall negative svar ut ifra oppgavetekstens parametere
    neg = sum(1 for s in gyldige if s <= 6)
    #Regner ut NPS ut ifra hva som stod i oppgaveteksten "NPS = % positive kunder - % negative kunder"
    nps = (pos / ant) * 100 - (neg / ant) * 100

    #skriver ut resulatat med 2 desimaler
    print(f"NPS: {nps:.2f}%")

# Kaller funksjonen med listen score fra oppgave A
beregn_nps(score)
