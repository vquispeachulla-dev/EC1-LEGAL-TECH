from datetime import datetime, timedelta, date

FERIADOS_NACIONALES_2026 = {
    "01/01/2026", "02/04/2026", "03/04/2026", "01/05/2026",
    "07/06/2026", "29/06/2026", "23/07/2026", "28/07/2026",
    "29/07/2026", "06/08/2026", "30/08/2026", "08/10/2026",
    "01/11/2026", "08/12/2026", "09/12/2026", "25/12/2026"
}

print("\nCALCULADORA DE PLAZOS ADMINISTRATIVOS")

print("\nTipo de recurso:")
print("\n     1. Reconsideración")
print("     2. Apelación")

tipo_recurso = input("\nSeleccione una opción (1 o 2): ")

if tipo_recurso == "1":
    tipo_recurso = "Reconsideración"
elif tipo_recurso == "2":
    tipo_recurso = "Apelación"
else:
    print("\nOpción no válida.")
    exit()

fecha_notificacion = input("\nFecha de notificación (DD/MM/AAAA): ")
dias = 15

try:
    fecha = datetime.strptime(fecha_notificacion, "%d/%m/%Y")
except ValueError:
    print("\nFecha inválida. Ingrese una fecha válida.")
    exit()
    
print("\nTipo de cómputo:")
print("\n     1. Días hábiles")
print("     2. Días calendario")

tipo = input("\nSeleccione una opción (1 o 2): ")

if tipo == "1":
    fecha_vencimiento = fecha
    dias_contados = 0

    while dias_contados < dias:
        fecha_vencimiento += timedelta(days=1)

        fecha_texto = fecha_vencimiento.strftime("%d/%m/%Y")

        if (fecha_vencimiento.weekday() < 5 and fecha_texto not in FERIADOS_NACIONALES_2026):
            dias_contados += 1

elif tipo == "2":
    fecha_vencimiento = fecha + timedelta(days=dias)

else:
    print("\nOpción no válida.")
    exit()

hoy = date.today()
dias_restantes = (fecha_vencimiento.date() - hoy).days

print("\nRESULTADO")
print("\n     Tipo de recurso:", tipo_recurso)
print("     Fecha de notificación:", fecha.strftime("%d/%m/%Y"))
print("     Plazo:", dias, "días")

if tipo == "1":
    print("     Tipo de cómputo utilizado: Días hábiles")
else:
    print("     Tipo de cómputo utilizado: Días calendario")

print("     Fecha de vencimiento:", fecha_vencimiento.strftime("%d/%m/%Y"))

if dias_restantes < 0:
    print("\nEl plazo ya venció hace", abs(dias_restantes),"días.")
else:
    print("     Días restantes para interponer el recurso:", dias_restantes,"dias calendario.")

print("\n*Base legal: TUO de la Ley N.° 27444, artículos 133, 134, 139 y 207")
