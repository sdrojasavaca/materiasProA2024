listNumbers = []
listNumbersPair = []
for i in range(10):
    listNumbers.append(int(input(f"Ingrese un numero: ")))
for i in listNumbers:
    if i == 0:
        print(f"El numero ingresado: 0, es cero")
        listNumbersPair.append(i)
    elif i % 2 == 0:
        print (f"El numero que ingreso: {i}, es par")
    elif not(i %2== 0):
        print (f"El numero que ingreso: {i}, es impar")
    else:
        print("Error, no ingreso un numero valido")
print(f"Los numeros pares que ingreso fueron {listNumbersPair}") 
