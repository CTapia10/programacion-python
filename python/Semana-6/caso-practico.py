
# rol = "Admin"
rol = "Editor"
estado = "Inactivo"
if (rol == "Admin") or (rol == "Editor" and estado == "Activo"):
    print("Acceso Concedido")
else:
    print("Acceso Denegado")