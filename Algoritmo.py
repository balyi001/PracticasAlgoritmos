
try:

    nota1 = float(input("Ingrese la nota de la actividad 1: "))
    nota2 = float(input("Ingrese la nota de la actividad 2: "))
    nota3 = float(input("Ingrese la nota de la actividad 3: "))
    nota4 = float(input("Ingrese la nota de la actividad 4: "))
    
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    if promedio >= 3.5:
        mensaje = "Aprobado"
        print(f"El aprendiz ha sido {mensaje}")
    else:
        mensaje = "Reprobado"
        print(f"El aprendiz ha sido {mensaje}")
        print("Recomendacion: el aprendiz debe realizar refuerzo")
        
    print("\nPromedio final obtenido")
    print(f"Estado: {mensaje}")
    
except ValueError:
    print("\nError: Por favor, ingrese solo números válidos para las notas.")

