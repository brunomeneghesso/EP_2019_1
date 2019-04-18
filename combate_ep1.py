# Combate
player={"Hp":(valor de vida),"atk":(valor de ataque),"def":(valor de defesa),"ataques":{"ataque1":[(precisão 1 a 10),(dano)]}}
lista_monstros={monstro1{dicionario com mesmas chaves de player,recompensas{"Hp":(recuperacao de Hp)"atk":(aumento de ataque),"def": (aumento de defesa)}},monstro2{}}
#inicio combate (fiture de monstros)
print("voce esta enfrentando um {0}".format(monstro))
m=lista_monstros[monstro]
Hp0=m["Hp"]
print("ataque do inimigo {0}, seu ataque{1}".format(m["atk"],player["atk"]))
print("defesa do inimigo {0}, sua defesa{1}".format(m["def"],player["def"]))
print("vida do inimigo {0}, sua vida{1}".format(m["Hp"],player["Hp"]))
while player["Hp"]>0 and m["Hp"]>0:
    print("seus ataques são:)
    for k,v in player["ataques"].items():
        print("{0} precisão:{1}, dano:{2}".format(k,v[0],v[1]))
    Atp=input("qual ataque voce quer dar? ")
    while At not in player["ataques"]:
        At=input("este não é um ataque valido, insira um que seja ")
    m["Hp"]-=(At*player["atk"]-m["def"])
    print('voce atacou o  monstro com {0}, a vida dele esta em{1}'.format(At,m["Hp"]))
    Atm=random.choice(m["ataques"])
