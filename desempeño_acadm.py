# Pedir las 3 notas
try:
    nota1 = float(input("Dame la primera nota (0.0 a 5.0): "))
    nota2 = float(input("Dame la segunda nota (0.0 a 5.0): "))
    nota3 = float(input("Dame la tercera nota (0.0 a 5.0): "))
    nota4 = float(input("Dame la cuarta nota (0.0 a 5.0): "))
except ValueError:
    print("Error: Solo números.")
    exit()

# Calcular el promedio
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Mostrar el promedio para que el usuario lo vea
print(f"\nLa nota final es: {promedio:.1f}")

# Validar el rango de la nota
if promedio < 0 or promedio > 5:
    print("Error: La nota no está en el rango de 0 a 5.")

# Evaluación del desempeño
else:
    # Excelente (4.6 a 5.0)
    if promedio >= 4.6:
        print("Resultado: Excelente, ¡muchas felicidades!")
        
    # Sobresaliente (4.0 a 4.5)
    elif promedio >= 4.0:
        print("Resultado: Sobresaliente, revisa algunos temas.")

    # Aprobado (3.5 a 3.9)
    elif promedio >= 3.5:
        print("Resultado: Aprobado, debes estudiar más.")
        
    # Reprobado (menor a 3.4)
    else: # Esto cubre de 0.0 a 3.4
        print("Resultado: Reprobado, a estudiar para la próxima.")
    
    # Lógica del comportamiento (solo si es 3.5 o más)
    if promedio >= 3.5:
        
        comportamiento = input("¿El comportamiento fue 'bueno' o 'excelente'?: ").lower()

        print("\nMensaje extra:")
        
        if comportamiento == "excelente":
            print('Felicidades por tu buen trabajo y actitud.')
        elif comportamiento == "bueno":
            print('Sigue así para mejorar más.')
        else:
            print("No hay mensaje extra.")

print("\n--- FIN ---")