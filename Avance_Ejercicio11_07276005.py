print("\n''' Dulce Alejandra Gomez Guevara    07244343 '''")
print("''' Fátima Isabella Pagno Castillo    07276005 '''\n")

print("''' Ejercicio 11 ¿Qué me pongo hoy? '''")

#int() convierte el texto a número para poder comparar
temperatura = int(input("\n¿Cuántos grados hacen hoy? "))
#Si el usuario escribe 15, ahora temperatura vale 15

print("\n==== OUTFIT DEL DÍA ====")

#PREGUNTA 1: ¿15 es menor que 10? Respuesta: False, pasa a la siguiente
if temperatura < 10:
    print("Hace mucho frío: chamarra, bufanday botas")
    
#PREGUNTA 2: ya sabemos que hace 10 o más
#¿15 es menor que 20? Respuesta: True, muestra el mensaje y TERMINA
elif temperatura < 20:
    print("Está fresco: sudadera y jeans")
    
#PREGUNTA 3: ya sabemos que hace 20 o más
elif temperatura < 30:
    print("Está agradable: playera y tenis")
    
#else: hace 30 o más
else:
    print("Hace mucho calor: short, gorra y mucha agua")