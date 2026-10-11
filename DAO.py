from pymongo import MongoClient

class DAO:
    def __init__(self):
        # Conexión local a MongoDB
        self.client = MongoClient('mongodb://localhost:27017')
        # Cambiado a la base de datos temática
        self.db = self.client['PokemonDB']
        # Cambiado a la colección de Pokémon
        self.collection = self.db['Pokemones']
        
    def cerrarConexion(self):
        self.client.close()
        
    def registrar(self, datos):
        r = self.collection.insert_one(datos)
        return str(r.inserted_id)
    
    def modificar(self, id, datos):
        r = self.collection.update_one({"_id": id}, {"$set": datos})
        return int(r.modified_count)
    
    def eliminar(self, id):
        r = self.collection.delete_one({"_id": id})
        return int(r.deleted_count)
    
    def listar(self, condicion):
        r = self.collection.find(condicion)
        return r