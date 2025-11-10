"""
Ir uzrakstīta programma Python, izmantojot funkciju.
Summējot divus norādītos veselos skaitļus. 
Tomēr, ja summa ir no 15 līdz 20, tā atgriezīs 20.

"""
def spec_summa(a, b): # a un b ir parametri
    kopaa=a+b
    if 15<=kopaa<=20:
        return 20
    else:
        return kopaa
    
# piemērs
skaitlis1=int(input("Ievadi pirmo skaitli: "))
skaitlis2=int(input("Ievadi otro skaitli: "))

rezultats=spec_summa(skaitlis1, skaitlis2) # jānorāda divi argumenti

print(f"Rezultāts ir: {rezultats}")