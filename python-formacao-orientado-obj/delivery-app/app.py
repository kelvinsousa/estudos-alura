import os
from time import sleep

restaurantes = [
                  {'nome': 'PizzaHut', 'categoria': 'Pizza', 'ativo': False }
                , {'nome': "Mc Donald's", 'categoria': 'Fast-Food', 'ativo': False}
                , {'nome': 'Grilleto', 'categoria': 'Comida brasileira', 'ativo': True}
]

def exibir_nome_app():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""
        █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
        ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """)

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair')

def opcao_invalida():
    '''Essa função informa ao usuário que a opção é inválida e chama o Menu'''
    print('Opcao Inválida!')
    voltar_menu_principal()
       
def finalizar_app():
    '''Essa função é responsável por finalizar o app'''
    exibir_subtitulos('Finalizando o app...')
    sleep(1)
    os.system('cls') #limpando o terminal 'clear'

def voltar_menu_principal():
    '''Função responsável por chamar o Menu'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()
    
def exibir_subtitulos(texto):
    '''Função responsável por criar o subtítulo das opções'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print() #para pular linha

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do resturante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria para o {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante foi {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    '''Essa função lista os restaurantes já cadastrados'''
    exibir_subtitulos('Listando os restaurantes...')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' #conceito de ternário para econimizar código
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')    
    voltar_menu_principal()


def alternar_estado_restaurante():
    '''Essa função altera o status do restaurante de True para False ou vice-versa'''
    exibir_subtitulos('Alternando estado do restaurante...')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            print('Restaurante encontrato!')
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # o not inverte o estado, não precisamos assim validar se é true passar para false ou vice versa.
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            voltar_menu_principal()
            
    if not restaurante_encontrado: # if não verdadeiro, mesma coisa de restaurante_encontrado == false
        cadastro = input(f'O restaurante {nome_restaurante} não foi localizado na base.. Deseja cadastrá-lo: (S/N) ').upper().strip()
        
        if cadastro == 'S':
            cadastrar_novo_restaurante()
        else:
            main()
    
def escolher_opcao():
    '''Função responsável por receber a opção escolhinha pelo usuário no Menu ao usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    '''Função principal'''
    os.system('cls')
    
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()
    finalizar_app()
    
if __name__ == '__main__':
    main()