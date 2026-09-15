from datetime import datetime, timedelta
FERIADOS_NACIONALES_2026 = {
    "01/01/2026",
    "02/04/2026",
    "03/04/2026",
    "01/05/2026",
    "07/06/2026",
    "29/06/2026",
    "23/07/2026",
    "28/07/2026",
    "29/07/2026",
    "06/08/2026",
    "30/08/2026",
    "08/10/2026",
    "01/11/2026",
    "08/12/2026",
    "09/12/2026",
    "25/12/2026"
}

fecha_inicio = input("Ingrese la fecha de notificación (DD/MM/AAAA): ")
dias = int(input("Ingrese el número de días del plazo: "))

print("\nMencione el tipo de cómputo que desea aplicar:")
print(" 1. Días hábiles")
print(" 2. Días calendario")

tipo = input("Seleccione una opción (1 o 2): ")

try:
    fecha = datetime.strptime(fecha_inicio, "%d/%m/%Y")
except ValueError:
    print("Fecha inválida. Ingrese una fecha válida.")
    exit()

if tipo == "1":
    fecha_vencimiento = fecha
    dias_contados = 0

    while dias_contados < dias:
        fecha_vencimiento += timedelta(days=1)

        fecha_texto = fecha_vencimiento.strftime("%d/%m/%Y")

        if fecha_vencimiento.weekday() < 5 and fecha_texto not in FERIADOS_NACIONALES_2026:
            dias_contados += 1

elif tipo == "2":
    fecha_vencimiento = fecha + timedelta(days=dias)

else:
    print("Opción no válida.")
    exit()

print("\nResultado:")
print("\n Fecha de inicio:", fecha.strftime("%d/%m/%Y"))
print(" Días del plazo:", dias)

if tipo == "1":
    print(" Tipo de cómputo: Días hábiles")
else:
    print(" Tipo de cómputo: Días calendario")

print(" Fecha de vencimiento:", fecha_vencimiento.strftime("%d/%m/%Y"))
print("\nBase legal: TUO de la Ley N.° 27444, artículos 133 y 134.")
