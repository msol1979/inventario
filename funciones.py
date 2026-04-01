
from bd.conexion import obtener_conexion

def listar():

    # conexión y consulta
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    # Interfaz
    # encabezado de la tabla
    print('\n' + '═' * 55) #Linea separadora
    print(f"{'ID':<5} {'NOMBRE':<25} {'PRECIO':>8} {'STOCK':>8}") #Texto a mostrar alineados a la izq(<) o a la der(>)
    print('═' * 55) #Linea separadora

    # filas de la tabla
    if len(productos) == 0:                # verifica si no hay productos
        print('  No hay productos cargados.')
    else:
        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<25} {producto[2]:>8.2f} {producto[3]:>8}")

    # pie de la tabla
    print('═' * 55)

    # Cierre
    cursor.close()
    conexion.close()

def agregar():
     # Validación del nombre
    while True:
        nombre = input('Nombre del producto: ')
        # strip() elimina espacios en blanco
        if nombre.strip() == '':          
            print('El nombre no puede estar vacío.')
        else:
            break                       
    # Validación de precio
    while True:
        try:
            # intenta convertir a decimal
            precio = float(input('Precio: ')) 
            break                              
        except ValueError:                   
            print('El precio debe ser un número. Ej: 99.99')

    # ── Validación de stock
    while True:
        try:
            # intenta convertir a entero
            stock = int(input('Stock: '))  
            break                          
        except ValueError:                 
            print('El stock debe ser un número entero. Ej: 100')

    # Coneccion y guardado
    conexion = obtener_conexion()
    cursor   = conexion.cursor()
    sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, precio, stock))
    conexion.commit()
    print("Producto agregado correctamente!")
    cursor.close()
    conexion.close()

def actualizar():
    # Valid. ID
    while True:
        try:
            id = int(input('ID del producto a actualizar: '))  
            break                          
        except ValueError:                
            print('El ID debe ser un número entero. Ej: 1')

    # Valid. del nombre
    while True:
        nombre = input('Nuevo nombre: ')
        if nombre.strip() == '':           
            print('El nombre no puede estar vacío.')
        else:
            break                          

    # Valid. de precio
    while True:
        try:
            precio = float(input('Nuevo precio: '))  # intenta convertir a decimal
            break                                     
        except ValueError:                          
            print('El precio debe ser un número. Ej: 99.99')

    # Valid. stock
    while True:
        try:
            stock = int(input('Nuevo stock: '))  # intenta convertir a entero
            break                               
        except ValueError:                       
            print('El stock debe ser un número entero. Ej: 100')

    # Coneccion y guardado
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = 'UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id=%s'
    cursor.execute(sql, (nombre, precio, stock, id))
    conexion.commit()
    print('Producto actualizado correctamente')  
    cursor.close()
    conexion.close()

def eliminar():
    # valid. ID
    while True:
        try:
            id = int(input('ID del producto a eliminar: '))  
            break                          
        except ValueError:                 
            print('El ID debe ser un número entero. Ej: 1')

    # Confirmación antes de eliminar
    confirmacion = input(f'¿Segura que querés eliminar el producto {id}? (s/n): ')
    if confirmacion.lower() != 's':        # lower() convierte a minúscula
        print('Eliminación cancelada.')
        return                             # sale de la función sin eliminar

    # Conexión y eliminación
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = 'DELETE FROM productos WHERE id=%s'
    cursor.execute(sql, (id,))
    conexion.commit()
    print('Producto eliminado correctamente!')  
    cursor.close()
    conexion.close()