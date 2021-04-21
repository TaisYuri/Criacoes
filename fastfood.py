MENU = {'Cheese burger': 10,
        'Bacon burger': 13,
        'Vegan burger': 10,
        'Refrigerante': 5,
        'Batata frita': 6,
        'Batata frita com bacon e cheddar': 8,
        'Sorvete': 2,
        'Sundae': 6  }

class Fastfood:
    def __init__(self, vltotal = 0):
        self.vltotal = vltotal
        self.pedido = pedido ={}

    def apresentar_menu(self):
        for indice, produtos in enumerate(MENU.items()):
            print(f'({indice+1})  {produtos[0]}  R$ {produtos[1]}')

    def fazer_pedido(self,item, qtd):
        self.pedido[item] = qtd

    def altera_qtd(self):
        item = int(input('Escolha o item que deseja alterar: '))
        print(f'item a ser alterado:{item} - qtd: {self.pedido[item]}')
        self.pedido.pop(item)
        novaqtd = int(input('Nova quantidade: '))
        self.pedido[item] = novaqtd

    def exclui_item(self):
        item = int(input('Escolha o item que deseja excluir: '))
        print(f'item excluido: {item} - qtd: {self.pedido[item]}')
        self.pedido.pop(item)


    def fecha_conta(self):
        self.vltotal = 0
        print(f'\n{"Produto":<15} {"Valor Unitário":<15} {"Quantidade":<15} {"Subtotal":<15}')
        for indice,qtd in self.pedido.items():
            for chave, valor in enumerate(MENU.items()):

                if indice == chave + 1:
                    subtotal = valor[1] * qtd
                    self.vltotal += subtotal
                    print(f'({indice}) {valor[0]:<15} R${valor[1]:<15} {qtd:<15} {subtotal:<15}')

        print('-' * 80)
        print(f'{"Total: R$":<15} {self.vltotal:>35}')





