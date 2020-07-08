class Impressora:

    def __init__(self):
        self.a = 10

    @classmethod
    def imprimir_folha(cls):
        print('Folha impressa')

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()


Impressora.imprimir_folha()

print("==================")

Impressora.imprimir_livro(5)

print("==================")

impressora = Impressora()

impressora.imprimir_folha()

print("==================")
