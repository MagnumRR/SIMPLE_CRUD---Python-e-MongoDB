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

# Funcionalidade atualizar "documentos/registros" na tabela(coleção) "produtos" 
def atualizar():
    print('------------ ATUALIZAR PRODUTO -------------')
    # Chamar conexão
    con = conectar()
    
    # Acessar a coleção específica
    db = con.p_mongodb
    
    # Recebendo "Id" do usuário
    _id = input('Informe o Id: ')
    # Atribuindo a consulta ao documento, com base no "_id"
    comp = db.produtos.find_one({"_id": ObjectId(_id)})
    # Tratamento da atualização
    try:
        # Se existir o documento
        if comp:
            # É atribuído o valor da chave "nome"
            nome = comp['nome']
            # Realiza-se a verificação
            if input(f'Deseja atualizar o produto: {nome}?: ') == 's':
                # Se não ocorrer alteração nos dados permaneçe os existentes.
                n_nome = input('Informe o nome: ') or comp['nome']
                
                preco_a = comp['preco']
                at_preco = input(f'Atualizar [{preco_a}]: ')
                n_preco = float(at_preco) if at_preco else preco_a
                
                estoque_a = comp['estoque']                                    
                at_estoque = input(f'Atualizar quantidade [{estoque_a}]: ')
                n_estoque = int(at_estoque) if at_estoque else estoque_a
                
                # Atribuição para atualizar 1 (um) registro/documento
                res = db.produtos.update_one(
                    {"_id": ObjectId(_id)}, # Utilização do "ObjectId" para vincular-se ao atributo criado
                    {
                        # Recurso "Set" permite focar no respecitvo campo a ser atualizado 
                        '$set': {
                            'nome': n_nome,
                            'preco': n_preco,
                            'estoque': n_estoque
                        } 
                    }
                )
                # Realiza um conferência, com base na contagem de registros atualizados
                if res.matched_count == 1:
                    print(f'\n>>> O produto {nome} foi atualizado com sucesso! <<<')
                else:
                    print('\n>>> Não foi possível atualizar o produto <<<')
            else:
                print('\n>>> Atualização cancelada <<<')
        else:
            print('\n>>> Não existem produtos a serem atualizados <<<')    
    except errors.PyMongoError as e:
        print(f'\n>>> Falha na conexão com o banco: {e} <<<')
    except InvalidId as f:
        print(f'\n>>> Falha na conexão com o banco: {f} <<<')            
    desconectar(con)         

# Funcionalidade excluir "documentos/registros" na tabela(coleção) "produtos" 
def deletar():
    print('------------ EXCLUIR PRODUTO -------------')
    # Chamar conexão
    con = conectar()
    
    # Acessar a coleção específica
    db = con.p_mongodb
    
    # Recebendo "Id" do usuário
    _id = input('Informe o Id: ')
    
    # Atribuindo o nome do produto, conforme "_id"
    cons = db.produtos.find_one({"_id": ObjectId(_id)})
    # Atribuindo o valor da chave "nome"
    nome = cons['nome']
    # Tratamento ao excluir documentos (produtos)
    try:
        if cons:
            # Confirmação de exclusão
            if input(f'Deseja excluir o produto: {nome}? >>> ') == 's':
                res = db.produtos.delete_one(
                    {
                        '_id': ObjectId(_id)
                    }
                )
                # Conferência: se houver um registro excluído
                  
                if res.deleted_count == 1:
                    print('\n>>> O produto foi excluido com sucesso! <<<')
                else:
                    print('\n>>> Não foi possível excluir o produto <<<')    
            else:
                print('\n>>> Exclusão cancelada! <<<')
        else:
            print('\n>>> Não há produtos a serem excluídos <<<')        
    except errors.PyMongoError as e:
        print(f'\n>>> Falha na conexão com o banco: {e} <<<')
    except InvalidId as f:
        print(f'\n>>> Falha na conexão com o banco: {f} <<<')     
    desconectar(con)            

# Funcionalidade Menu
def menu():
    # Painel, cuja as opções acionam as respectivas funcionalidades
    print('========= PAINEL =========')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    print('5 - Sair.')
    print('===========================')
    # Loop de processos
    while True:
        opcao = int(input('Opção >>>:  ')) # Usuário escolhe a opção desejada
        if opcao in [1, 2, 3, 4, 5]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            elif opcao == 5:
                print('\n>>> Operação encerrada. <<<')
                break
            else:
                print('\n>>> Opção inválida. Tente novamente: ') # Se inválida, retorna a opção
            if input('Nova consulta (s- sim / n - não)?: ').lower() == 's': # Nova consulta ou finaliza
                continue
            else:
                print('\n>>> Processo encerrado. <<<')
                break 
