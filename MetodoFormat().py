#Concatenacion: union de dos o mas cadenas de caracrteres(strings)
#Metodo fortmat()

#Ejemplo 1
nombre = 'Romina'
edad = 31

print('Hola {} tienes {} años'.format(nombre, edad))

#Ejemplo 2
print('Hola {nombre} tienes {edad} años'.format(nombre = 'Romina', edad = 31))

#Ejemplo 3
nombre = 'Romina'
edad = 31

print('Hola {0} tienes {1} años'.format(nombre, edad))
print('Hola {1} tienes {0} años'.format(edad, nombre))