class Mamifero:
    def emitir_som(self):
        pass


class Cachorro(Mamifero):
    def emitir_som(self):
        print('Au, Au')


class Gato(Mamifero):
    def emitir_som(self):
        print('Miau, miau')


class Rato(Mamifero):
    def emitir_som(self):
        print('Squeeee, squeee')


cachorro = Cachorro()
gato = Gato()
rato = Rato()

mamiferos = [cachorro, gato, rato]

for mamifero in mamiferos:
    mamifero.emitir_som()
