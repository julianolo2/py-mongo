from pymongo import MongoClient



# função em python é declarada utilizando a key word def : define

def get_database(database):
    # var cliente recebe o objeto cliente MongoDB
    client = MongoClient("mongodb://localrost:27017")
    # cliente = MongoCliente(database="localrost",port="27017")
    return client[database]

def insert_farm(farm):
    #sere uma nova fazenda
    db = get_database("class_19004") #conectando no banco a salvando a conexão na var DB
   #con.colletion.funcao

   ret = db.farms.insert_one(farm)

# bloco que inicia um programa em python
def printName():
   print("Diego")

#if __name__ == "__main__":
    #print("Funcionou...")
    #printName("Andressa")
    #get_database("database")
    #insert_farm()
if __name__ == "__main__":
    #python listas, tuplas, dicionários
    # mongo JSONs {"field":"value"}

newFarm ={
    "name": "Farm's Python 1"
    "maneger": "João quebra toco"
}
#arm. na var id o último id inserido
ID = insert_farm(newFarm)
# imprimindo a mensagem com o ID da fazendo gerado pelo mongoBD
print(F"Fazenda inserida.ID:{id}")
