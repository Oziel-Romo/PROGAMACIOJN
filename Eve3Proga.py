#Lectura y escritura de archivos

#Esto sería un ejercicio sin incluir saltos de línea.

# Abro el archivo en modo Write Extended.
# Si el archivo no existe, lo genera. Si existe, lo remplaza.
# Los contenidos van en secuencia.
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 contenidos en secuencia.
f.write("Blanco")
f.write("Negro")
f.write("Naranja")
# Cierro el archivo.
f.close()

#------------------------------------------------
#Esto sería un ejemplo incluyendo saltos de página

# Para saltos de línea, se utiliza \n
# Abro el archivo en modo Write Extended
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 líneas adicionales.
f.write("Rojo\n")
f.write("Amarillo\n")
f.write("Verde\n")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()

#------------------------------------------------
#otra forma de escribir líneas es utilizando el método writelines() , que toma un iterable, donde cada elemento representa una línea del archivo.

archivo="colores.txt"
f = open(archivo,"a+")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()

#------------------------------------------------

#Lectura de archivo
#Se puede leer el contenido de un archivo utilizando la función read() . Si se aplica de esta manera, la totalidad del archivo se recupera.

# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo el contenido y se lo asigno a la variable
# contenido.
contenido=f.read()
# Muestro el contenido. Debe ser todo el archivo.
print(contenido)
# Cierro el archivo.
f.close()

#------------------------------------------------
#Si se especifica un número como parámetro del método read() , quiere decir el número de caracteres que se quiere recuperar

# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente los primeros 5 caracteres del archivo.
contenido=f.read(5)
# Muestro el contenido
print(contenido)
# Leo otros 5 caracteres del archivo.
contenido=f.read(5)
# Muestro el contenido
print(contenido)
# Cierro el archivo.
f.close()

#------------------------------------------------

#Se puede leer el archivo línea por línea, si se utiliza el método readline() .

# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente la primer línea del archivo.
contenido=f.readline()
# Muestro el contenido
print(contenido)
# Leo siguiente línea
contenido=f.readline()
# Muestro el contenido
print(contenido)
# Cierro el archivo.
f.close()