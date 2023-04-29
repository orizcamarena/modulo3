
from pymongo import MongoClient
import sys 

try:
    def connect_to_mongodb():
        client = MongoClient('mongodb://localhost:27017')
        return client
    def createDocument(baseDatos, document):
        result = baseDatos.insert_one(document)
        print("Document create with ID", result.insert.id)


    def principal():
        client = connect_to_mongodb()
        db = client['orizeida']
        baseDatos = db['tareaMongo']

        menu = """
    \n-----------------Menu---------------------
    a) Agragar nueva palabra:
    b) Eliminar palabra existente: 
    c) Ver Significado de palabra:
    d) Salir.
    ------------------------------------------
    Selecciona una opción: """
        option = ""
        while option != 'd': 
            option = input(menu)
            if  option == 'a':
                palabra = input('Agragar nueva palabra: ')
                significado = input('Ingrese el significado: ')
                agragarPalabra(baseDatos, palabra, significado)
            if option == 'b':
                palabra = input('Eliminar palabra existente: : ')
                eliminarpalabra(baseDatos, palabra)
                print(f"Palabra eliminada:{palabra}")
            if option == 'c':
                palabra = input('Ver Significado de palabra: ')
                significado = get_significado(palabra)
            if significado:
                print(f"El significado de '{palabra}' es: {significado[0]}")
            else:
                print(f"Palabra '{palabra}' no encontrada")
        else:
            print("\nEl programa ha finalizado, bye...")
            sys.exit()


    def createDocument(baseDatos, document):
        result = baseDatos.insert_one(document)
        print("Document create with ID", result.insert.id)

   
    def get_significado(baseDatos, palabra):
        result = baseDatos.insert_one({'palabra': palabra})
        if result:
            return result['significado']
        else:
            return None 
    
    def get_salir(baseDatos, palabra):
        result = baseDatos.insert({'palabra': palabra})
        if result:
           return result['significado']
        else:
          return None
    

    def agragarPalabra(baseDatos, palabra, significado):
        result = baseDatos.insert_one({'palabra': palabra, 'significado': significado})
        return result.inserted_id

    def eliminarpalabra(baseDatos, palabra):
        query ={"palabra":palabra}
        result = baseDatos.delete_one(query)
        print(result.delete_count,"documents delete.")

    if __name__ == '__main__':
        principal() 



finally:
    connection =connect_to_mongodb()
    connect_to_mongodb().close