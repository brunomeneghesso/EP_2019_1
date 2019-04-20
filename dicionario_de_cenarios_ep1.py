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
                            
            
    nome_cenario_atual = "inicio"
