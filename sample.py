edad = int(input("Ingrese su edad "))
inscrito = bool(input("Esta Inscrito "))
Judicial = bool(input("Tiene procedimientos Judiciales en marcha "))

if edad >= 18 and inscrito == True and Judicial == False:
    print("Puedes ingresar, ya que estas inscrito y eres mayor de edad")

elif edad >= 18 and inscrito == False:
    print(f"No puedes entrar, tienes {edad} años pero no estas inscrito")
    
else: print(f"no puedes entrar")