from datetime import datetime, timedelta

fecha_inicio = input("Ingresa la fecha de inicio (DD/MM/AAAA): ")
dias = int(input("Ingresa el número de días del plazo: "))

fecha = datetime.strptime(fecha_inicio, "%d/%m/%Y")

fecha_vencimiento = fecha + timedelta(days=dias)

print("\nResultado:")
print("Fecha de inicio:", fecha.strftime("%d/%m/%Y"))
print("Días del plazo:", dias)
print("Fecha de vencimiento:", fecha_vencimiento.strftime("%d/%m/%Y"))