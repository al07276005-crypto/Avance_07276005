
print("\n*** Dulce Alejandra Gomez Guevara    07244343 ***")
print("*** Fátima Isabella Pagno Castillo    07276005 ***\n")

print("*** Ejercicio 3 WI-FI DEL CAFÉ ***\n")

contrasena_cafe = "Latte2026"

nombre = input("¿Cómo te llamas? ")
contrasena = input("Escribe la contraseña: ")
gasto = float(input("¿Cuánto gastaste? "))

if contrasena == contrasena_cafe:
    print("Conectado al Wi-Fi, bienvenida", nombre)
else:
    print("Contraseña incorrecta")
    
if gasto >= 100:
    print("Tienes 1 hora de Wi/Fi\n")
else:
    print("Tienes 30 minutos de Wi/Fi\n")