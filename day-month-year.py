#Pon el dia, mes y año
dia = int(input("Dime el dia"))
mes = int(input("Dime el mes"))
year = int(input("Dime el dime el año"))

#Comprueba que la fecha es real
if  mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias = 30
elif mes == 2:
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
        dias = 29
    else:
        dias = 28
else:
    print("Fecha incorrecta")

if dia < 0 or dia > dias:
    print("Fecha incorrecta")
else:
    #Imprime la fecha aceptada
    print(dia, "/", mes, "/", year)
