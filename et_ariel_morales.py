#diccionario prendas... Nombre, categoria, talla, color, material, unisex
prendas = {
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',
True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester',
True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon',
True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon',
False]
}

#diccionario bodegas... precio, unidades
bodega = {
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2]
}

def leer_opcion():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de prendas por rango de precio")
        print("3. Actualizar precio de prenda")
        print("4. Agregar prenda")
        print("5. Eliminar prenda")
        print("6. Salir")
        print("=====================================")

        try:
            opcion = int(input("selecciona una opcion: "))
            if opcion >= 1 and opcion <=6 :
                return opcion
            else:
                print("Seleccione una de las opciones")
        except ValueError:
            print("Ingrese una variable valida")

def unidades_categorias(categoria):
    total_unidades = 0
    for codigo, datos in prendas.items():
        if categoria.lower() == datos[0].lower():
            total_unidades += bodega[codigo][1]
    print(f"categoria seleccionada: {categoria} tiene {total_unidades} en total")

def busqueda_precio(p_min, p_max, prendas, bodega):
    prenda_encontrada = []
    for codigo, datos in bodega.items():
        if p_min <= datos[0] and datos[0] <= p_max and datos[1] > 0:
            nombre = prendas[codigo][0]
            formato = f"{nombre}--{codigo}"
            prenda_encontrada.append(formato)
    prenda_encontrada.sort()
    
    for prenda in prenda_encontrada:
        print(prenda)
    
def buscar_codigo(codigo):

    if codigo in bodega:
        return True
    else:
        print("El codigo no existe")
        return False
    
def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo) == True:
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False
    
def validar_codigo(codigo):
    return codigo.strip() != "" and not buscar_codigo()

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_talla(talla):
    return talla.strip() != ""

def validar_color(color):
    return color.strip() != ""

def validar_material(material):
    return material.strip() != ""

def validar_es_unisex(es_unisex):
    return es_unisex.lower() in ["s","n"]

def validar_precio(precio):
    try:
        precio = int(precio)
        return precio > 0
    except:
        return False

def validar_unidades(unidades):
    try:
        unidades = int(unidades)
        return unidades > 0
    except:
        return False

def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
    if buscar_codigo(codigo):
        return False
    prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex ]
    bodega[codigo] = [precio, unidades]
    return True

def eliminar_prenda(codigo):
    if buscar_codigo(codigo):
        del prendas(codigo)
        del bodega(codigo)
        return True
    else:
        return False


while True:
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese la categoria a buscar:")
        unidades_categorias(categoria)
    elif opcion == 2:
        try:
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
        except ValueError:
            print("Ingrese una variable valida")
        busqueda_precio(p_min, p_max, prendas, bodega)
    elif opcion == 3:
        
        codigo = input("Ingrese el codigo de la prenda que desea actualizar: ")

        try:
            nuevo_precio = int(input("Ingrese el nuevo precio de la prenda: "))
            
        except ValueError:
            print("Ingrese una variable valida")
        actualizar_precio(codigo, nuevo_precio)

    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        print( "Programa finalizado.")
        break