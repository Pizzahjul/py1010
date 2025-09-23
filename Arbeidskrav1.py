"""
Arbeidskrav1 
Lars Magne Orrebakken (orrebakken@gmail.com)
Oppdatert 2025 09 22
"""

TFA = 8.38*365 # Trafikkforsikringavgift per år
EF = 5000 # Elbilforsikring per år
BF = 7500 # Bensinbilforsikring per år
KM = 8000 # KM forbruk per år
DEB = 0.2*KM*2 # Drivstoffbruk elbil
DBB = 1*KM # Drivstoff forbruk bensinbil
BOMEB = 0.1*KM #Bomavgift for elbil
BOMBB = 0.3*KM #Bomavfigt for bensinbil

EB = TFA+EF+DEB+BOMEB #Kostnad for ebil per år
BB = TFA+BF+DBB+BOMBB #Kostnad for bensinbil per år

DIF = BB - EB # Kostnadsdifferanssen mellom Bensinbil og Elbil

print("Med", KM, "KM kjørt hvert år vil det koste",EB,"NOK for elbil og",BB," NOK for bensinbil. Dette utgjør en fordel til elbil på",DIF,"NOK" )
