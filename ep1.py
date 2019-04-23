# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fulano da Silva, fulanos@insper.edu.br
# - aluno B: Sicrano de Almeida, sicranoa1@insper.edu.br
import time
import random
def carregar_cenarios():
    cenarios={
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "auditorio":"ir para o auditorio",
                "quata":"sair do predio do insper",
                "requisito":''
                
            },
            "probabilidade":30,
            "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor, mas nao o ve em lugar algum",
            "opcoes": {
                "inicio": "Tomar o elevador e procurar ele em outro local",
             "requisito":''
            },
            "probabilidade":50,
            "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "ler um livro": "estudar para d-soft",
                "salas de estudo": "ir para um aquario de estudo em grupo",
            "itens":'chave auditorio',
             "requisito":''
            
            },
                'probabilidade':10,
                "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
      },
            "ler um livro":{
                "titulo": "sala teletransporte",
                "descricao": "voce encontrou sala de teletransporte, daqui voce pode escolher qualquer lugar para ir, parabéns"}
            , 
            "auditorio":{
                    "titulo": "salao do espetaculo",
                    "descrição" : "voce esta no auditorio do insper",
                    "opcoes":{
                            "predio1":"voltar para o saguao de entrada",
                             "palco":"subir no palco do auditorio",
                              "requisito":"chave auditorio"
                              
                              
            },
                    'probabilidade':0,
                    'monstros possiveis':[]
                
       },
                    "palco":{
                            "titulo": "apresentacao de duelo",
                            "descricao": "voce esta no palco e apareceu um inimigo",
                            "opcoes":{
                                    "auditorio":"para descer tera que derrotar seu adversario",
                                     "requisito":''
             },
                            'probabilidade':100,
                            'mostros possiveis':['cosplayer de gladiador','cosplayer de ninja']
                            
      },
                    "salas de estudo":{
                            "titulo":"aquario",
                            "descricao": "voce esta na sala de estudo em grupo",
                            "opcoes":{
                                    "biblioteca":"voltar para a biblioteca",
                                    "ler um livro":"estudar para alguma materia qualquer",
                            "requisito":''                                                       
           },
                            'probabilidade':30,
                            "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
    },
   
                            "terraco":{
                                    "titulo":"terraco do fim",
                                    "descricao":"voce esta no terraco do insper",
                                    "opcoes":{
                                            "cafe":"ir tomar um cafe no sexto andar",
                                            "raul":"o professor esta no terraco, lute com ele para tentar adiar o trabalho",
             },
                "requisito":'',
                            'probabilidade':80,
                            "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
   },         
                            "cafe":{
                                    "titulo":"salao do banquete",
                                    "descricao":"voce pede um cafe",
                                     "opcoes":{
                                             "quata":"sair do predio",
                                             "terraco":"voltar para o terraco",

            },
                                             "itens":['forca','bebida revigorante'],
                                       "requisito":'',
                                    'probabilidade':80
   },        
                                    "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2'],
                            
                            "raul":{
                                    "titulo":"professor raul",
                                    "descricao":"voce achou o professor, agora precisa lutar com ele para adiar o trabalho",
                                    "opcoes":{"acabar com isso":"voce se sente pronto, esta na hora de encarar seu ultimo desafio"},
                                    'probabilidade':100,
                                    'monstros possiveis':['Raul'],
                        
            },
                                    "requisito":'',                           
                           "quata":{
                                   "titulo":"rua quata",
                                   "descrição": " voce esta na rua do insper",
                                   "opcoes":{
                                           "predio 1": "ir para o predio velho",
                                           "predio 2":"ir para o predio novo",
            },
                                    "requisito":'',
                                    'probabilidade':80,
                                   "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO','veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
    },  
                                   "fablab":{
                                           "titulo":"laboratori da producao incansavel",
                                           "descricao":"voce esta em no FabLab do insper",
                                           "opcoes":{
                                                   "quata":"sair do predio",
                                                   "terraco": "subir para o terraco  do insper"   ,
                                                   "itens":'espada',
                                            "requisito":''
             },
                                                  "itens":'espada',
                                            "requisito":'',
                                            'probabilidade':100,
                                            'monstros possiveis':['tecnivo de corte a laser','tecnico de 3D']
    },
                                   "predio 1":{
                                          "titulo": "local anciao",
                                          "descricao": "voce esta no predio velho do insper",
                                          "opcaoes": {
                                                     "andar professor": "Tomar o elevador para o andar do professor",
                                                     "biblioteca": "Ir para a biblioteca",
                                                     "auditorio":"ir para o auditorio",
                                                     "quata":"sair para a rua",                
            },
                                        "requisito":'',
                                            "probabilidade":70,
                                            "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
                                          
        },                    
                                       
                                 "predio 2":{
                                         "titulo":"local inovado",
                                         "descricao":"voce esta no predio novo do insper",
                                         "opcoes":{
                                                 "fablab":"tomar o elevador para ir para o fablab",
                                                 "terraco":"tomar o elevador para ir para o terraco",
                                                 "sala de aula":"tomar o elevador para a sala de aula",
                                                 "quata":"sair para a rua",
            },
                                        "requisito":'',
                                     "probabilidade":70,
                                     "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
     },                            
                                "sala de aula":{
                                        "titulo":"sala 111",
                                        "descricao":"voce esta na sala de aula",
                                        "opcoes":{
                                                "predio 2":"tomar o elevador para descer para a entrada do predio"
           },
                                        "itens":'armadura',
                                        "requisito":'',
                                         "probabilidade":100,
                                         "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']},
                                "casa":{
                                        "titulo":"aceitar seu destino",
                                        "descricao":"voce usou o teleporte para voltar para casa e desistiu do EP1",
                                        "opcoes":{},
                                         "requisito":''}}  
    itens={'poder da criacao':{'descricao':'o mais poderoso item defensivo','modificacoes':{'def':200}},'armadura de PLA':{'descricao':'um item fabricado para a defesa','modificacoes':{'def':25}},'laser de corte':{'descricao':'a mais poderosa arma ofensiva','modificacoes':{'atk':100}},'espada de mdf':{'descricao':'um equipamento fabricado para o combate','modificacoes':{'atk':10}},'traje ninja':{'descricao':'um traje que oculta a sua presenca e outras surpresas','modificacoes':{'Hp':20,'atk':10}},'traje de glaiador':{'descricao':'um traje que revela sua ferossidade','modificacoes':{'def':20,'cura':5}},'calculadora cientifica':{'descricao':'te defende das contas dificeis','modificacoes':{'def':10}},'vassoura':{'descricao':'usada para ataques de medio alcanse','modificacoes':{'atk':10}},'caderno doproximo semestre':{'descricao':'o caderno de um veterano, te consede um bonus de vida no inico do co mbate', 'modificacoes':{'Hp':30}},'espada':{'descricao':'aumenta o dano de ataque','modificacoes':{'atk':5}},'chave auditorio':{'descricao':'permite acesso ao auditorio','modificacoes':{}},'forca':{'descricao':'aumenta o poder de ataque','modificacoes':{'atk':10}},'armadura':{'descricao':'aumenta a protecao','modificacoes':{'def':15}},'bebida revigorante':{'descricao':'funcoes adicionais ','modificacoes':{'cura': 5}}}
                              



                            
    player={"Hp":100,"atk":5,"def":10,"ataques":{'soco':[90,4],'chute na coxa':[70,8],'chute cabeca':[30,15]}}
    lista_monstros={'veterano':{"Hp":50,"atk":3,"def":15,
                            "ataques":{'soco':[90,4],'chute costela':[60,8]},
                            'recompensas':{"Hp":30,"atk":1,"def": 1},
                            'loot':{'caderno do proximo semestre':30}},
                'faxineiro':{'Hp':40,'atk':6,'def':10,
                             'ataques':{'vassourada':[70,6],'jogar o carrinho':[50,10]},
                             'recompensas':{'Hp':40,'atk':3,'def':1},
                             'loot':{'vassoura':30}},
                'aluno de ADM/ECO':{'Hp':70,'atk':2,'def':20,
                                    'ataques':{'reclamar do grupo':[100,3],'tapa':[80,5]},
                                    'recompensas':{'Hp':30,'atk':1,'def':5},
                                    'loot':{'calculadora cientifica':30}},
                'cosplayer de gladiador':{'Hp':100,'atk':4,'def':20,
                                          'ataques':{'clava':[30,12],'chute frontal':[40,10],'ombrada':[50,8]},
                                          'recompensa':{'Hp':50,'atk':3,'def':5},
                                          'loot':{'traje de gladiador':20}},
                'cosplayer de ninja':{'Hp':70,'atk':10,'def':5,
                                      'ataques':{'katana':[75,7],'adaga':[85,6],'shuriken':[100,5]},
                                      'recompensas':{'Hp':70,'atk':6,'def':2},
                                      'loot':{'traje ninja':20}},
                'tecnivo de corte a laser':{'Hp':100,'atk':25,'def':30,
                                            'ataques':{'espada de acrilico':[90,5],'porrete de mdf':[75,8],'caixa de papelao':[100,2],'laser cortante':[20,15]},
                                            'recompensas':{'Hp':80,'atk':10,'def':0},
                                            'loot':{'espada de mdf':60,'laser de corte':10}},
                'tecnico de 3D':{'Hp':150,'atk':12,'def':50,
                                 'ataques':{'chicote de filamento':[80,5],'espinhos de pet-G':[70,6],'caxao de de pla':[30,15]},
                                 'recompensas':{'Hp':70,'atk':0,'def':15},
                                 'loot':{'armadura de PlA':60,'poder da criacao':10}},
                'veterano lv2':{"Hp":120,"atk":15,"def":40,
                            "ataques":{'soco':[90,6],'chute costela':[60,10]},
                            'recompensas':{"Hp":60,"atk":2,"def": 2},
                            'loot':{}},
                'faxineiro lv2':{'Hp':120,'atk':20,'def':30,
                             'ataques':{'vassourada':[70,6],'jogar o carrinho':[50,10]},
                             'recompensas':{'Hp':70,'atk':3,'def':1},
                             'loot':{}},
                'aluno de ADM/ECO lv2':{'Hp':160,'atk':4,'def':50,
                                    'ataques':{'reclamar do grupo':[100,6],'tapa':[80,10]},
                                    'recompensas':{'Hp':30,'atk':1,'def':5},
                                    'loot':{}},
                'Raul':{'Hp':500,'atk':50,'def':100,
                        'ataques':{'nota da PI':[100,8],'o codigo das 1001 linhas':[75,15],'funcao de dano':[100,(0.5*player['Hp']+player['def'])/'Raul'['atk']],'inception de dicionarios':[50,20],'Prazo inadiavel':[100,20]},
                        'recompensas':{},
                        'loot':{}}}        
    nome_cenario_atual="inicio"

    return cenarios, nome_cenario_atual,player,lista_monstros,itens


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual,player,lista_monstros,itens = carregar_cenarios()
   
    win=False
    game_over = False
    inventario={}
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        # Aluno A: substitua este comentário pelo código para imprimir 

        
        print(cenario_atual["titulo"])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        
        
    if cenario_atual['item'] not in itens:
       inventario[cenario_atual[itens]]=itens[cenario_atual['itens']]
       for k,v in inventario:
            print("agora voce tem{0}{1}".format(cenario_atual['itens'],itens[cenario_atual['itens']['descricao']]))
            print ("itens")



        
        
    if nome_cenario_atual=="ler um livro":
                nome_cenario_atual=input("escolha um lugar do insper para ir ")
                while nome_cenario_atual not in cenarios:
                     nome_cenario_atual =input("essa escolha nao foi valida, decida outro ")
    else:
            opcoes = cenario_atual['opcoes']
            if len(opcoes) == 0:
                print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                game_over = True
            else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código

                for k,v in cenario_atual["opcoes"].items():
                    print("digite {0} para {1}".format(k,v))
                escolha =input("qual sua escolha? ")
                if escolha in opcoes:
                    if cenarios[escolha]['requisito'] in inventario:
                        nome_cenario_atual = escolha
                    else:
                        print('voce precisa do item {0} para entrar nessa sala'.format(cenarios[escolha]['requisito']))
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True
                    
                rolagem=random. rendint(0,100)
                if rolagem<=cenario_atual['probabilidade']:
                    monstro=random.choice(cenario_atual['monstros possiveis'])
                    combate=True
   
                if combate:
                    if monstro=='Raul':
                        print('Raul: então você quer atrasar a entrega do EP!?')
                        time.sleep(0.5)
                        print('Patético, mas eu não esperava nada mais de alguém como você.')
                        time.sleep(0.5)
                        print('se acha que pode me vencer lhe mostrarei o meu poder')
                    else:
                        print("voce esta enfrentando um {0}".format(monstro))
                        m=lista_monstros[monstro]
                        Hp0=m["Hp"]
                        print("ataque do inimigo {0}, seu ataque{1}".format(m["atk"],player["atk"]))
                        print("defesa do inimigo {0}, sua defesa{1}".format(m["def"],player["def"]))
                        print("vida do inimigo {0}, sua vida{1}".format(m["Hp"],player["Hp"]))
                        bonus={}
                        for v in inventario.values():
                            for k,v2 in v['modificacoes'].items():
                                if k not in bonus:
                                    bonus[k]=v2
                                else:
                                    bonus[k]+=v2
                        player['Hp']+=bonus['Hp']
                        while player["Hp"]>0 and m["Hp"]>0:
                            player['Hp']+=bonus['cura']
                            print('seus ataques são:')
                            for k,v in player["ataques"].items():
                                print("{0} precisão:{1}, dano:{2}".format(k,v[0],v[1]))
                            Atp=input("qual ataque voce quer dar? ")
                            while Atp not in player["ataques"]:
                                At=input("este nao e um ataque valido, insira um que seja ")
                            chance=random.rendint(1,10)
                            if chance<player['ataques'][Atp][0]:
                                perda=(player['ataques'][Atp][1]*(player["atk"]+bonus['atk'])-m["def"])
                                if perda>0:
                                    m['Hp']-=perda
                                    print('voce atacou o  {0} com {1}, a vida dele esta em{2}'.format(m,At,m["Hp"]))
                                else:
                                    print('nao suriu efeito')
                            else:
                                print('voce errou o ataque')
                            Atm=random.choice(m["ataques"])
                            chance=random.rendint(1,10)
                            if chance<m['ataques'][Atp][0]:
                                perda=(m['ataques'][Atm][1]*m["atk"]-(player["def"]+bonus['def']))
                                if perda>0:
                                    player['Hp']-=perda
                                    print('{0} atacou voce com {1}, a sua vida esta em{2}'.format(m,At,player["Hp"]))
                            else:
                                print('o inimigo tentou atacar voce com {0}, mas errou'.format(Atm))
                        if player['Hp']<=0:
                            print('voce foi derrotado pelo {0}'.format(m))
                            game_over=True
                        else:
                            if monstro=='Raul':
                                print('Raul: Impossivel! Como um ser inferior conseguiu me ferir')
                                time.sleep(0.5)
                                print('Parabés seu verme insolente, você foi capaz de superar 1% do meu poder.')
                                time.sleep(0.5)
                                print('como prova de seu feito adiarei a entrega do EP1')
                                time.sleep(0.5)
                                print('mas não terei tanta misericórdia no EP final')
                                time.sleep(0.5)
                                print('esteja pronto')
                                game_over=True
                                win=True
                            else:
                                print('voce derrotou o {0}, aqui estão seus premios'.format(m))
                                for k,v in m['recompensas'].items:
                                    print('voce recebu {0} de {1}'.format(v,k))
                                    player[k]+=v
                                    m['Hp']=Hp0
                                ganho=random.choice(m['loot'])
                                chance=random.randint(1,100)
                                if chance<m['loot'][ganho]:
                                    if ganho not in inventario:
                                        inventario[ganho]=itens[ganho]
                                        print('voce conseguiu o item {0} do monstro'.format(ganho))
                                combate=False    
    if win==True:
        print('você conseguiu adiar o EP1, mição completa')
        time.sleep(10)
        print('CONTINUA NO EP FINAL')       
    else:
        if player['Hp']<=0: 
            print('você foi derrotado pelo {0}'.format(m))
        print('sua falha fez com que o prazo do EP não fosse adiado')
        print('aproveite a DP de D soft')

# Programa principal.
if _name_ == "_main_":
    main()