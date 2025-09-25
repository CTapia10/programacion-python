# Catálogo de libros – Programación 1 - UTN TUPAD
# Cristian Tapia

# La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
# copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
# utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
# vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
# Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
# elija salir.

# Debes usar un bucle while para navegar por las opciones del
# menú hasta que el usuario elija salir

# Inicializo listas a utilizar
titulos = []
ejemplares = []

# Inicializo opciones_menu con los requerimientos del menu:
opciones_menu_principal = ["1. Ingresar títulos",
                "2. Ingresar ejemplares",
                "3. Mostrar catálogo",
                "4. Consultar disponibilidad",
                "5. Listar agotados",
                "6. Agregar título",
                "7. Actualizar ejemplares (préstamo/devolución)",
                "8. Salir",]

opciones_menu_actualizacion= ["1. Pedir prestado un ejemplar",
                            "2. Devolver un ejemplar",
                            "3. Volver al menú principal",]
# Inicializo variable selección que va a tener la elección del item del menu
seleccion = 0

while True:
    # Mostramos las opciones del menu al usuario
    print("="*50)
    print("Bienvenido al catálogo de libros, elija una opción")
    print("="*50)
    for opcion in opciones_menu_principal:
        print(opcion)
    print("="*50)
    # Pedimos al usuario que seleccione una de las opciones
    seleccion = int(input("Opción seleccionada: "))
    print("="*50+"\n")
    
    # Procesamos la posición con match/case
    match seleccion:
        # 1. Ingresar títulos
        case 1:
            nuevoTitulo = input("Ingrese el título que desea agregar a la lista: ").strip()
            # Valido si el nuevo título existe en la lista o esta vacio, considerando tambien el caso por si es mayusculas o minusculas
            while ((nuevoTitulo.lower() in [titulo.lower() for titulo in titulos]) or nuevoTitulo == ""):
                print("\n ⚠️  Ingreso un título vacío o esta repetido en la lista. Intente nuevamente.\n")
                nuevoTitulo = input("Ingrese el título nuevamente: ").strip()
            print(f"\n✅ Se ingreso con éxito el título: {nuevoTitulo}. \n")
            # Agrego el nuevo título a la lista
            titulos.append(nuevoTitulo)
            # Al agregar el título tambien preparo el espacio en la lista ejemplares con el mismo índice para evitar desincronizacion
            posicion = titulos.index(nuevoTitulo)
            ejemplares.insert(posicion, 0)
        # 2. Ingresar ejemplares
        case 2:
            # Si no hay títulos cargados no debe permitir agregar ejemplares
            if not titulos:
                print("⚠️  No existen títulos en la lista. Para ingresar la cantidad de ejemplares primero debe ingresar títulos.\n")
                continue
            # En caso que existan muestro los títulos actuales para que el usuario seleccione al cual desea agregar ejemplares
            print("="*16+"Catálogo de libros"+"="*16)
            for i, titulo in enumerate(titulos):
                print(f"{i+1}. {titulo} ({ejemplares[i]})")
            print("="*50+"\n")
            # Verifico que la posición indicada exista dentro de la lista de títulos
            while True:
                posicion = input("\nSeleccione el índice del título que desea ingresar ejemplares: ")
                if not posicion.isdigit():
                    print("\n ⚠️  Ingrese una posición valida.")
                    continue
                # Despues de verificar que no hayan signos especiales transformo a entero y resto 1 para que coincida con el índice
                posicion = int(posicion)-1
                if posicion < 0 or posicion >= len(titulos):
                    print("\n ⚠️  Ingrese una posición valida.")
                    continue
                break
            # Verifico que la cantidad de ejemplares a ingresar sea valida
            while True:
                cantidad = input("\nIngrese la cantidad de ejemplares que desea agregar: ")
                if not cantidad.isdigit():
                    print("\n⚠️  Ingrese una cantidad valida (numero entero mayor a 0).")
                    continue
                # Despues de verificar que no hayan signos especiales transformo a entero
                cantidad = int(cantidad)
                if cantidad <= 0:
                    print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).\n")
                    continue
                break
            # Sumo al total la cantidad de ejemplares ingresados y lo muestro en pantalla
            ejemplares[posicion] += cantidad
            print(f"\n✅ Se agregaron un total de {ejemplares[posicion]} ejemplares al título {titulos[posicion]}. \n")
            
        # 3. Mostrar catálogo
        case 3:
            # Si no hay títulos cargados no hay nada que mostrar
            if not titulos:
                print("⚠️  Todavía no existen títulos en la lista.\n")
                continue
            print("="*16+"Catálogo de libros"+"="*16)
            for i, titulo in enumerate(titulos):
                print(f"{i+1}. {titulo} ({ejemplares[i]})")
            print("="*50+"\n")
        # 4. Consultar disponibilidad
        case 4:
            # Si no hay títulos cargados no debe permitir consultar disponibilidad
            if not titulos:
                print("⚠️  Para poder consultar la disponibilidad de un libro deben existir títulos en la lista.\n")
                continue
            titulo_consulta = input("Ingrese el nombre del título que desea consultar: ").strip()
            # Verifico que el título que se intenta consultar exista, si es asi muestro la cantidad de ejemplares que tiene
            while True:
                if (titulo_consulta.lower() in [titulo.lower() for titulo in titulos]):
                    posicion = titulos.index(titulo_consulta)
                    print(f"\n✅ Existen {ejemplares[posicion]} ejemplares del título {titulo_consulta}.\n")
                    break
                else:
                    # Si no existe el título se puede decidir volver a consultar o volver al menu
                    print(f"⚠️  El título ingresado: {titulo_consulta} no existe en el catálogo de libros.\n")
                    print(f"Si desea consultar por otro título ingrese 'S', si desea volver al menu principal 'N'.")
                    if input().lower() == "s":
                        titulo_consulta = input("Ingrese el nombre del título que desea consultar: ").strip()
                    else:
                        break
        # 5. Listar agotados
        case 5:
            # Si no hay títulos cargados no hay nada que mostrar
            if not titulos:
                print("⚠️  Todavía no existen títulos en la lista.\n")
                continue
            
            # Inicializo variable agotados
            agotados = False
            # Verifico que hayan títulos sin ejemplares y cambio variable agotados a True en caso que exista por lo menos 1 título agotado
            if not titulos:
                print("⚠️  Todavía no existen títulos en la lista.\n")
                continue
            hay_agotados = False
            print("\n" + "="*11 + " Catálogo de títulos agotados " + "="*11)
            for i, titulo in enumerate(titulos):
                if ejemplares[i] == 0:
                    print(f"{i+1}. {titulo} = ⚠️  Agotado")
                    hay_agotados = True
            print("="*50 + "\n")

            if not hay_agotados:
                print("⚠️  No existen títulos agotados en el catálogo.\n")
            
        # 6. Agregar título
        case 6:
            nuevoTitulo = input("Ingrese el título que desea agregar a la lista: ").strip()
            # Valido si el nuevo título existe en la lista o esta vacio, considerando tambien el caso por si es mayusculas o minusculas
            while ((nuevoTitulo.lower() in [titulo.lower() for titulo in titulos]) or nuevoTitulo == ""):
                print("\n ⚠️  Ingreso un título vacío o esta repetido en la lista. Intente nuevamente.\n")
                nuevoTitulo = input("Ingrese el título nuevamente: ").strip()
            # Agrego el nuevo título a la lista
            titulos.append(nuevoTitulo)
            # Verifico que la cantidad de ejemplares a ingresar sea valida
            while True:
                cantidad = input(f"\nIngrese la cantidad de ejemplares para el título {nuevoTitulo}: ")
                if not cantidad.isdigit():
                    print("\n⚠️  Ingrese una cantidad valida (numero entero mayor a 0).")
                    continue
                # Después de verificar que no hayan signos especiales transformo a entero
                cantidad = int(cantidad)
                if cantidad <= 0:
                    print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).\n")
                    continue
                break
            # Agrego la cantidad de ejemplares al nuevo título, utilizo append ya que ya existe un título asociado para agregarle sus ejemplares
            ejemplares.append(cantidad)
            print(f"\n✅ Se agrego exitosamente el título {nuevoTitulo} al catálogo con {cantidad} ejemplares.\n")
        # 7. Actualizar ejemplares (préstamo/devolución)
        case 7:
            # Si no hay títulos cargados no debe permitir actualizar ejemplares
            if not titulos:
                print(" ⚠️  No existen títulos en la lista. Para actualizar la cantidad de ejemplares primero debe ingresar títulos.\n")
                continue
            CANTIDAD = 1
            # En caso que existan muestro los títulos actuales para que el usuario seleccione al cual desea actualizar ejemplares
            print("\n"+"="*16+"Catálogo de libros"+"="*16)
            for i, titulo in enumerate(titulos):
                print(f"{i+1}. {titulo} ({ejemplares[i]})")
            print("="*50+"\n")
            
            # Verifico que la posición indicada exista dentro de la lista de títulos
            while True:
                posicion = input("\nIngrese el índice correcto del título cuyo número de ejemplares desea actualizar: ")
                if not posicion.isdigit():
                    print("\n ⚠️  Ingrese una posición valida.")
                    continue
                # Despues de verificar que no hayan signos especiales transformo a entero y resto 1 para que coincida con el índice
                posicion = int(posicion)-1
                if posicion < 0 or posicion >= len(titulos):
                    print("\n ⚠️  Ingrese una posición valida.")
                    continue
                break
            # Reinicio selección
            seleccion = 0
            while True:
                print("\n"+"="*50)
                print("Elija una de las opciones")
                print("="*50)
                for opcion in opciones_menu_actualizacion:
                    print(opcion)
                print("="*50)
                seleccion = int(input("Opción seleccionada: "))
                match seleccion:
                    case 1:
                        if ejemplares[posicion] > 0:
                            ejemplares[posicion] -= CANTIDAD
                            print(f"\n ✅ Se tomo prestado el título {titulos[posicion]} del catálogo, quedan {ejemplares[posicion]} ejemplares restantes.\n")
                            break
                        else:
                            print("\n ⚠️  No hay ejemplares disponibles para el título solicitado")
                            continue
                    case 2:
                        # Aumento en 1 los ejemplares del título seleccionado y lo muestro en pantalla
                        ejemplares[posicion] += CANTIDAD
                        print(f"\n✅ Devolución exitosa del título {titulos[posicion]}.\n")
                        break
                    case 3:
                        break
        # 8. Salir
        case 8:
            print("Saliendo...")
            break
        