from django.test import TestCase

# Importa o app que será testado
from .models import Product

# Cria uma classe de testes


class ProductStrTestCase(TestCase):

    # Teste se a função str retorna o name
    def test_str_should_return_name(self):
        # Usa uma função auxiliadora do objects
        product = Product.objects.create(
            # passa os campos de produto
            name='Teste Produto',
            description='Teste description',
            price=10.5
        )

        # Faz o assertEquals
        self.assertEqual(str(product), 'Teste Produto')
