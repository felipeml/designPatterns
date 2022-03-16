from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos:

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(
                    Desconto_por_mais_de_quinhentos_reais(
                        Sem_desconto())).calcula(orcamento)

        return desconto

from orcamento import Orcamento, Item

orcamento = Orcamento()
orcamento.adiciona_item(Item('Item - 1', 100))
orcamento.adiciona_item(Item('Item - 2', 50))
orcamento.adiciona_item(Item('Item - 3', 400))

print(orcamento.valor)

calculador = Calculador_de_descontos()

desconto = calculador.calcula(orcamento)

print(f'Desconto calculado {desconto}')