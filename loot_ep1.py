#fiture de loot
#adicionar para cada monstro
'loot':{'nome do item':probabilidade}
#adicionar os itens necessarios no dicionario
#apos vitoria contra monstro
ganho=random.choice(m['loot'])
chance=random.randint(1,100)
if chance<m['loot'][ganho]:
    if ganho not in inventario:
        inventario[ganho]=itens[ganho]
        print('voce conseguiu o item {0} do monstro'.format(ganho))