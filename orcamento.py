from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.desconto_aplicado = False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass

class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        if(not self.desconto_aplicado):
            orcamento.adiciona_desconto_extra(orcamento.valor*0.02)
            self.desconto_aplicado = True
            print(self.desconto_aplicado)
        else:
            raise Exception('Desconto extra já aplicado')

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orcamento em aprovacao nao pode ir para finalizado')

class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        print(self.desconto_aplicado)
        if(not self.desconto_aplicado):
            print('test')
            orcamento.adiciona_desconto_extra(orcamento.valor*0.05)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto extra já aplicado')

    def aprova(self, orcamento):
        raise Exception('Orcamento ja esta aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento aprovado nao pode ser reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orcamento reprovado nao pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento ja esta reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orcamento finalizado nao pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento finalizado nao pode ser reprovado')

    def finaliza(self, orcamento):
        raise Exception('Orcamento ja finalizado')

class Orcamento:

    def __init__(self):

        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        self.estado_atual.finaliza(orcamento)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def valor(self):
        total = 0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))

    print(orcamento.valor)
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)

