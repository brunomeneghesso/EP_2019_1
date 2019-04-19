# Combate
player={"Hp":(valor de vida),"atk":(valor de ataque),"def":(valor de defesa),"ataques":{"ataque1":[(precisÃ£o 1 a 10),(dano)]}}
lista_monstros={monstro1{dicionario com mesmas chaves de player,'recompensas':{"Hp":(recuperacao de Hp)"atk":(aumento de ataque),"def": (aumento de defesa)}},monstro2{}}
#inicio combate (fiture de monstros)
print("voce esta enfrentando um {0}".format(monstro))
m=lista_monstros[monstro]
Hp0=m["Hp"]
print("ataque do inimigo {0}, seu ataque{1}".format(m["atk"],player["atk"]))
print("defesa do inimigo {0}, sua defesa{1}".format(m["def"],player["def"]))
print("vida do inimigo {0}, sua vida{1}".format(m["Hp"],player["Hp"]))
while player["Hp"]>0 and m["Hp"]>0:
    print("seus ataques sã0:)
    for k,v in player["ataques"].items():
        print("{0} precisão:{1}, dano:{2}".format(k,v[0],v[1]))
    Atp=input("qual ataque voce quer dar? ")
    while Atp not in player["ataques"]:
        At=input("este nao e um ataque valido, insira um que seja ")
    chance=randon.rendint(1,10)
    if chance<player['ataques'][Atp][0]:
        m["Hp"]-=(player[ataques[Atp][1]*player["atk"]-m["def"])
        print('voce atacou o  {0} com {1}, a vida dele esta em{2}'.format(m,At,m["Hp"]))
    else:
        print('voce errou o ataque')
    Atm=random.choice(m["ataques"])
    chance=randon.rendint(1,10)
    if chance<m['ataques'][Atp][0]:
        player["Hp"]-=(m['ataques'][Atm][1]*m["atk"]-player["def"])
        print('{0} atacou voce com {1}, a sua vida esta em{2}'.format(m,At,player["Hp"]))
    else:
        print('o inimigo errou o ataque')
if player['Hp']<=0:
    print('voce foi derrotado pelo {0}'.format(m))
    game_over=True
else:
    print('voce derrotou o {0}, aqui estão seus premios'.format(m))
    for k,v in m['recompensas'].items:
        print('voce recebu {0} de {1}'.format(v,k))
        player[k]+=v
    #linha adicional necessária para fiture de item