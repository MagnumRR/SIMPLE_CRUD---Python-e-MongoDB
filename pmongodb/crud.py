# Instalação da biblioteca MongoDB: "pymongo"
# Importação dos módulos MongoClient e erros da biblioteca pymongo
# Importação de erros do módulo "bson" dos arquivos mongo bd

from pymongo import MongoClient, errors
from bson.objectid import ObjectId #???
from bson.errors import InvalidId
from tabulate import tabulate

# Funcionalidade conexão com o banco MongoDB
def conectar():
        
    # Parâmetros de conexão com o MongoClient (local e porta)
    con = MongoClient('localhost', 27017)
    return con
