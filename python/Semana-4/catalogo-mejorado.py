# Programacion 1 | Parcial 2 
# Cristian Tapia - 2025

# 1: El catálogo se gestionará con una única lista de diccionarios, donde cada diccionario representa un libro:

# Claves obligatoria por libro:
    # TITULO → str (nombre del libro)
    # CANTIDAD → int (número de ejemplares disponibles, >= 0)

# TODO: Comportamiento esperado
# Si el CSV no existe, iniciar con catálogo vacío.
# ● Si el usuario ingresa un título duplicado, rechazar y volver a pedir.
# ● Tras agregar/actualizar datos, guardar automáticamente en el CSV.
# ● Las búsquedas de títulos deben ser robustas (insensibles a mayúsculas y espacios
#   extra).

# TODO VALIDACIONES: 
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
            if not (0 <= cantidad < 1000):
                print("\n ⚠️  Ingrese una cantidad valida (numero entero entre 0 y 1000).")
                continue
            break
        return cantidad
    
    def ObtenerTitulos():
        dir_archivo = DirArchivo()
        titulos = []
    # Si el archivo no existe, lo crea con encabezado vacío
        if not ExisteArchivo(dir_archivo):
            with open(dir_archivo, "w", newline="", encoding="utf-8") as archivo:
                filas = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
                filas.writeheader()
                return titulos
        
        with open(dir_archivo, "r", newline="",encoding="utf-8") as archivo:
            filas = csv.DictReader(archivo)
            for fila in filas:
                titulos.append({"Titulo": fila["Titulo"], "Cantidad": int(fila["Cantidad"])})
        return titulos
            
            
    def MostrarTitulos():
        titulos = ObtenerTitulos()
        if titulos:
            print("\n" + "=" * 18 + " Titulos disponibles " + "=" * 18)
            for titulo in titulos:
                for clave, valor in titulo.items():
                    print(f"{clave}: {valor}")
                print("=" * 54)
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.\n")
    
    def ExisteTitulo(nombre):
        # Verifica si existe un titulo con el nombre indicado en el archivo.
        titulos = ObtenerTitulos()
        for titulo in titulos:
            if titulo["Titulo"] == nombre:
                return True
        return False

    # Defino metodo para consultar por un titulo en especifico y lo muestro en pantalla
    def MostrarTituloConsulta():
        titulos = ObtenerTitulos()
        if titulos:
            nombre_titulo = PedirNombre()
            if not ExisteTitulo(nombre_titulo):
                print(f"\n ⚠️  El titulo {nombre_titulo} no se encuentra dentro del catalogo.\n")
            else:
                for titulo in titulos:
                    if titulo.get("Titulo") == nombre_titulo:
                        print("=" * 54)
                        for clave, valor in titulo.items():
                            print(f"{clave}: {valor}")
                        print("=" * 54)
                        break
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.\n")
    # Defino metodo para agregar titulos al csv sin sobreescribir
    def AgregarNuevoTitulo():
        nombre_titulo = PedirNombre()
        dir_archivo = DirArchivo()
        if not ExisteTitulo(nombre_titulo):
            cantidad = PedirCantidad()
            with open(dir_archivo, "a", newline="", encoding="utf-8") as archivo:
                filas = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
                filas.writerow({"Titulo": nombre_titulo, "Cantidad": cantidad})
            print(f"\n ✅ Titulo {nombre_titulo} agregado correctamente.")
        else:
            print("\n ⚠️  El titulo ya se encuentra dentro del catalogo.\n")
            
    def GuardarProductos(filas_titulos):
        dir_archivo = DirArchivo()
        with open(dir_archivo, "w", newline="", encoding="utf-8") as archivo:
            filas = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
            filas.writeheader()
            filas.writerows(filas_titulos)
    
    def IngresarEjemplares():
        titulos = ObtenerTitulos()
        if titulos:
            print("\nA que titulo desea agregarle ejemplares?")
            nombre = PedirNombre()
            if ExisteTitulo(nombre):
                for titulo in titulos:
                    if titulo["Titulo"] == nombre:
                        print(f"Cuantos ejemplares desea agregarle al titulo '{nombre}' ?")
                        cant_ejemplares = PedirCantidad()
                        titulo["Cantidad"] =+ cant_ejemplares
                        print(f"\n ✅ Se agregaron con exito {cant_ejemplares} al titulo {nombre} | Cantidad actual: {titulo["Cantidad"]}.")
                        GuardarProductos(titulos)
                        break
            else:
                print("\n ⚠️  El titulo ingresado no se encuentra dentro del catalogo.\n")
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.\n")
            
    def MostrarAgotados():
        titulos = ObtenerTitulos()
        agotados = False
        if titulos:
            print("\n" + "=" * 18 + " Titulos agotados " + "=" * 18)
            for titulo in titulos:
                if titulo["Cantidad"] == 0:
                    print(f"{titulo["Titulo"]} | Agotado")
                    agotados = True
                if not agotados:
                    print("\n ✅  No hay titulos agotados dentro del catalogo.\n")
        else:
            print("\n ⚠️  No hay titulos disponibles dentro del catalogo.\n")


    
    
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
                print("\nCuantos titulos desea ingresar?")
                cant_titulos_agregar = PedirCantidad()
                for i in range(cant_titulos_agregar):
                    print(f"\nTitulo numero {i+1}")
                    nombre_titulo = PedirNombre()
                    AgregarNuevoTitulo(nombre_titulo)
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
                            pass
                        case "2":
                            pass
                        case "3":
                            MostrarTitulos()
                        case "4":
                            print("Volviendo al menu principal...!\n")
                            break
                        case _:
                            print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 4.\n")
                            continue   
            case "8":
                print("Saliendo del programa... ¡Hasta luego!\n")
                break
            # Opcion inválida
            case _:
                print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 6.\n")
                continue            
    
#=========================================================================================#
#                              Ejecuto el programa principal                              #
#=========================================================================================#
programa_principal()
#=========================================================================================#