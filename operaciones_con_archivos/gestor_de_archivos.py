def crear():
    archivo = input("Nombre del archivo (sin .txt): ") + ".txt"
    with open(archivo, "w") as f:
        f.write("NOMBRE:\nMATRICULA:\nCORREO:\nTELEFONO:\n")
    print("Archivo creado correctamente.")

def guardar():
    archivo = input("Archivo donde guardar (sin .txt): ") + ".txt"
    nombre = input("Nuevo nombre: ")
    matricula = input("Nueva matrícula: ")
    correo = input("Nuevo correo: ")
    telefono = input("Nuevo teléfono: ")

    with open(archivo, "w") as f:
        f.write(f"NOMBRE: {nombre}\n")
        f.write(f"MATRICULA: {matricula}\n")
        f.write(f"CORREO: {correo}\n")
        f.write(f"TELEFONO: {telefono}\n")

    print("Datos guardados correctamente.")

def leer():
    archivo = input("Archivo a leer (sin .txt): ") + ".txt"
    try:
        print("\n" + open(archivo).read())
    except:
        print("Ese archivo no existe.")

def cambiar_nombre():
    archivo = input("Archivo donde cambiar (sin .txt): ") + ".txt"
    nombre_actual = input("Nombre que aparece dentro del archivo: ")
    nuevo_nombre = input("Nuevo nombre para reemplazarlo: ")

    try:
        contenido = open(archivo).read()
    except:
        print("Ese archivo no existe.")
        return

    if nombre_actual in contenido:
        contenido = contenido.replace(nombre_actual, nuevo_nombre)
        open(archivo, "w").write(contenido)
        print("Nombre cambiado exitosamente.")
    else:
        print("Ese nombre NO está en el archivo.")

while True:
    print("\n1. Crear archivo")
    print("2. Guardar registros")
    print("3. Leer archivo")
    print("4. Cambiar nombre dentro del archivo")
    print("5. Salir")

    op = input("Opción: ")

    if op == "1": crear()
    elif op == "2": guardar()
    elif op == "3": leer()
    elif op == "4": cambiar_nombre()
    elif op == "5":
        print("Cerrando programa...")
        break
    else:
        print("Opción inválida.")