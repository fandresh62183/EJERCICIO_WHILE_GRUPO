import math

# calcular el valor de un número
def valor(n):
    if n == 0:
        return 1
    else:
        return n * valor(n-1)

# Inicializamos las variables
num1 = int(input("Escriba el primer número: "))
num2 = int(input("Escriba el segundo número: "))
opcion = ""

# Ciclo while para mostrar las opciones de la calculadora
while opcion != "9":
    print(" ")
    print("-------- CALCULADORA --------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Factorial")
    print("7. Raíz cuadrada")
    print("8. Cambiar números")
    print("9. Salir")
    opcion = input("Seleccione una opción: ")
    
    # Suma
    if opcion == "1":
        resultado = num1 + num2
        print("El resultado de la suma es: ", resultado)
    
    # Resta
    elif opcion == "2":
        resultado = num1 - num2
        print("El resultado de la resta es: ", resultado)
    
    # Multiplicación
    elif opcion == "3":
        resultado = num1 * num2
        print("El resultado de la multiplicación es: ", resultado)
    
    # División
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir entre 0")
        else:
            resultado = num1 / num2
            print("El resultado de la división es: ", resultado)
    
    # Potenciación
    elif opcion == "5":
        resultado = num1 ** num2
        print("El resultado de la potenciación es: ", resultado)
    
    # Factorial
    elif opcion == "6":
        if num1 < 0:
            print("Error: El número debe ser positivo")
        else:
            resultado = factorial(num1)
            print("El factorial de ", num1, " es: ", resultado)
    
    # Raíz cuadrada
    elif opcion == "7":
        if num1 < 0:
            print("Error: El número debe ser positivo")
        else:
            resultado = math.sqrt(num1)
            print("La raíz cuadrada de ", num1, " es: ", resultado)
    
    # Cambiar números
    elif opcion == "8":
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
    
    # Salir
    elif opcion == "9":
        print("Hasta la próxima!")
    
    # Opción inválida
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")
