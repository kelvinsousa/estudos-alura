from abc import ABC, abstractmethod
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self):
        pass
    
'''
A concepção é que, ao considerar a classe abstrata, não pretendemos que seja uma classe instanciada por item_cardapio que realize ações. Queremos que esse método sirva como um modelo para que outras classes derivadas o implementem.

Para dizer que uma classe é uma classe abstrata, vamos importar de um pacote chamado ABC. Podemos colocar na primeira linha: from abc import ABC, abstractmethod.

Guilherme: Agora, criamos agora esse método. Lembrando, o que queremos é que ele não seja um método que a classe item_cardapio crie objetos, instancie. Vamos apenas servir de modelo para as derivadas. Para isso, inserimos um decorator chamado @abstractmethod.

Podemos definir normalmente, def aplicar_desconto().

Laís: Só uma dúvida neste ponto. Se estamos pegando dessa classe ABC, é como se estivesse herdando dela também?

Guilherme: Sim, exatamente.

Laís: Precisamos colocar então ItemCardapio(ABC).

Guilherme: Como será aplicado esse desconto? Não temos essa informação, e não é relevante para a classe item cardápio. A principal vantagem dessa abordagem é evidenciada quando usamos @abstractmethod. Isso implica que todas as classes derivadas são obrigadas a seguir essa diretriz; quando dizemos "precisam", é uma exigência real.

Nosso código vai parar se não tiver a aplicação desse desconto. E para essa classe, não importa como o desconto é. Não importa nada. Não precisamos implementar. Então podemos colocar dois pontos e na linha de baixo um pass.

Essa forma de pegar um método e dizer que ele deve se moldar de forma diferente em diferentes classes é o que chamamos na programação de polimorfismo. O mesmo método se adapta para uma classe específica e tem um comportamento diferente através desse método abstrato que criamos na nossa classe principal.

'''