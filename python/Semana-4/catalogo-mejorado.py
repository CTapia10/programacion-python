# Programacion 1 | Parcial 2 
# Cristian Tapia - 2025

# 1: El catálogo se gestionará con una única lista de diccionarios, donde cada diccionario representa un libro:

# Claves obligatoria por libro:
    # TITULO → str (nombre del libro)
    # CANTIDAD → int (número de ejemplares disponibles, >= 0)

# Comportamiento esperado
# Si el CSV no existe, iniciar con catálogo vacío.
# ● Si el usuario ingresa un título duplicado, rechazar y volver a pedir.
# ● Tras agregar/actualizar datos, guardar automáticamente en el CSV.
# ● Las búsquedas de títulos deben ser robustas (insensibles a mayúsculas y espacios
#   extra).

# VALIDACIONES: 
# Unicidad: no pueden existir dos libros con el mismo TITULO (comparación insensible a mayúsculas/minúsculas y espacios redundantes).
# Títulos: no se aceptan vacíos; comparar sin sensibilidad a mayúsculas y normalizando espacios.
# Cantidades: deben ser enteros >= 0 al cargar/editar
# Préstamos: no permitir valores negativos (si está en 0, informar al usuario)
# Mensajes claros: informar siempre si una operación fue exitosa o rechazada y el motivo.

# PERSISTENCIA:
# El programa carga el catálogo desde un archivo CSV al iniciar (si existe) y guarda los cambios cada vez que se modifica el inventario.

# FORMATO sugerido del CSV (con encabezado):
# Columnas: TITULO,CANTIDAD 

#=============================================================================#
#======================== Defino el programa principal =======================#
#=============================================================================#
def programa_principal():
    import csv
    import os
    def TituloArchivo():
        # Guardo el nombre del archivo en variable para reutilizarlo o cambiarlo en todas las coincidencias
        NOMBRE_ARCHIVO = "titulos.csv"
        return NOMBRE_ARCHIVO

    def DirArchivo():
        # Ruta absoluta del archivo titulos.csv en la misma carpeta que este script
        base = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(base, TituloArchivo())
        return archivo

    # Defino metodo para verificar si existe el archivo
    def ExisteArchivo(archivo):
        return os.path.isfile(archivo)

    # Defino metodo para pedir el nombre del titulo al usuario
    def PedirNombre():
        while True:
            nombre = input("\nIngrese el nombre del titulo: ").strip().capitalize()
            if len(nombre) < 2:
                print(f"\n⚠️  El nombre es demasiado corto.")
                continue
            if len(nombre) > 40:
                print(f"\n⚠️  El nombre es demasiado largo.")
                continue
            return nombre

    # Defino metodo para pedir la cantidad y devolverla sin errores de entrada
    def PedirCantidad():
        while True:
            cantidad = input("\nIngrese la cantidad deseada: ").strip()
            if not cantidad.isdigit():
                print("\n ⚠️  Ingrese una cantidad valida (numero entero entre 0 y 1000).")
                continue
            # Despues de verificar que no hayan signos especiales transformo a entero
            cantidad = int(cantidad)
            if not (0 <= cantidad <= 1000):
                print("\n ⚠️  Ingrese una cantidad valida (numero entero entre 0 y 1000).")
                continue
            break
        return cantidad
    
    # Defino metodo para obtener titulos, en caso que no existan crea un nuevo archivo vacio
    def ObtenerTitulos():
        dir_archivo = DirArchivo()
        titulos = []
    # Si el archivo no existe, lo crea con encabezado vacío
        if not ExisteArchivo(dir_archivo):
            with open(dir_archivo, "w", newline="", encoding="utf-8") as archivo:
                filas = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
                filas.writeheader()
                return titulos
        
        with open(dir_archivo, "r", newline="",encoding="utf-8") as archivo:
            filas = csv.DictReader(archivo)
            for fila in filas:
                titulos.append({"TITULO": fila["TITULO"], "CANTIDAD": int(fila["CANTIDAD"])})
        return titulos
            
    # Defino metodo para mostrar todos los titulos disponibles
    def MostrarTitulos():
        titulos = ObtenerTitulos()
        if titulos:
            print("\n" + "=" * 16 + " Titulos disponibles " + "=" * 17)
            for titulo in titulos:
                print(f"Titulo: {titulo["TITULO"]} \nCantidad: {titulo["CANTIDAD"]}")
                print("=" * 54)
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.\n")
    
    # Defino metodo para verificar si un titulo existe
    def ExisteTitulo(nombre):
        # Verifica si existe un titulo con el nombre indicado en el archivo.
        titulos = ObtenerTitulos()
        for titulo in titulos:
            if titulo["TITULO"] == nombre:
                return True
        return False

    # Defino metodo para consultar por un titulo en especifico y lo muestro en pantalla
    def MostrarTituloConsulta():
        titulos = ObtenerTitulos()
        if titulos:
            nombre_titulo = PedirNombre()
            if not ExisteTitulo(nombre_titulo):
                print(f"\n ⚠️  El titulo {nombre_titulo} no se encuentra dentro del catalogo.")
            else:
                for titulo in titulos:
                    if titulo["TITULO"] == nombre_titulo:
                        print(f"\n ✅ El titulo {nombre_titulo} esta disponible.")
                        print("=" * 54)
                        print(f"Titulo: {titulo["TITULO"]} \nCantidad: {titulo["CANTIDAD"]}")
                        print("=" * 54)
                        break
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.\n")
            
    # Defino metodo para agregar titulos al csv sin sobreescribir
    def AgregarNuevoTitulo():
        dir_archivo = DirArchivo()
        while True:
            nombre_titulo = PedirNombre()
            if not ExisteTitulo(nombre_titulo):
                cantidad = PedirCantidad()
                with open(dir_archivo, "a", newline="", encoding="utf-8") as archivo:
                    filas = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
                    filas.writerow({"TITULO": nombre_titulo, "CANTIDAD": cantidad})
                print(f"\n ✅ Titulo {nombre_titulo} agregado correctamente.")
                break
            else:
                print(f"\n ⚠️  El titulo {nombre_titulo} ya se encuentra dentro del catalogo.")
                continue
    # Defino metodo para persistir los cambios en el archivo csv
    def GuardarProductos(filas_titulos):
        dir_archivo = DirArchivo()
        with open(dir_archivo, "w", newline="", encoding="utf-8") as archivo:
            filas = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
            filas.writeheader()
            filas.writerows(filas_titulos)
    
    # Defino metodo para ingresar ejemplares de un titulo indicado
    def IngresarEjemplares():
        titulos = ObtenerTitulos()
        if titulos:
            print("\nA que titulo desea agregarle ejemplares?")
            nombre = PedirNombre()
            if ExisteTitulo(nombre):
                for titulo in titulos:
                    if titulo["TITULO"] == nombre:
                        print(f"\nCuantos ejemplares desea agregarle al titulo '{nombre}' ?")
                        cant_ejemplares = PedirCantidad()
                        if not cant_ejemplares == 0:
                            titulo["CANTIDAD"] += cant_ejemplares
                            print(f"\n ✅ Se agregaron con exito {cant_ejemplares} al titulo '{nombre}' | Cantidad actual: {titulo["CANTIDAD"]}.")
                            GuardarProductos(titulos)
                            break
                        else:
                            print("\n ✅ No se agrego ningun ejemplar.")
                            break
            else:
                print(f"\n ⚠️  El titulo '{nombre}' no se encuentra dentro del catalogo.")
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.")
            
    # Defino metodo para mostrar en pantalla los titulos sin ejemplares disponibles
    def MostrarAgotados():
        titulos = ObtenerTitulos()
        agotados = False
        if titulos:
            print("\n" + "=" * 18 + " Titulos agotados " + "=" * 18)
            for titulo in titulos:
                if titulo["CANTIDAD"] == 0:
                    print(f"{titulo["TITULO"]} | Agotado ⚠️")
                    agotados = True
            if not agotados:
                print("\n ✅  No hay titulos agotados dentro del catalogo.")
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.")

    # Defino metodo para pedir prestado un ejemplar
    def PedirEjemplar():
        titulos = ObtenerTitulos()
        if titulos:
            print("\nQue titulo desea pedir prestado?")
            nombre = PedirNombre()
            if ExisteTitulo(nombre):
                for titulo in titulos:
                    if titulo["TITULO"] == nombre:
                        if (titulo["CANTIDAD"] > 0):
                            titulo["CANTIDAD"] -= 1
                            print(f"\n ✅ Se tomo prestado con exito el titulo '{nombre}' | Cantidad actual: {titulo["CANTIDAD"]}.")
                            GuardarProductos(titulos)
                            break
                        else:
                            print(f"\n⚠️  No hay copias del titulo '{nombre}' disponibles para préstamo en este momento.")
                        
            else:
                print(f"\n ⚠️  El titulo '{nombre}' no se encuentra dentro del catalogo.")
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.")
    
    # Defino metodo para devolver un ejemplar
    def DevolverEjemplar():
        titulos = ObtenerTitulos()
        if titulos:
            print("\nQue titulo desea devolver?")
            nombre = PedirNombre()
            if ExisteTitulo(nombre):
                for titulo in titulos:
                    if titulo["TITULO"] == nombre:
                        titulo["CANTIDAD"] += 1
                        print(f"\n ✅ Devolución con exito del titulo '{nombre}' | Cantidad actual: {titulo["CANTIDAD"]}.")
                        GuardarProductos(titulos)
                        break
            else:
                print(f"\n ⚠️  El titulo '{nombre}' no se encuentra dentro del catalogo.")
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.")

    # Defino metodo que contiene el menu secundario para actualizar los ejemplares
    def ActualizarEjemplares():
        menu_secundario = ["1. Pedir prestado un titulo",
                "2. Devolver un titulo",
                "3. Mostrar catálogo",
                "4. Volver al menu principal"]
        while True:
            # Mostramos las opciones del menu al usuario
            print("\n"+"="*54)
            print("Elija una opción")
            print("="*54)
            for opcion in menu_secundario:
                print(opcion)
            print("="*54)
            seleccion = input("Opción seleccionada: ").strip()
            print("="*54)
            match seleccion:
                case "1":
                    PedirEjemplar()
                case "2":
                    DevolverEjemplar()
                case "3":
                    MostrarTitulos()
                case "4":
                    print("✅ Volviendo al menu principal...\n")
                    break
                case _:
                    print("\n⚠️  Opción inválida. Por favor, elija una opción del 1 al 4.\n")
                    continue   
                
    # Defino metodo para ingresar varios titulos a la vez, maximo 10 para evitar estar en un loop por ejemplo de ingresar 1000 titulos
    def AgregarTitulos():
        while True:
            print("\nCuantos titulos desea ingresar?")
            cant_titulos_agregar = PedirCantidad()
            if cant_titulos_agregar > 10:
                print("\n ⚠️  Advertencia, el numero ingresado es muy alto, el maximo de titulos permitidos a agregar son 10.")
                continue
            else:
                for i in range(cant_titulos_agregar):
                    print(f"\nTitulo numero {i+1}")
                    AgregarNuevoTitulo()
            break
            
    # Lista que contiene las opciones del menu principal
    menu_principal = ["1. Ingresar títulos",
                    "2. Ingresar ejemplares",
                    "3. Mostrar catálogo",
                    "4. Consultar disponibilidad",
                    "5. Listar agotados",
                    "6. Agregar título",
                    "7. Actualizar ejemplares (préstamo/devolución)",
                    "8. Salir"]
    while True:
        # Mostramos las opciones del menu al usuario
        print("\n"+"="*54)
        print("Bienvenido al catálogo de titulos, elija una opción") 
        print("="*54)
        for opcion in menu_principal:
            print(opcion)
        print("="*54)
        # Pedimos al usuario que seleccione una de las opciones
        seleccion = input("Opción seleccionada: ").strip()
        print("="*54)
        match seleccion:
            case "1":
                AgregarTitulos()
            case "2":
                IngresarEjemplares()
            case "3":
                MostrarTitulos()
            case "4":
                MostrarTituloConsulta()
            case "5":
                MostrarAgotados()
            case "6":
                AgregarNuevoTitulo()
            case "7":
                ActualizarEjemplares()
            case "8":
                print("✅ Saliendo del programa... ¡Hasta luego!\n")
                break
            # Opcion inválida
            case _:
                print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 8.\n")
                continue            
    
#=========================================================================================#
#                              Ejecuto el programa principal                              #
#=========================================================================================#
programa_principal()
#=========================================================================================#