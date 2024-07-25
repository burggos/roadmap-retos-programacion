# Operadores Aritméticos
a = 10
b = 3

print("Suma:", a + b)        
print("Resta:", a - b)       
print("Multiplicación:", a * b)
print("División:", a / b) 
print("División entera:", a // b)  
print("Módulo:", a % b)   
print("Potencia:", a ** b)

# Operadores de Comparación
x = 5
y = 8

print("Igual a:", x == y)      
print("Distinto de:", x != y)
print("Mayor que:", x > y)  
print("Menor que:", x < y)     
print("Mayor o igual que:", x >= y)
print("Menor o igual que:", x <= y)

# Operadores Lógicos
p = True
q = False

print("Y lógico:", p and q)
print("O lógico:", p or q)
print("Negación lógica:", not p)

# Operadores de Asignación
z = 10
z += 5
print("Asignación de suma:", z)

z -= 3
print("Asignación de resta:", z)

z *= 2
print("Asignación de multiplicación:", z)



z /= 4
print("Asignación de división:", z) 

z //= 2
print("Asignación de división entera:", z) 

z %= 2
print("Asignación de módulo:", z)

z **= 3
print("Asignación de potencia:", z)  

# Operadores de Identidad
a = [1, 2, 3]
b = [1, 2, 3]

print("Es:", a is b)
print("No es:", a is not b)

# Operadores de Pertenencia
x = 5
lista = [1, 2, 3, 4, 5]

print("Está en:", x in lista)       
print("No está en:", x not in lista)  

# Operadores Bit a Bit(No se si valla alguna ves en mi vida a usar esto)
a = 5 
b = 3  

print("Y bit a bit:", a & b)  
print("O bit a bit:", a | b)  
print("XOR bit a bit:", a ^ b)  
print("Negación bit a bit:", ~a)  
print("Desplazamiento a la izquierda:", a << 1)  
print("Desplazamiento a la derecha:", a >> 1) 

""""Estructuras de control"""

# Condicionales
x = 10

if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

# Bucle for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Bucle con break
for i in range(10):
    if i == 5:
        break
    print(i)

# Bucle con continue
for i in range(10):
    if i == 5:
        continue
    print(i)

# Definición de funciones
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Gabriel")

# Funciones con valores de retorno
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado)


""""Bueno despues de escribir todo eso no me queda ganas de nada 
pero lo que toca toca"""

print("Dificultad extra")

for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 !=0:
        print(i)