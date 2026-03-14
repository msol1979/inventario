
from bd.conexion import obtener_conexion

def listar():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    cursor.close()
    conexion.close()

def agregar():
    nombre = input('Nombre del producto: ')
    precio = input('Precio: ')
    stock = input('Stock: ')
    conexion = obtener_conexion()
    cursor   = conexion.cursor()
    sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, precio, stock))
    conexion.commit()
    print("Producto agregado correctamente!")
    cursor.close()
    conexion.close()

def actualizar():
    id = input('ID del producto a actualizar: ')  
    nombre = input('Nuevo nombre: ')
    precio = input('Nuevo precio: ')
    stock = input('Nuevo stock: ')
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = 'UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id=%s'
    cursor.execute(sql, (nombre, precio, stock, id))
    conexion.commit()
    print('Stock actualizado correctamente')
    cursor.close()
    conexion.close()


def eliminar():
    id = input('ID del producto a eliminar: ')
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = 'DELETE FROM productos WHERE id=%s'
    cursor.execute(sql, (id,))
    conexion.commit()
    print('Producto eliminado correctamente!')
    cursor.close()
    conexion.close()