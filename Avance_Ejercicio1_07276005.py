print("\n*** Dulce Alejandra Gomez Guevara    07244343 ***")
print("*** Fátima Isabella Pagno Castillo    07276005 ***\n")

print("*** Ejercicio 1: Estado de mi celular ***\n")

bateria = int(input("¿Cuánta batería tienes? "))
espacio = int(input("¿Cuántos GB libres tienes? "))
notificaciones = int(input("¿Cuántas notificaciones sin leer tienes? "))

if bateria <= 20:
    print("Batería baja, conecta tu cargador")
    
if espacio < 5:
    print("Poco espacio, borra fotos o apps que no uses")
    
if notificaciones > 0:
    print("Tienes", notificaciones, "notificaciones sin leer\n")
else:
    print("Estás al día, no tienes notificaciones\n")