from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos:

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print (imposto_calculado)



from orcamento import Orcamento, Item

orcamento = Orcamento()
orcamento.adiciona_item(Item('Item - 1', 50))
orcamento.adiciona_item(Item('Item - 2', 200))
orcamento.adiciona_item(Item('Item - 3', 250))

calculador = Calculador_de_impostos()


print ('ISS e ICMS')
calculador.realiza_calculo(orcamento, ISS())
calculador.realiza_calculo(orcamento, ICMS())

print ('ISS com ICMS')
calculador.realiza_calculo(orcamento, ISS(ICMS()))

print('ICPP e IKCV')
calculador.realiza_calculo(orcamento, ICPP())
calculador.realiza_calculo(orcamento, IKCV())

print('ICPP com IKCV')
calculador.realiza_calculo(orcamento, ICPP(IKCV()))