from pymongo import MongoClient
import json
import os

def cargar_semilla():
    # Conexión local a MongoDB (misma base de datos y colección que DAO.py)
    client = MongoClient('mongodb://localhost:27017')
    db = client['PokemonDB']
    collection = db['Pokemones']
    
    ruta_json = 'pokemones_seed.json'
    
    if not os.path.exists(ruta_json):
        print(f"¡Error! No se encontró el archivo {ruta_json}")
        return

    with open(ruta_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    registrados = 0
    omitidos = 0
    
    for doc in datos:
        # Verifica si la ID ya existe para evitar errores de clave duplicada
        if collection.count_documents({"_id": doc["_id"]}) == 0:
            collection.insert_one(doc)
            registrados += 1
        else:
            omitidos += 1
            
    print("--- POBLAMIENTO DE BASE DE DATOS FINALIZADO ---")
    print(f"Pokémon registrados correctamente: {registrados}")
    print(f"Pokémon ya existentes (omitidos): {omitidos}")
    
    client.close()

if __name__ == '__main__':
    cargar_semilla()