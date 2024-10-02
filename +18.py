permatrago = int(input("Dime tu edad: "))
if permatrago < 18:
  #Impide el acceso
    print("Acceso denegado, solo +18")
elif permatrago >= 18:
  #Redirecciona a la pagina 
    print("Bienvenido")
else:
  #En caso de cualquier tipo de error saldira este mensaje
    print("Error en el sistema")

print("Fin del programa")
