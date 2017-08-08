import random
# O random implementa números e palavras aleatórios
palavras = []
def p():
    while True:
        palanovas = input('Digite a palvra que você deseja usar:' )
        palavras.append(palanovas)# adiciona a palavra que você digitou a uma lista
        if palanovas == "":
            break

letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def principal():
    # A função def é usada para definir uma função
    """
    Função Princial do programa
    """
    print('F O R C A')
    p()
    # Print serve para imprimir algo na tela
    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True:
        # while True roda um looping enquanto ele for verdadeiro 
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        
        if perdeuJogo():
            # if avalia uma função
            print('Voce Perdeu!!!')
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break
        # break quebra um looping
        
def perdeuJogo():
    global FORCAIMG
    #global é um comando que indica que uma variavel para todo o programa
    if len(letrasErradas) == len(FORCAIMG):
        return True
    # return True/False informar o que vai retornar quando você chamar a função
    else:
        return False
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        # len retorna o número de caracteres de uma string 
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        # elif nos permite verificar expressões múltiplas, ele só será executado quando todas as condições anteriores forem falsas
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        # else avalia a expressão do teste e só executa se a condição for verdadeira
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:

        letrasErradas += palpite

    for letra in letrasCertas: #adiciona a letra certa no grupo de letras certas
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()
#random.choice(palavras).upper() colocam as letras em maiúsculo

    
principal()
