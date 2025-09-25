"""
Arbeidskrav1 
Lars Magne Orrebakken (orrebakken@gmail.com)
Oppdatert 2025 09 25
"""
KM = int(input("Hvor mange kilometer kjører du?: "))

TFA = 8.38*365 # Trafikkforsikringavgift per år
EF = 5000 # Elbilforsikring per år
BF = 7500 # Bensinbilforsikring per år
DEB = 0.2*KM*2 # Drivstoffbruk elbil per år
DBB = 1*KM # Drivstoff forbruk bensinbil per år
BOMEB = 0.1*KM #Bomavgift for elbil per år
BOMBB = 0.3*KM #Bomavfigt for bensinbil per år

EB = TFA+EF+DEB+BOMEB #Kostnad for ebil per år
BB = TFA+BF+DBB+BOMBB #Kostnad for bensinbil per år

DIF = BB - EB # Kostnadsdifferanssen mellom Bensinbil og Elbil

print("Med", KM, "KM kjørt hvert år vil det koste")
print(EB,"NOK for elbil")
print(BB,"NOK for bensinbil") 
print("Dette utgjør en fordel til elbil på",DIF,"NOK" )
