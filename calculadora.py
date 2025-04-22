print("Mi Calculadora en Python")
#Ingresar los numeros en las variables num1 y num2
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el Segundo Numero: "))
#Mostrar menu de operaciones
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Divisón")

operacion =input("Elija una operación")
#Logica con: If / ELif /Else
if operacion == "1":
    resultado = num1+num2
    print("Resultado de la Suma es: ",resultado)
elif operacion == "2":
    resultado = num1-num2
    print("Resultado de la Resta es: ",resultado)
elif operacion == "3":
    resultado= num1*num2
    print("Resultado de la Multiplicación es: ", resultado)
elif operacion =="4":
    resultado = num1/num2
    print("El Resultado de la División es: ", resultado)
else:
    print("Opcion NO valida")

print("¿Desea seguir en la Caculadora?")
print("1. Si")
print("2. No")

continuar = input("Ingresa la opcion")
if continuar == "1":
    print("Se va volver a ejecutar la calculadora")
else:
    print("Gracias por Utilizar mi calculadora")