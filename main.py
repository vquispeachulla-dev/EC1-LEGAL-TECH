from datetime import datetime

fecha_inicio = input("Ingresa la fecha de inicio (DD/MM/AAAA): ")
dias = int(input("Ingresa el número de días del plazo: "))

fecha = datetime.strptime(fecha_inicio, "%d/%m/%Y")

print("\nDatos ingresados:")
print("Fecha de inicio:", fecha.strftime("%d/%m/%Y"))
print("Días del plazo:", dias)