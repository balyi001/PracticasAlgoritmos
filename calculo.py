
porcentaje_descuento = 0.10 

try:

    valor_compra = float(input("Ingrese el valor total de la compra: "))
    descuento = 0
    
    if valor_compra >= 100000:
        descuento = valor_compra * porcentaje_descuento
        print("¡Felicidades! Se aplica un 10% de descuento.")
        print(f"Valor del descuento aplicado: ${round(descuento, 2)}")
    else:
        print("No se aplica ningún descuento (la compra debe ser mayor o igual a $100000).")
        
    valor_final = valor_compra - descuento
    
    print("\n--- Resumen de la Compra ---")
    print(f"Valor inicial de la compra: ${round(valor_compra, 2)}")
    print(f"Valor final a pagar: ${round(valor_final, 2)}")

except ValueError:
    print("\nError: Por favor, ingrese un número válido para el valor de la compra.")
