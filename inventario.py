itens={'espada':{'descricao':'aumenta o dano de ataque','atk':5},'chave auditorio':{'descricao':'permite acesso ao auditorio','modificacoes':[]},'forca':{'descricao':'aumenta o poder de ataque','modificacoes':'atk':6},'armadura':{'descricao':'aumenta a protecao','modificacoes':{'def':5}},'bonus':{'descricao':'funcoes adicionais ','modificacoes':'atk def Hp ou cura': 4}}
inventario={}


    if cenario_atual['item'] not in itens:
       inventario[cenario_[itens]]=itens[cenario_atual['itens']]
        for k,v in inventario:
            print("agora voce tem{0}{1}".format(cenario_atual['itens'],itens[cenario_atuar['itens']['descricao']]))
            print ("itens")



   