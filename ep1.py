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
                "quata":"sair do predio do insper" 
                
            },
            "probabilidade":30,
            "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor, mas nao o ve em lugar algum",
            "opcoes": {
                "inicio": "Tomar o elevador e procurar ele em outro local"
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
                "salas de estudo": "ir para um aquario de estudo em grupo"
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
                              "palco":"subir no palco do auditorio"
                              
                              
            },
                    'probabilidade':0,
                    'monstros possiveis':[]
                
       },
                    "palco":{
                            "titulo": "apresentacao de duelo",
                            "descricao": "voce esta no palco e apareceu um inimigo",
                            "opcoes":{
                                    "auditorio":"para descer tera que derrotar seu adversario"
             },
                            'probabilidade':100,
                            'mostros possiveis':['cosplayer de gladiador','cosplayer de ninja']
      },
                    "salas de estudo":{
                            "titulo":"aquario",
                            "descricao": "voce esta na sala de estudo em grupo",
                            "opcoes":{
                                    "biblioteca":"voltar para a biblioteca",
                                    "ler um livro":"estudar para alguma materia qualquer"                                                        
           },
                            'probabilidade':30,
                            "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
    },
   
                            "terraco":{
                                    "titulo":"terraco do fim",
                                    "descricao":"voce esta no terraco do insper",
                                    "opcoes":{
                                            "cafe":"ir tomar um cafe no sexto andar",
                                            "raul":"o professor esta no terraco, lute com ele para tentar adiar o trabalho"
             },
                            'probabilidade':80,
                            "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
   },         
                            "cafe":{
                                    "titulo":"salao do banquete",
                                    "descricao":"voce pede um cafe",
                                     "opcoes":{
                                             "quata":"sair do predio",
                                             "terraco":"voltar para o terraco"
            },
                                    'probabilidade':80,2']
   },        
                                    "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
                            
                            "raul":{
                                    "titulo":"professor raul",
                                    "descricao":"voce achou o professor, agora precisa lutar com ele para adiar o trabalho",
                                    "opcoes":{"acabar com isso":"voce se sente pronto, esta na hora de encarar seu ultimo desafio"},
                                    'probabilidade':100,
                                    'monstros possiveis':['Raul']
                        
            },
                           
                           "quata":{
                                   "titulo":"rua quata",
                                   "descrição": " voce esta na rua do insper",
                                   "opcoes":{
                                           "predio 1": "ir para o predio velho",
                                           "predio 2":"ir para o predio novo"
            },
                                   'probabilidade':80,
                                   "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO','veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
    },  
                                   "fablab":{
                                           "titulo":"laboratori da producao incansavel",
                                           "descricao":"voce esta em no FabLab do insper",
                                           "opcoes":{
                                                   "quata":"sair do predio",
                                                   "terraco": "subir para o terraco  do insper"                                      
             },
                                            'probabilidade':100
                                            'monstros possiveis':['tecnivo de corte a laser','tecnico de 3D']
    },
                                   "predio 1":{
                                          "titulo": "local anciao",
                                          "descricao": "voce esta no predio velho do insper",
                                          "opcaoes": {
                                                     "andar professor": "Tomar o elevador para o andar do professor",
                                                     "biblioteca": "Ir para a biblioteca",
                                                     "auditorio":"ir para o auditorio",
                                                     "quata":"sair para a rua" 
                
            },
                                            "probabilidade":70,
                                            "monstros possiveis":['veterano','faxineiro','aluno de ADM/ECO']
                                          
        },                    
                                    
    },   
                                 "predio 2":{
                                         "titulo":"local inovado"
                                         "descricao":"voce esta no predio novo do insper"
                                         "opcoes":{
                                                 "fablab":"tomar o elevador para ir para o fablab",
                                                 "terraco":"tomar o elevador para ir para o terraco",
                                                 "sala de aula":"tomar o elevador para a sala de aula"
                                                 "quata":"sair para a rua"
            },
                                     "probabilidade":70,
                                     "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
     },                            
                                "sala de aula":{
                                        "titulo":"sala 111"
                                        "descricao":"voce esta na sala de aula"
                                        "opcao":{
                                                "predio 2":"tomar o elevador para descer para a entrada do predio"
           },
                                         "probabilidade":100,
                                         "monstros possiveis":['veterano lv2','faxineiro lv2','aluno de ADM/ECO lv2']
                                "casa":{
                                        "titulo":"aceitar seu destino",
                                        "descricao":"voce usou o teleporte para voltar para casa e desistiu do EP1",
                                        "opcoes":{}
    }}
                            
    player={"Hp":100,"atk":5,"def":10,"ataques":{'soco':[90,4],'chute na coxa':[70,8],'chute cabeca':[30,15]}}
    lista_monstros={'veterano':{"Hp":50,"atk":3,"def":15,
                            "ataques":{'soco':[90,4],'chute costela':[60,8]},
                            'recompensas':{"Hp":30,"atk":1,"def": 1}},
                'faxineiro':{'Hp':40,'atk':6,'def':10,
                             'ataques':{'vassourada':[70,6],'jogar o carrinho':[50,10]},
                             'recompensas':{'Hp':40,'atk':3,'def':1}},
                'aluno de ADM/ECO':{'Hp':70,'atk':2,'def':20,
                                    'ataques':{'reclamar do grupo':[100,3],'tapa':[80,5]},
                                    'recompensas':{'Hp':30,'atk':1,'def':5}},
                'cosplayer de gladiador':{'Hp':100,'atk':4,'def':20,
                                          'ataques':{'clava':[30,12],'chute frontal':[40,10],'ombrada':[50,8]},
                                          'recompensa':{'Hp':50,'atk':3,'def':5}},
                'cosplayer de ninja':{'Hp':70,'atk':10,'def':5,
                                      'ataques':{'katana':[75,7],'adaga':[85,6],'shuriken':[100,5]},
                                      'recompensas':{'Hp':70,'atk':6,'def':2}},
                'tecnivo de corte a laser':{'Hp':100,'atk':25,'def':30,
                                            'ataques':{'espada de acrilico':[90,5],'porrete de mdf':[75,8],'caixa de papelao':[100,2],'laser cortante':[20,15]},
                                            'recompensas':{'Hp':80,'atk':10,'def':0}},
                'tecnico de 3D':{'Hp':150,'atk':12,'def':50,
                                 'ataques':{'chicote de filamento':[80,5],'espinhos de pet-G':[70,6],'caxao de de pla':[30,15]},
                                 'recompensas':{'Hp':70,'atk':0,'def':15}},
                'veterano lv2':{"Hp":120,"atk":15,"def":40,
                            "ataques":{'soco':[90,6],'chute costela':[60,10]},
                            'recompensas':{"Hp":60,"atk":2,"def": 2}},
                'faxineiro lv2':{'Hp':120,'atk':20,'def':30,
                             'ataques':{'vassourada':[70,6],'jogar o carrinho':[50,10]},
                             'recompensas':{'Hp':70,'atk':3,'def':1}},
                'aluno de ADM/ECO lv2':{'Hp':160,'atk':4,'def':50,
                                    'ataques':{'reclamar do grupo':[100,6],'tapa':[80,10]},
                                    'recompensas':{'Hp':30,'atk':1,'def':5}},
                'Raul':{'Hp':500,'atk':50,'def':100,
                        'ataques':{'nota da PI':[100,8],'o codigo das 1001 linhas':[75,15],'funcao de dano':[100,(0.5*player['Hp']+player['def'])/Raul['atk']],'inception de dicionarios':[50,20],'Prazo inadiavel':[100,20]},
                        'recompensas':{}}}        
    nome_cenario_atual = "inicio"

    return cenarios, nome_cenario_atual,player,lista_monstros


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

    cenarios, nome_cenario_atual = carregar_cenarios()
   
    win=False
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        # Aluno A: substitua este comentário pelo código para imprimir 

        
        print(cenario_atual["titulo"])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        
        
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
                    nome_cenario_atual = escolha
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
                        while player["Hp"]>0 and m["Hp"]>0:
                            print('seus ataques são:')
                            for k,v in player["ataques"].items():
                                print("{0} precisão:{1}, dano:{2}".format(k,v[0],v[1]))
                            Atp=input("qual ataque voce quer dar? ")
                                while Atp not in player["ataques"]:
                            At=input("este nao e um ataque valido, insira um que seja ")
                            chance=randon.rendint(1,10)
                            if chance<player['ataques'][Atp][0]:
                                perda=(player['ataques'][Atp][1]*player["atk"]-m["def"])
                                if perda>0:
                                    m['Hp']-=perda
                                    print('voce atacou o  {0} com {1}, a vida dele esta em{2}'.format(m,At,m["Hp"]))
                            else:
                                print('voce errou o ataque')
                            Atm=random.choice(m["ataques"])
                            chance=randon.rendint(1,10)
                            if chance<m['ataques'][Atp][0]:
                                perda=(m['ataques'][Atm][1]*m["atk"]-player["def"])
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