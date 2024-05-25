#Ejercicio CFE

ImpuestoDAP = 12.56

kwh = int(input("Ingrese en kWh la energía consumida"))

if kwh <= 150:
    precio_parcial = kwh*0.987
else: 
    precio_parcial = (150*0.987)+((kwh-150)*1.203)

subtotal = precio_parcial*1.16

Total_A_Pagar = subtotal+ImpuestoDAP

print(f"El recibo de luz total a pagar es de {Total_A_Pagar}")



