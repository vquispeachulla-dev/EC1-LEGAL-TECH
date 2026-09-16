from datetime import datetime, timedelta
FERIADOS_NACIONALES_2026 = {
    "01/01/2026", "02/04/2026", "03/04/2026", "01/05/2026", "07/06/2026", "29/06/2026", "23/07/2026", "28/07/2026", 
    "29/07/2026", "06/08/2026", "30/08/2026", "08/10/2026", "01/11/2026", "08/12/2026", "09/12/2026", "25/12/2026"
}

print("\nCALCULADORA DE PLAZOS ADMINISTRATIVOS: RECURSOS ADMINISTRATIVOS")
tipo_recurso = input("\nEscoga entre: Apelación - Reconsideración: ")
fecha_inicio = input("\nIngrese la fecha de notificación (DD/MM/AAAA): ")

dias = 15 #plazo que da la ley para interponer los recursos

print("\nMencione el tipo de cómputo que desea aplicar:")
print("      1. Días hábiles     2. Días calendario")

tipo = input("\nSeleccione una opción (1 o 2): ")

try:
    fecha = datetime.strptime(fecha_inicio, "%d/%m/%Y")
except ValueError:
    print(" Fecha inválida. Ingrese una fecha válida.")
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
    print(" Opción no válida.")
    exit()

print("\nResultado:")
print("\n     Fecha de notificación:", fecha.strftime("%d/%m/%Y"))
print("     Días del plazo:", dias)

if tipo == "1":
    print("     Tipo de cómputo: Días hábiles")
else:
    print("     Tipo de cómputo: Días calendario")

print("     Fecha de vencimiento:", fecha_vencimiento.strftime("%d/%m/%Y"))

from datetime import date

hoy = date.today()
dias_restantes = (fecha_vencimiento.date() - hoy).days

if dias_restantes < 0 :
   print("\nTu plazo ya venció hace", abs(dias_restantes), "dias calendario.")
else :
   print("\nTe quedan", dias_restantes, "días calendario.")

print("\n*Base legal: TUO de la Ley N.° 27444, artículos 133, 134 y 139.2.")
