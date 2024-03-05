from random import randrange



def jogar():

    msg_abertura()
    
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    tentativas_restante = 7
    
    while(not enforcou and not acertou):
        
        chute = str(input('Qual letra? ')).upper().strip()
        
        if chute in palavra_secreta:   
            i = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[i] = chute
                i += 1
        else:
            tentativas_restante -= 1
            print(f'A letra {chute} não contém na palavra secreta, ainda restam {tentativas_restante} chances.')    
            desenha_forca(tentativas_restante)
        
        print(letras_acertadas)
        enforcou = tentativas_restante == 0
        acertou = '_' not in letras_acertadas
        
    if enforcou:
        msg_perdedor(palavra_secreta)
    else:
        msg_ganhador(palavra_secreta, tentativas_restante)
        



def msg_abertura():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("C:/Estudos/Alura/python-avancando-na-linguagem/alura-python/jogos/palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        palavras.append(linha.strip())        
    arquivo.close()
    
    posicao = randrange(0, len(palavras))
    
    palavra_secreta = palavras[posicao].upper()
    
    return palavra_secreta

def inicializa_letras(palavra_secreta):
    lista = ['_' for i in palavra_secreta]
    return lista

def msg_ganhador(palavra_secreta, tentativas_restante):
    print(f'Parabéns! Você descobriu nossa palavra secreta {palavra_secreta} e ainda restavam {tentativas_restante} tentativas' )    
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def msg_perdedor(palavra_secreta):
    print(f'Puxa, você foi enforcado! Não conseguiu descobrir a palavra secreta que era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(tentativas_restante):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas_restante == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restante == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restante == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restante == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restante == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas_restante == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas_restante == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
if(__name__ == "__main__"):
    jogar()

