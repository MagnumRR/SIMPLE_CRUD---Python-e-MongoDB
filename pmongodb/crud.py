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

# Funcionalidade desconexão com o banco MongoDB
def desconectar(con):
    # se existir a conexão é realizado o processo de desconectar do banco
    if con:
        con.close()

# Funcionalidade listar os "documentos/registros" da tabela(coleção) "produtos"  
def listar():
    
    # Chamar conexão
    con = conectar()
    
    # Acessar a coleção específica
    db = con.p_mongodb
    
    # Tratamento ao banco
    try:
        if db.produtos.count_documents({}) > 0:
            # comando "find" - bscar itens/documentos na coleção
            produtos = db.produtos.find()
            
            print('\t--------------------- PRODUTOS ---------------------\n')
            print(tabulate(produtos, headers='keys', tablefmt="grid"))
            print('------------------------------------------------------\n')
        else:
            print('\n>>> Não existem produtos cadastrados <<<')
    except errors.PyMongoError as e:
            print(f'\n>>> Erro ao acessar o banco: {e} <<<')
    desconectar(con)            

# Funcionalidade inserir novos "documentos/registros" na tabela(coleção) "produtos"  
def inserir():
    print('------------ NOVO PRODUTO -------------')
    # Chamar conexão
    con = conectar()
    
    # Acessar a coleção específica
    db = con.p_mongodb
    
    # Recebendo entrada do usuário
    nome = input('Produto: ')
    preco = float(input('Preço: '))
    estoque = int(input('Quantidade: '))
    
    # Tratamento ao banco
    try:
        # Adicionando novo documento a coleção "produtos"
        db.produtos.insert_one(
            {
                'nome': nome,
                'preco': preco,
                'estoque': estoque
            }
        )
        print('------------------------------------')
        print(f'\n>>> O produto {nome} foi adicionado com sucesso! <<<')
    except errors.PyMongoError as e:
       print(f'\n>>> Falha ao cadastrar o produto - {e} <<<')
    desconectar(con)            
