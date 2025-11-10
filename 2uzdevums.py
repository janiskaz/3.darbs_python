"""
    Funkcija koks akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to summas kvadrātu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    parādot skaitli ar diviem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu summa
"""
def koks(a,b,c):
    summa = a + b + c # jāiegūst visu trīs skaitļu summa
    return summa*summa # summas kvadrāts

# piemēri --> visi varianti
rezultats1 = koks(1,2,3) # tiek apskatīti veseli skaitļi
rezultats2 = koks(2.5,3.5,4.0) # visi skaitļi ir float
rezultats3 = koks(-1,5,2)

# datu izvads
print(f"Rezultāts 1: {rezultats1:.2f}")
print(f"Rezultāts 2: {rezultats2:.2f}")
print(f"Rezultāts 3: {rezultats3:.2f}")