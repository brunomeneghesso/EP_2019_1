# Combate
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
#inicio combate (fiture de monstros)
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
        chance=randon.rendint(1,10)
        if chance<player['ataques'][Atp][0]:
            perda=(player['ataques'][Atp][1]*(player["atk"]+bonus['atk'])-m["def"])
            if perda>0:
                m['Hp']-=perda
                print('voce atacou o  {0} com {1}, a vida dele esta em{2}'.format(m,At,m["Hp"]))
            else:
                print('voce errou o ataque')
        Atm=random.choice(m["ataques"])
        chance=randon.rendint(1,10)
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
        combate=False
    #linha adicional necessária para fiture de item