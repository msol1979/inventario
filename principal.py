
from funciones import *

def menu():
    while True:
        print('\n===== INVENTARIO DE PRODUCTOS =====')
        print('1. Listar productos')
        print('2. Agregar producto')
        print('3. Actualizar producto')
        print('4. Eliminar producto')
        print('5. Salir')
        
        opcion = input('Selecciona una opción: ')
        
        if   opcion == '1': listar()
        elif opcion == '2': agregar()
        elif opcion == '3': actualizar()
        elif opcion == '4': eliminar()
        elif opcion == '5': break
        else: print('Opción no válida, intenta de nuevo')

if __name__ == '__main__':
    menu()