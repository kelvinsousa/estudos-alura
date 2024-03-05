from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

bebida_suco_melancia = Bebida('Suco de Melancia', 8.0, 'grande')
bebida_suco_melancia.aplicar_desconto()
bebida_garapa = Bebida('Caldo de Cana', 10.00, 'jarra')
bebida_garapa.aplicar_desconto()
prato_paozinho = Prato('Paozinho tostado', 5.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 15.00, 'doce', 'pequeno')
sobremesa_sorvete = Sobremesa('Sorvete Flocos', 10.00, 'sorvete', 'médio')
sobremesa_torta_morango = Sobremesa('Torta de Morango', 50.00, 'torta', 'grande')
sobremesa_torta_morango.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco_melancia)
restaurante_praca.adicionar_no_cardapio(bebida_garapa)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)
restaurante_praca.adicionar_no_cardapio(sobremesa_sorvete)
restaurante_praca.adicionar_no_cardapio(sobremesa_torta_morango)


def main():
    restaurante_praca.exibir_cardapio # propriedade não precisa adicionar () no final.



if __name__ 98iuy76== '__main__':
    main()